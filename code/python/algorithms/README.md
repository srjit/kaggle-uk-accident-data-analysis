
## Collection of analysis performed using Python :snake:

#### Author: Sreejith Sreekumar   	      

#### The data for the analysis is about 650 MBs and has been put in the google live location shared here
    	
https://drive.google.com/drive/folders/1Z7ZZFldy-XB1koU3JPW7oTQqs-jPGPMD?usp=sharing 
	    											 
#### Folder Organization

 -  [htmls](htmls)   	  : Since the map outputs do not render on github, html output documents of previous successful runs  
         	    have been placed here as a demo.  
 - [scrap-code](scrap-code)     : Intermediate scrap code used in analysis - Clusterings which didn't give fruitful results / Time 
 - address_list_x : These files are address from geo-tags in json format. Since most service providers restrict
	   		  decoding geo to address api limits to ~ 2000 calls per day, the decoded addresses have been cached 
			  and kept in these files.


#### Dependencies
  1) pandas==0.21.0
  2) matplotlib==2.0.2
  3) folium==0.5.0
  4) json==1.35
  5) scikit-learn==0.19.1

     
#### Important Note

 - The [data](https://drive.google.com/drive/folders/1Z7ZZFldy-XB1koU3JPW7oTQqs-jPGPMD?usp=sharing) has to be downloaded and the variable *data_folder* in the notebooks has to be set to the downloaded path for the code to run correctly. 

   	      
#### Notebooks

 - [Extended EDA for London](extended-eda-for-london.ipynb)	
 - [Cluster Analysis for patterns in traffic](trends-in-traffic-busy-roads-london.ipynb)
 - [HeatMap of Accidents which has been used for traffic correlation checks](london-heatmap.ipynb)

