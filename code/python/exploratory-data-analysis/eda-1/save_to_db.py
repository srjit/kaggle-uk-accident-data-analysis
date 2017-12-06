import connector


import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
import folium

import json

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


## 


accidents_data_file11 = "data/accidents_2009_to_2011.csv"
accidents_data_file14 = "data/accidents_2012_to_2014.csv"

data1 = pd.read_csv(accidents_data_file11)
data2 = pd.read_csv(accidents_data_file14)

data = pd.concat([data1, data2])

data['Year'] = data['Date'].apply(lambda x : str(x).split("/")[2])
data['Month'] = data['Date'].apply(lambda x : str(x).split("/")[1])
                              
## Co-ordinates of the accident for plotting on map
data["co-ordinates"] = data.apply(lambda x: (x["Latitude"], x["Longitude"]), axis=1)

## Isolate the location
from geopy.geocoders import Nominatim
geolocator = Nominatim()

def get_location(points):
    try:
        import ipdb
        ipdb.set_trace()
        sleep(5)
        return geolocator.reverse(points)
    except:
        return "Error"


def get_address(location):
    try:
        return json.dumps(location.raw['address'])
    except:
        return json.dumps({})

def get_city(location):
    try:
        return location.raw["address"]["city"]
    except:
        return "Unknown"


def get_suburb(location):
    try:
        return location.raw["address"]["suburb"]
    except:
        return "Unknown"

def get_road(location):
    try:
        return location.raw["address"]["road"]
    except:
        return "Unknown"


def get_neighbourhood(location):
    try:
        return location.raw["address"]["neighbourhood"]
    except:
        return "Unknown"

# data = data[0:10]

# data["location"] = data.apply(lambda x: get_location(x["co-ordinates"]), axis=1)
# data["city"] = data.apply(lambda x: get_city(x["location"]), axis=1)
# data["suburb"] = data.apply(lambda x: get_suburb(x["location"]), axis=1)
# data["road"] = data.apply(lambda x: get_road(x["location"]), axis=1)
# data["neighbourhood"] = data.apply(lambda x: get_neighbourhood(x["location"]), axis=1)

# data["address"] = data.apply(lambda x: get_address(x["location"]), axis=1)

# data = data.rename(columns={'Local_Authority_(District)': 'Local_Authority_District', 'Local_Authority_(Highway)': 'Local_Authority_Highway'})
# del data["location"]
# connector.save_to_postgres(data)






data["long_imprecise"] = data.apply(lambda x: str(x["Longitude"])[:4], axis=1)
data["lat_imprecise"] = data.apply(lambda x: str(x["Latitude"])[:4], axis=1)

data["co-ord_imprecise"] = data.apply(lambda x: (x["lat_imprecise"], x["long_imprecise"]), axis=1)

unique_coordinates = pd.unique(data["co-ord_imprecise"]).tolist()


# import json

# def get_address(points):
#     return geolocator.reverse(points).raw["address"]


# samples = []
# serialized_samples = []

# counter = 1

# for i in range(0, 6000, 1000):
#     begin = i
#     end = i+1000

#     tmp = unique_coordinates[begin:end]
#     serialized_samples.append(json.dumps(tmp))

#     filename = "sample_" + str(counter) + ".txt"
#     with open(filename, "w") as f:
#         f.write(json.dumps(tmp))
        
#     samples.append(tmp)
#     counter+=1
    

# tmp = samples.append(unique_coordinates[6000:6023])
# serialized_samples.append(json.dumps(tmp))

# filename = "sample_7.txt"
# with open(filename, "w") as f:
#     f.write(json.dumps(tmp))

# samples.append(tmp)
# counter+=1





# ## getaddresses
# def get_address(points):
# 	global counter
# 	counter+=1
# 	try:
# 	    return geolocator.reverse(points).raw["address"]
# 	except:
# 		print("Error at :", counter)
# 		return "{}"



# ## serialize i-th set
# i = 5

# pts = samples[i]

# # import ipdb
# # ipdb.set_trace()

# addressess = list(map(get_address, pts))
# serialized_addresses = json.dumps(addressess)

# op_file = "address_list_" + str(i) 

# with open(op_file, "w") as f:
#     f.write(serialized_addresses)





## open and read into lists:

addresses = []

for i in range(7):
    filename = "address_list_" + str(i) 

    with open(filename,'r') as f:
        s = f.read()
        tmp = json.loads(s)
        addresses.append(tmp)



addresses_combined = [item for sublist in addresses for item in sublist]


locations = {'co_ordinates':unique_coordinates,
              'address' : addresses_combined }

locations_df = pd.DataFrame(locations, columns=['co_ordinates','address'])


## joining dataframes
_new_data = pd.merge(data, locations_df, how='left', left_on='co-ord_imprecise', right_on='co_ordinates')



def attach_city(x):
    """
    
    Arguments:
    - `x`:
    """
    try:
        # import ipdb
        # ipdb.set_trace()
        return x["address"]["city"]
    except:
        print("Error")
        return "Unknown"


def attach_road(x):
    """
    
    Arguments:
    - `x`:
    """
    try:
        return x["address"]["road"]
    except:
        print("Error")
        return "Unknown"



def attach_suburb(x):
    """
    
    Arguments:
    - `x`:
    """
    try:
        return x["address"]["suburb"]
    except:
        print("Error")
        return "Unknown"
    

_new_data["city"] = _new_data.apply(lambda x: attach_city(x), axis=1)
_new_data["road"] = _new_data.apply(lambda x: attach_road(x), axis=1)
_new_data["suburb"] = _new_data.apply(lambda x: attach_suburb(x), axis=1)




#connector.save_to_postgres(_new_data)



        



# connector.updated_input_dataframe_to_postgres()
    
    
# samples.append(unique_coordinates[6000:6023])

# sample = unique_coordinates[:2000]
# sample1 = unique_coordinates[2000:4000]
# sample2 = unique_coordinates[4000:6000]
# sample3 = unique_coordinates[6000:6023]


    



#data["location_imprecise"] = data.apply(lambda x: get_location(x["co-ord_imprecise"]), axis=1)

#data["lat_imprecise"] = data.apply(lambda x: str(x["Latitude"])[:3], axis=1)

