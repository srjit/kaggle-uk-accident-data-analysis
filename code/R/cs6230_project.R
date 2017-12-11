library(ggplot2)
library(dplyr)
library(xts)
library(date)
library(scales)
library(forecast)
library(lubridate)
library(gridExtra)
library(data.table)

### Data import 
path = "F:/Study/courses/DS 5230/project/1-6m-accidents-traffic-flow-over-16-years"
data_import1 <- paste(path, "accidents_2012_to_2014.csv",sep="/")
data_import2 <- paste(path, "accidents_2005_to_2007.csv",sep="/")
data_import3 <- paste(path, "accidents_2009_to_2011.csv",sep="/")

data_lsoa_london_imp <-  paste(path, "LSOA_2011_London_gen_MHW.csv",sep="/")

data_import4 <- paste(path,"ukTrafficAADF.csv",sep="/")

a05_07 <- read.csv(data_import2,head=TRUE, na.strings=c("","NA"))
a09_11 <- read.csv(data_import3,head=TRUE, na.strings=c("","NA"))
a12_14 <- read.csv(data_import1,head=TRUE, na.strings=c("","NA"))

traf <- read.csv(data_import4,head=TRUE, na.strings=c("","NA"))

london0507 <- read.csv("F:/Study/courses/DS 5230/project/1-6m-accidents-traffic-flow-over-16-years/acc0507lon.csv",
                 head=TRUE, na.strings=c("","NA"))


london0911 <- read.csv("F:/Study/courses/DS 5230/project/1-6m-accidents-traffic-flow-over-16-years/acc0911lon.csv",
                       head=TRUE, na.strings=c("","NA"))


london1214 <- read.csv("F:/Study/courses/DS 5230/project/1-6m-accidents-traffic-flow-over-16-years/acc1214lon.csv",
                       head=TRUE, na.strings=c("","NA"))

london_accident <- rbind(london0507,london0911,london1214)

#write.csv(london_accident1,file="F:/Study/courses/DS 5230/project/1-6m-accidents-traffic-flow-over-16-years/london_accident.csv")

# ggplot themes
themeblank_twolines <- theme_bw()+
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        panel.background = element_blank(), axis.line = element_line(colour = "black"))+
  theme(panel.border = element_blank(),
        axis.line.x = element_line(size = 0.5, linetype = "solid", colour = "black"),
        axis.line.y = element_line(size = 0.5, linetype = "solid", colour = "black"))

themeblank_twolines1 <- theme_bw()

themeblank <- theme_bw()+
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        panel.background = element_blank(), axis.line = element_line(colour = "black"))

## basic data

accident <- rbind(a05_07,a09_11,a12_14)

accident <- accident %>% 
  mutate(hour=substr(Time,1,2),minute=substr(Time,4,5)) %>% 
  mutate(hour=as.numeric(hour)+1,minute=as.numeric(minute),
         month=month(Date))

setnames(traf,old=c('Lat','Lon'),new=c('Latitude','Longitude'))

hour_case <- accident %>% 
  group_by(hour1,Accident_Severity) %>% 
  summarise(count=n(),freq=n()/length(accident$Year)) %>% 
  filter(hour1!=0) 

hour_case1 <- hour_case %>% 
  group_by(hour1) %>% 
  summarise(count1=sum(count)) %>% 
  right_join(hour_case,by=c('hour1')) %>% 
  mutate(hfreq=count/count1)
week_count <- accident %>% 
  group_by(Day_of_Week) %>% 
  summarise(count=n())

week_count1 <- accident %>% 
  group_by(Day_of_Week,hour1) %>% 
  summarise(count=n()) %>% 
  filter(hour1!='NA')
month_count <- accident %>% 
  mutate(month=month(Date)) %>% 
  group_by(month) %>% 
  summarise(mcount=n())

year_rate <- accident %>% 
  group_by(Year) %>% 
  summarise(count=n())

p_hour <- ggplot(hour_case,aes(hour1,count))+
  geom_bar(stat = "identity")+
  labs(x='Hour',y='Accident frequency')+
  themeblank_twolines

p_week <- ggplot(week_count1,aes(as.factor(Day_of_Week),count))+
  geom_bar(stat = "identity")+
  labs(x='Week ',y='Accident frequency')+
  #scale_x_discrete(limits=c(2005,2014),breaks=seq(2005,2014,2))+
  scale_y_continuous(limits=c(0,250000),breaks=seq(0,250000,25000))+
  coord_cartesian(ylim = c(150000, 250000)) +
  scale_x_discrete(labels=c("1" = "Mon", "2" = "Tue",'3'='Wed','4'='Thu',
                            "5" = "Fri",'6'='Sat','7'='Sun'))+
  themeblank_twolines

p_month <- ggplot(month_count,aes(month,mcount))+
  geom_bar(stat = "identity")+
  labs(x='Month ',y='Accident frequency')+
  scale_y_continuous(limits=c(0,140000),breaks=seq(0,140000,10000))+
  coord_cartesian(ylim = c(100000, 140000))+
  scale_x_continuous(limits=c(0,13),breaks=seq(0,13,1))+
  themeblank_twolines
p_year <- ggplot(year_rate,aes(Year,count))+
  geom_bar(stat = "identity")+
  labs(x='Year',y='Accident frequency')+
  #scale_x_discrete(limits=c(2005,2014),breaks=seq(2005,2014,2))+
  scale_y_continuous(limits=c(0,200000),breaks=seq(0,200000,20000))+
  coord_cartesian(ylim = c(100000, 200000)) +
  scale_x_continuous(limits=c(2005,2015),breaks=seq(2005,2015,2))+
  themeblank_twolines+
  theme(legend.position = "None")
grid.arrange(p_year,p_month,p_week,p_hour,ncol=2)


####################################################
#### Analysis of the frequencies of the main covariates

p_road_type <- ggplot(accident,aes(fct_rev(fct_infreq(factor(Road_Type)))))+
  geom_bar()+
  themeblank_twolines+
  labs(x="",y='')+
  annotate("text", x = 1.2, y = 9.5e+05, label = "a) Road type")+
  theme(axis.text.x = element_text(angle = 30, hjust = 1))


p_road_surface <- ggplot(subset(accident,Road_Surface_Conditions !='NA'),
                         aes(fct_rev(fct_infreq(factor(Road_Surface_Conditions)))))+
  geom_bar()+
  labs(x="",y='')+
  annotate("text", x = 1.2, y = 1000000, label = "b) Road surface")+
  themeblank_twolines+
  theme(axis.text.x = element_text(angle = 30, hjust = 1))

p_light <- ggplot(accident,aes(fct_rev(fct_infreq(factor(Light_Conditions)))))+
  geom_bar()+
  labs(x="",y='')+
  annotate("text", x = 1, y = 9.5e+05, label = "c) Street light")+
  themeblank_twolines+
  theme(axis.text.x = element_text(angle = 30, hjust = 1))

grid.arrange(p_road_type,p_road_surface,p_light,ncol=1)

##### drive speed, weather and pedestrian plot

p_speed <- ggplot(subset(accident,Speed_limit!='NA'),
                  aes(fct_rev(fct_infreq(factor(Speed_limit)))))+
  geom_bar()+
  labs(x="",y='')+
  annotate("text", x = 1.2, y = 1000000, label = "a) Speed")+
  themeblank_twolines+
  theme(axis.text.x = element_text(angle = 30, hjust = 1))

p_pedestrian_human <- ggplot(subset(accident,Pedestrian_Crossing.Physical_Facilities!='NA'),
                             aes(fct_rev(fct_infreq(factor(Pedestrian_Crossing.Physical_Facilities)))))+
  geom_bar()+
  labs(x="",y='')+
  annotate("text", x = 1.5, y = 1200000, label = "b) Pedestrian facility")+
  themeblank_twolines+
  theme(axis.text.x = element_text(angle = 30, hjust = 1))


p_weather <- ggplot(subset(accident,Weather_Conditions !='NA'),
                 aes(fct_rev(fct_infreq(factor(Weather_Conditions)))))+
  geom_bar()+
  labs(x="",y='')+
  annotate("text", x = 1.5, y = 1000000, label = "c) Weather")+
  themeblank_twolines+
  theme(axis.text.x = element_text(angle = 30, hjust = 1))

grid.arrange(p_speed,p_weather,p_pedestrian_human,ncol=1)

####################################################
####Clustering analysis on the time

### note:
## based on above analysis, we have identified several key patterns, therefore, 
## I narrow down my analysis subset the data without the perturbations of confounders


site_freq <- accident %>% 
  group_by(Year,Longitude,Latitude) %>% 
  summarise(freq=n()) %>% 
  filter(Longitude!='NA')

site_freq_high <- site_freq %>% 
  filter(freq>=5)

UK <- map_data(map = "world", region = "UK") # changed map to "world"

p_uk <- ggplot() + 
  geom_polygon(data = UK, aes(x = long, y = lat, group = group),color='grey80') +
  coord_map()+
  themeblank

par(mfrow = c(3, 3))
par(mar = c(2.5, 3.5, 1, 0.5))
par(mgp = c(1.5, 0.5, 0))
par(oma = c(0, 0, 3, 0))
p_freq_high <- p_uk + geom_point(data=subset(site_freq_high,Year>2000),
                  aes(Longitude,Latitude),color="red")+
  facet_wrap(~Year,ncol=3)



#### treat the data into doable format
### select important variables such as: Latitude, Longitude, Day_of_Week,Road_Type,
#### Speed_limit, Light_Conditions,Weather_Conditions,Road_Surface_Conditions, hour,
#### month;
variables <- c('Latitude', 'Longitude', 'Day_of_Week','Road_Type','Speed_limit', 
               'Light_Conditions','Weather_Conditions','Road_Surface_Conditions', 'hour','month','Year')

accident1 <- accident[,variables]


###### convert every variables into monthly level data, the frequency of incidence in each month represent
###### the rate of 
accident1 <- accident1 %>% 
  mutate(date2=as.Date(paste(Year,month,'01',sep='/')))

Daylight1 <- accident1 %>% 
  filter(Light_Conditions==unique(accident$Light_Conditions)[1]) %>% 
  group_by(date2) %>% 
  summarise(light1=n())

Daylight2 <- accident1 %>% 
  filter(Light_Conditions==unique(accident$Light_Conditions)[2]) %>% 
  group_by(date2) %>% 
  summarise(light2=n())

Daylight3 <- accident1 %>% 
  filter(Light_Conditions==unique(accident$Light_Conditions)[3]) %>% 
  group_by(date2) %>% 
  summarise(light3=n())

Daylight4 <- accident1 %>% 
  filter(Light_Conditions==unique(accident$Light_Conditions)[4]) %>% 
  group_by(date2) %>% 
  summarise(light4=n())

Daylight5 <- accident1 %>% 
  filter(Light_Conditions==unique(accident$Light_Conditions)[5]) %>% 
  group_by(date2) %>% 
  summarise(light5=n())

light <- accident_month %>% 
  left_join(Daylight1,by=c('date2')) %>% 
  left_join(Daylight2,by=c('date2')) %>%
  left_join(Daylight3,by=c('date2')) %>%
  left_join(Daylight4,by=c('date2')) %>%
  left_join(Daylight5,by=c('date2')) 

light <- light %>% 
  mutate(light1r=light1/incidence,light2r=light2/incidence,light3r=light3/incidence,light4r=light4/incidence,
         light5r=light5/incidence)

light <- light[,c(1:2,8:12)]
colnames(light) <- c('date2','incidence','Daylight: Street light present','Darkness: Street lights present and lit',  
                     'Darkness: Street lighting unknown','Darkness: Street lights present but unlit',
                     'Darkeness: No street lighting' )

# standardize data
light_stan <- as.data.frame(scale(light[,c(3:7)]))

### Factor analysis with rotation
res1a = factanal(light_stan, factors = 2, rotation = "varimax", na.action = na.omit)
res1a$loadings

### Plot loadings against one another
load = res1a$loadings[,1:2]
plot(load, type="n") # set up plot 
text(load,labels=names(light_stan),cex=.7) # add variable names



# Pricipal Components Analysis
# entering raw data and extracting PCs 
# from the correlation matrix 
fit <- princomp(light_stan, cor=TRUE)
summary(fit) # print variance accounted for 
loadings(fit) # pc loadings 
plot(fit,type="lines") # scree plot 
fit$scores # the principal components
biplot(fit)

# PCA Variable Factor Map 
library(FactoMineR)

result <- PCA(light_stan) # graphs generated automatically
text(load,labels=names(light_stan),cex=.7)


### weather conditions
dry <- accident1 %>% 
  filter(Road_Surface_Conditions==unique(accident$Road_Surface_Conditions)[1]) %>% 
  group_by(date2) %>% 
  summarise(dry=n())

wet <- accident1 %>% 
  filter(Road_Surface_Conditions==unique(accident$Road_Surface_Conditions)[2]) %>% 
  group_by(date2) %>% 
  summarise(wet=n())

frost <- accident1 %>% 
  filter(Road_Surface_Conditions==unique(accident$Road_Surface_Conditions)[3]) %>% 
  group_by(date2) %>% 
  summarise(frost=n())

snow <- accident1 %>% 
  filter(Road_Surface_Conditions==unique(accident$Road_Surface_Conditions)[4]) %>% 
  group_by(date2) %>% 
  summarise(snow=n())

weather <- dry %>% 
  left_join(wet,by=c('date2')) %>% 
  left_join(frost,by=c('date2')) %>% 
  left_join(snow,by=c('date2'))
  


### hierarchical analysis

a14 <- accident %>% 
  filter(Year==2014)
a14_data <- a14[,c("Number_of_Casualties" ,'Speed_limit','Latitude','Longitude')] %>% 
  mutate(casualties = ifelse(Number_of_Casualties==1,Number_of_Casualties,
                             ifelse(Number_of_Casualties==2,Number_of_Casualties,3)))

a14_data <-  a14_data[!rowSums((is.na(a14_data))),]

a14m <- a14 %>% 
  filter(Number_of_Casualties<10)

#convert all to factor variables
i=0
while(i < ncol(a14_data)){
  i=i+1  
  a14_data[,i] = as.factor(a14_data[,i])
}


install.packages(c("FactoMineR", "factoextra"))
 
 library("FactoMineR")
 library("factoextra")
 
 library("FactoMineR")

 library(FactoMineR)
 res.famd <- FAMD(a14_data, graph = FALSE)
 print(res.famd)
 
 library("factoextra")
 eig.val <- get_eigenvalue(res.famd)
 head(eig.val)
 
 fviz_screeplot(res.famd)
 
 var <- get_famd_var(res.famd)
 var

 # Coordinates of variables
 head(var$coord)
 # Cos2: quality of representation on the factore map
 head(var$cos2)
 # Contributions to the  dimensions
 head(var$contrib)
 
 # Plot of variables
 fviz_famd_var(res.famd, repel = TRUE)
 # Contribution to the first dimension
 fviz_contrib(res.famd, "var", axes = 1)
 # Contribution to the second dimension
 fviz_contrib(res.famd, "var", axes = 2)
 
 quanti.var <- get_famd_var(res.famd, "quanti.var")
 quanti.var 
 
 
 fviz_famd_var(res.famd, "quanti.var", repel = TRUE,
               col.var = "black")
 
 
 #### mixed types clustering
 set.seed(1680) # for reproducibility
 
 library(dplyr) # for data cleaning
 library(ISLR) # for college dataset
 library(cluster) # for gower similarity and pam
 library(Rtsne) # for t-SNE plot
 library(ggplot2) # for visualization
 
 
 college_clean <- ISLR::College %>%
   mutate(name = row.names(.),
          accept_rate = Accept/Apps,
          isElite = cut(Top10perc,
                        breaks = c(0, 50, 100),
                        labels = c("Not Elite", "Elite"),
                        include.lowest = TRUE)) %>%
   mutate(isElite = factor(isElite)) %>%
   select(name, accept_rate, Outstate, Enroll,
          Grad.Rate, Private, isElite)
 
 # Remove college name before clustering
 
 gower_dist <- daisy(college_clean[, -1],
                     metric = "gower",
                     type = list(logratio = 3))
 
 # Check attributes to ensure the correct methods are being used
 # (I = interval, N = nominal)
 # Note that despite logratio being called, 
 # the type remains coded as "I"
 
 gower_mat <- as.matrix(gower_dist)
 
 # Output most similar pair
 
 college_clean[
   which(gower_mat == min(gower_mat[gower_mat != min(gower_mat)]),
         arr.ind = TRUE)[1, ], ]
 
 
 # Calculate silhouette width for many k using PAM
 
 sil_width <- c(NA)
 
 for(i in 2:10){
   
   pam_fit <- pam(gower_dist,
                  diss = TRUE,
                  k = i)
   
   sil_width[i] <- pam_fit$silinfo$avg.width
   
 }
 
 
 
 # Plot sihouette width (higher is better)
 
 plot(1:10, sil_width,
      xlab = "Number of clusters",
      ylab = "Silhouette Width")
 lines(1:10, sil_width)
 
 
 pam_fit <- pam(gower_dist, diss = TRUE, k = 3)
 
 pam_results <- college_clean %>%
   dplyr::select(-name) %>%
   mutate(cluster = pam_fit$clustering) %>%
   group_by(cluster) %>%
   do(the_summary = summary(.))
 
 pam_results$the_summary
 
 
 college_clean[pam_fit$medoids, ]
 
 
 
 
 tsne_obj <- Rtsne(gower_dist, is_distance = TRUE)
 
 tsne_data <- tsne_obj$Y %>%
   data.frame() %>%
   setNames(c("X", "Y")) %>%
   mutate(cluster = factor(pam_fit$clustering),
          name = college_clean$name)
 
 ggplot(aes(x = X, y = Y), data = tsne_data) +
   geom_point(aes(color = cluster))
 
 
 
 
 
 
 