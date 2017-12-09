import pandas as pd
import folium

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


accidents_data_file11 = "data/accidents_2009_to_2011.csv"
accidents_data_file14 = "data/accidents_2012_to_2014.csv"

data1 = pd.read_csv(accidents_data_file11)
data2 = pd.read_csv(accidents_data_file14)

data = pd.concat([data1, data2])

## what columns do we have 
columns = data1.columns

## Exploratory data analysis on the data



## Questions to answers
## 1. are accidents seasonal ?
## 2. What kind of accidents are prominent at what times of the year ?
## 3.  


## Which road had the most number of accidents?

## What types of roads do we have in the UK?
road_types = data1.Road_Type.unique()

## On what road types to most accidents occur?
accidents_road_types_grouping_11 = data1.groupby(['Road_Type']).size()
accidents_road_types_grouping_14 = data2.groupby(['Road_Type']).size()
accidents_road_types_grouping_total = data.groupby(['Road_Type']).size()



## how many rows do we have
## 934139
len(data1)
len(data2)
len(data)

data["co-codinates"] = data1[["Longitude","Latitude"]].apply(lambda x,y: (x,y))
## data1['co-ordinates'] = data1["Longitude"],data["Latitude"])



# One person died in most cases - every record has atleast one dead person
casuality_count_grouped = data.groupby(['Number_of_Casualties']).size()


## How many casualities are caused in most accidents
## Binning the number of casualities 
#data['casuality_binned'] = pd.cut(data["Number_of_Casualties"], 20, retbins=True)[0]

## upto 2011
#data1['casuality_binned'] = pd.cut(data1["Number_of_Casualties"], 20, retbins=True)[0]
casuality_count_grouped_data1 = data1.groupby(['casuality_binned']).size()


## upto 2014
data2['casuality_binned'] = pd.cut(data2["Number_of_Casualties"], 20, retbins=True)[0]
casuality_count_grouped_data2 = data2.groupby(['casuality_binned']).size()









#########################################################################################################
### On which day do most accidents occur?

data.groupby(['Day_of_Week']).size()

## During what time of the day does accidents occur the most
















## which is the place where most number of accidents have happened









## bin the number of casualities and see where are the accidents occuring the most

map_hooray = folium.Map(location=[51.5074, 0.1278], zoom_start = 11)
map_hooray.render()




# Build a heatmap that change with time







## cluster for accident types - are they seasonal?

## check the existing kernels 
