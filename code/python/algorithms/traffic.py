import pandas as pd

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"

traffic_data_file = "ukTrafficAADF.csv"

traffic_data = pd.read_csv(traffic_data_file)
traffic_data_london = traffic_data[traffic_data.Region == "London"]


valid_years = [2009, 2010, 2011, 2012, 2013, 2014]

traffic_data_london = traffic_data_london[traffic_data_london["AADFYear"].isin(valid_years)]


## just consider year 2009
traffic_data_london_09 = traffic_data_london[traffic_data_london["AADFYear"] == 2009]


traffic_data_london_09["road_segment_id"] = traffic_data_london.apply(lambda x : 
                                                                          x["Road"] + "_" + 
                                                                          str(x["Easting"]) + "_" + 
                                                                          str(x["Northing"]), axis=1)

## cluster roads with same kind of traffic for cycles - Remove pedalcycles
features = ['Motorcycles', 'CarsTaxis', 'BusesCoaches', 'AllMotorVehicles']
motor_vehicles = traffic_data_london_09[features]


## Has there been a shift in the traffic in london's roads


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(motor_vehicles)

## 2 is the optimal number of clusters
from sklearn.metrics import silhouette_score
silhouette_score(motor_vehicles, kmeans.labels_)


## we have two clusters
road_name = traffic_data_london_09["road_segment_id"].tolist()
kmeans.labels_

roads_0 = set([r for (cluster,r) in zip(kmeans.labels_, road_name) if cluster == 0])
roads_1 = set([r for (cluster,r) in zip(kmeans.labels_, road_name) if cluster == 1])

motor_vehicles["cluster_assigned"] = kmeans.labels_


traffic_data_london_09["cluster_assigned"] = kmeans.labels_

cluster_0 = traffic_data_london_09[traffic_data_london_09.cluster_assigned == 0]
cluster_1 = traffic_data_london_09[traffic_data_london_09.cluster_assigned == 1]



## clustered with heavy traffic areas
## filter rows which are assigned to cluster 1
cluster_1 = motor_vehicles[motor_vehicles.cluster_assigned == 1]



## plot these points on folium - Roads with most 4 wheeler traffic in the area



## visualize the clusers
## we have the details of 1837 roads - let's visualize this
from sklearn import decomposition
pca = decomposition.PCA(n_components=1)
pca.fit(motor_vehicles)
X = pca.transform(motor_vehicles)
X.flatten()

import matplotlib.pyplot as plt
plt.plot(X.flatten(), 'x')
plt.show()
road_tags = traffic_data_london_09.Road.tolist()


## look at the traffic data for roads that have come for cluster 1

x = [2,3,4,5]
y = [0.7933, 0.608, 0.568, 0.492]
