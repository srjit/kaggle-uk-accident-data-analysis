import pandas as pd
import folium
import sklearn.decomposition
import json

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"

data_folder = "/media/sree/mars/data/road-accidents"
accidents_data_file11 = data_folder + "/accidents_2009_to_2011.csv"
accidents_data_file14 = data_folder + "/accidents_2012_to_2014.csv"

data1 = pd.read_csv(accidents_data_file11)
data2 = pd.read_csv(accidents_data_file14)

## 934139
data = pd.concat([data1, data2])
data['Month'] = data['Date'].apply(lambda x : str(x).split("/")[1])

## Lets isolate the accidents in one of the locations where accidents are the most common - London
data["co-ordinates"] = data.apply(lambda x: (x["Latitude"], x["Longitude"]), axis=1)
data["long_imprecise"] = data.apply(lambda x: str(x["Longitude"])[:4], axis=1)
data["lat_imprecise"] = data.apply(lambda x: str(x["Latitude"])[:4], axis=1)
data["co-ord_imprecise"] = data.apply(lambda x: (x["lat_imprecise"], x["long_imprecise"]), axis=1)

unique_coordinates = pd.unique(data["co-ord_imprecise"]).tolist()

addresses = []

## we have grabbed the address in address files
for i in range(7):
    filename = "address_list_" + str(i) 

    with open(filename,'r') as f:
        s = f.read()
        tmp = json.loads(s)
        addresses.append(tmp)


## address 
addresses_combined = [item for sublist in addresses for item in sublist]
locations = {'co_ordinates':unique_coordinates,
              'address' : addresses_combined }
locations_df = pd.DataFrame(locations, columns=['co_ordinates','address'])

#left joining to see what address these come from
data = pd.merge(data, locations_df, how='left', left_on='co-ord_imprecise', right_on='co_ordinates')

## Attaching city
def attach_city(x):
    try:
        return x["address"]["city"]
    except:
        return "Unknown"

data["city"] = data.apply(lambda x: attach_city(x), axis=1)

## Consider London
data_london = data[data['city'] == 'London']

## What are the types of Roads?
road_types = pd.unique(data_london["Road_Type"])


## how is the frequency of accidents on road types
data_london.groupby(['Road_Type']).size()

## most accidents occur in single carriage ways - Singnificantly more than dual carriageways

## has this shift varied over the years
years = [2009, 2010, 2011, 2012, 2013, 2014]
_data = []
[_data.append(data_london[(data_london.Year == year)]) for year in range(2009, 2015)]




road_conditions = ['Dual carriageway','One way street', 'Roundabout', 'Single carriageway',
                        'Slip road', 'Unknown']

road_conditions_grouped_by_year = [_data[i].groupby(['Road_Type']).size().tolist() for i in range(len(_data))]
ys = [[row[j] for row in road_conditions_grouped_by_year] for j in range(5)]

items = pd.unique(data.Road_Type).tolist()
width = 0.15
pos = list(range(len(years))) 
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,6))
plt.bar(pos,ys[0], width, alpha=0.5, color='#9b2f29', label=items[0]) 
plt.bar([p + width for p in pos], ys[1],width, alpha=0.5, color='#EE3224', label=items[1]) 
plt.bar([p + width*2 for p in pos], ys[2], width, alpha=0.5, color='#F78F1E', label=items[2]) 
plt.bar([p + width*3 for p in pos], ys[3], width, alpha=0.5, color='#FFC222', label=items[3]) 
plt.bar([p + width*4 for p in pos], ys[4], width, alpha=0.5, color='#000000', label=items[4]) 
plt.bar([p + width*4 for p in pos], ys[5], width, alpha=0.5, color='#000000', label=items[5]) 

ax.set_ylabel('Accident Count')
ax.set_title('Accidents by road over the years')
ax.set_xticks([p + 1 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(years)

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*8)
plt.ylim([0, max(ys[0] +  ys[1] + ys[2] + ys[3] + ys[4]) + 40000])

# Adding the legend and showing the plot
plt.legend(road_conditions, loc='upper left')
plt.grid()
plt.show()


## why have we chosen to ignore some variables
## only one significant value - None within 50 m
data_london.groupby(data_london["Pedestrian_Crossing-Human_Control"]).size() 





#####  Something to mark the unique road-id and speed
### Form 3-4 clusters
## Examine each cluster
### See how the speed is going and see the what kind of roads these are

features_to_select = ['Speed_limit', '']













## exclude road conditions and see how are accidents getting clustered


## include weather conditions later

from sklearn.preprocessing import LabelEncoder
def dummyEncode(df):
        columnsToEncode = list(df.select_dtypes(include=['category','object']))

        le = LabelEncoder()
        for feature in columnsToEncode:
            try:
                df[feature] = le.fit_transform(df[feature])
            except:
                print('Error encoding '+feature)
        return df

clustering1_data = data_london[features_to_select]
#clustering1_data = data1[features_to_select]
#clustering1_data = dummyEncode(clustering1_data)
pca = sklearn.decomposition.PCA(n_components=2)
pca.fit(clustering1_data)
pca_subsetted_data = pca.transform(clustering1_data)

## plotting
x_data = [x[0] for x in pca_subsetted_data]
y_data = [x[1] for x in pca_subsetted_data]

import matplotlib.pyplot as plt
plt.scatter(x_data, y_data)
plt.show()






## cluster this data
# import numpy as np
# from sklearn.cluster import DBSCAN
# db = DBSCAN(eps=0.7, min_samples=70).fit(clustering1_data)
# core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
# labels = db.labels_

# # Number of clusters in labels, ignoring noise if present.
# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

# print('Estimated number of clusters: %d' % n_clusters_)
# print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
# print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
# print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
# print("Adjusted Rand Index: %0.3f"
#       % metrics.adjusted_rand_score(labels_true, labels))
# print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
# print("Silhouette Coefficient: %0.3f"
#       % metrics.silhouette_score(X, labels))









# speed with the type of road






## extract month and road conditions
london_month_road = data_london[["Month","Road_Surface_Conditions"]]
london_month_road.groupby('Road_Surface_Conditions').Month.unique()
