* data provided in the data folder. Be sure to correct your data import directory;

PROC IMPORT OUT= WORK.a0911
            DATAFILE= "F:\Study\courses\DS 5230\project\accident_09_11.csv" 
            DBMS=CSV REPLACE;  GETNAMES=YES;     DATAROW=2; 
RUN;

PROC IMPORT OUT= WORK.a1214
            DATAFILE= "F:\Study\courses\DS 5230\project\accident_12_14.csv" 
            DBMS=CSV REPLACE;  GETNAMES=YES;     DATAROW=2; 
RUN;

* concatenate data;

data accident; set a0911 a1214; run;
proc print data=accident (obs=12);run;


** calculate the occurring frequencies of road accidents for these year to generate heat map in GIS;
proc sort data=accident; by year Location_E Location_N;run;

proc means data=accident noprint; by year Location_E Location_N;
var year; output out=accident_freq mean=/autoname;run;

data accident_freq; set accident_freq;
  drop _TYPE_ Year_Mean; 
  rename _FREQ_ = freq;run;

proc print data=accident_freq (obs=12);run;

proc means data=accident_freq;run;

proc export data=accident_freq
outFILE= "F:\Study\courses\DS 5230\project\accident_freq.csv" 
dbms=csv
replace;
run;

* treat the raw data by creating less groups;

data accident; set accident;
  if number_of_vehicles <3 then number_of_vehicles1 =number_of_vehicles;
  else number_of_vehicles1 = 3; * create three groups of vehicles in the accident;
  if Number_of_Casualties >1 then Number_of_Casualties=2;
  else Number_of_Casualties1=Number_of_Casualties;
  if Weather_Conditions = 'Fine without high winds' then Weather_Conditions1= 'fine';
  if Weather_Conditions = 'Raining without high winds' then Weather_Conditions1= 'rain';
  if Weather_Conditions = 'Raining with high winds' then Weather_Conditions1= 'Fine_with_high_winds';
  if Weather_Conditions = 'Fine with high winds' then Weather_Conditions1= 'Fine_with_high_winds';
  if Weather_Conditions = 'Fine with high winds' then Weather_Conditions1= 'Fine_with_high_winds';
  if Weather_Conditions = 'Fine with high winds' then Weather_Conditions1= 'Fine_with_high_winds';
run;

* perform a logistic regression on the causalties
* the target variable is the number of casualties, where number greater
* than 1 is grouped as 2;

ods graphics on;
proc logistic data=accident;
   class Speed_limit Weather_Conditions;
   model Number_of_Casualties =  Speed_limit Weather_Conditions Speed_limit*Weather_Conditions latitude longitude/ expb;
run;
ods graphics off;


**fast clustering analysis;
proc varclus data=accident;run;

proc fastclus data=accident 
              out=accident_clus
			  maxiter = 100
			  converge = 0
			  radius=100
			  maxclusters=5
			  summary;
run;
