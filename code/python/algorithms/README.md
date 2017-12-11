
## Collection of analysis performed using Python :snake:

### The data for the analysis is about 650 MBs and has been put in the google live location shared here
    	
https://drive.google.com/drive/folders/1Z7ZZFldy-XB1koU3JPW7oTQqs-jPGPMD?usp=sharing 
	    											 
### Folder Organization

 -  htmls   	  : Since the map outputs do not render on github, html output documents of previous successful runs  
         	    have been placed here as a demo.  
 - scrap-code     : Intermediate scrap code used in analysis 
 - address_list_x : These files are address from geo-tags in json format. Since most service providers restrict
	   		  decoding geo to address api limits to ~ 2000 calls per day, the decoded addresses have been cached 
			  and kept in these files.


### Important Note

 - This [data](https://drive.google.com/drive/folders/1Z7ZZFldy-XB1koU3JPW7oTQqs-jPGPMD?usp=sharing) has to be downloaded and the variable *data_folder* in the notebook has to be set to the downloaded path for the code to run correctly. 
    	      
### Notebooks

 - [Extended EDA for London](extended-eda-for-london.ipynb)	
 - [Cluster Analysis for patterns in traffic](trends-in-traffic-busy-roads-london.ipynb)
 - [HeatMap of Accidents which has been used for traffic correlation checks](london-heatmap.ipynb)

