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


## Cyclists


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