import pandas as pd
import folium
import sklearn.decomposition

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


## held up the season variable indicated by the month - Should i include the information 
## about the place?
subsetted_data = data[['Accident_Severity', 'Weather_Conditions', 'Road_Surface_Conditions', 
                           'Special_Conditions_at_Site', 'Urban_or_Rural_Area', 'Number_of_Vehicles',
                           'Number_of_Casualties','Light_Conditions']]

## Seasons and LSOA_of_Accident_Location



subsetted_data['Weather_Conditions'] = subsetted_data['Weather_Conditions'].astype('str')
subsetted_data['Road_Surface_Conditions'] = subsetted_data['Road_Surface_Conditions'].astype('str')
subsetted_data['Special_Conditions_at_Site'] = subsetted_data['Special_Conditions_at_Site'].astype('str')




################   PCA Components    ################     

## sklearn encoder
from sklearn.preprocessing import LabelEncoder

#Auto encodes any dataframe column of type category or object.
def dummyEncode(df):
        # columnsToEncode = list(df.select_dtypes(include=['Weather_Conditions',
        #                         'Road_Surface_Conditions', 'Special_Conditions_at_Site', 
        #                         'Urban_or_Rural_Area','Light_Conditions']))

        columnsToEncode = list(df.select_dtypes(include=['category','object']))

        le = LabelEncoder()
        for feature in columnsToEncode:
            try:
                df[feature] = le.fit_transform(df[feature])
            except:
                print('Error encoding '+feature)
        return df



## pca
subsetted_data = dummyEncode(subsetted_data)
pca = sklearn.decomposition.PCA(n_components=10)
pca.fit(subsetted_data)

pca_subsetted_data = pca.transform(subsetted_data)
## Explained Varience
print(pca.explained_variance_ratio_)  
print(pca.singular_values_)



### plot the PCA here ### 





################   DBScan on these     ################     


from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(subsetted_data)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))


# #############################################################################
# Plot result
import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
