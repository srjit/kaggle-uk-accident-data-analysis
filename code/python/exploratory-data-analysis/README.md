### Exploratory Data Analysis performed to understand attributes of the accident

#### Folder Organization

 -  [htmls](htmls)   	  : Since the map outputs do not render on github, html output documents of previous successful runs  
         	    have been placed here as a demo.  
 - [scrap-code](scrap)     : Intermediate scrap code used in the eda for testing
 - address_list_x : These files are address from geo-tags in json format. Since most service providers restrict
       	   	  decoding geo to address api limits to ~ 2000 calls per day, the points have been extracted, grouped into 6 batches		        	 for decoding, and the decoded addresses have been cached as files
			  and kept in these files.
 - [co-ordinates](sample-coordinates) : Collection of points, which are analysed later in 6 batches
    		    	  
#### Dependencies

  1) pandas==0.21.0
  2) matplotlib==2.0.2
  3) folium==0.5.0
  4) json==1.35
  5) scikit-learn==0.19.1

  
#### Notebook
  1) [Accidents - EDA](analysis-of-external-factors.ipynb)
     
