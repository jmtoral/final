# BarceinasToral
FINAL PROJECT

The main page of project is here:

http://localhost:8000/maps/map/

(We are trying to upload our page to: http://jmtrl.pythonanywhere.com/maps/, however, it has still some mistakes)


+++ Background +++
Violence in Mexico skyrocketed between 2006 and 2010, when former President Felipe Calderon Hinojosa declared the war against drug cartels. Since then, there has been several attempts to reduce violence in Mexico. We believe that the provision of public goods at a local scale could have a significant impact reducing violence, through a reduction in crime.
Our proxy to public goods was the provision of social infrastructure to rural localities by the program '3x1'. This program coordinates federal and municipal agencies to use infrastructure budget to match funds from emigrant clubs of Mexicans in United States. Emigrant clubs in the US fund infrastructure projects a while ago, but the idea is to use those resources more efficiently, and combine efforts to provide public goods in rural areas of Mexico.
Likewise, we used a dataset on crime to approach the problem of violence in Mexico. We decided to use rural areas under the assumption that violence in those areas must be related, unlike violence in urban areas, to drug cartels activities.

+++ Description of datasets +++
To prove this hypothesis, we gathered data at the Municipal (County) level from the following sources:
+ Mexican Ministry of Social Development:
++ Through a transparency solitude, we get data from the number of projects by municipalities rom 2013 and 2014.
+Mexican Executive Secretariat of Public Safety:
++From the website [http://secretariadoejecutivo.gob.mx/incidencia-delictiva/incidencia-delictiva-fuero-comun.php] we downloaded the database of all the crimes from the local jurisdiction by municipalities.

+++ Step 1: Cleaning up datasets +++
The first challenge we went through was that we had the dataset on public goods and crime in different levels of aggregation. While the crime dataset contained the information for each municipality, the information on the '3x1' program was stored at the locality level (one municipality contains several localities).
We overcome this by noting that each locality has a unique id made of 'state id' & 'municipality id' & 'locality id', and so we used state and municipality ids to group the localities into one municipality. This id was useful in further steps of transforming the database into a geopandas dataframe.
The entire process of cleaning an merging can be seen in our file “bases_B.ipynb”. The result of this process of cleaning is the archive “mater.csv” with our data of interest.

+++ Step 2
We use geopandas to put an interactive map in the very first page of our site. However we were unable to store them on the fly. The codes of our maps are saved in our file "mapas.ipynb".


+++ Results

This app can graph "on the fly" an scatterplot of the municipalities in Mexico. This graph have, in the y-axis, the homicide rate in 2014 per 100,000 population. In addition, the app display a table with all the relevan data per state.

When clik on the menu "Data by State" a menu will appear with the name of each Mexican State. Each submenu will contain relevant information by state.
