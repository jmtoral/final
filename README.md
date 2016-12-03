# BarceinasToral
FINAL PROJECT

+++ Background +++
Violence in Mexico skyrocketed between 2006 and 2010, when former President Felipe Calderon Hinojosa declared the war against drug cartels. Since then, there has been several attempts to reduce violence in Mexico. We believe that the provision of public goods at a local scale could have a significant impact reducing violence, through a reduction in crime.
To prove this hypothesis, we gathered data at the Municipal (County) level from the following sources:
+ Public goods- datos.gob.mx
+ Crime -
+ Demographic information- conapo.gob.mx ????
+ Geographic information- conabio.gob.mx

Our proxy to public goods was the provision of social infrastructure to rural localities by the program '3x1'. This program coordinates federal and municipal agencies to use infrastructure budget to match funds from emigrant clubs of Mexicans in United States. Emigrant clubs in the US fund infrastruture projects a while ago, but the idea is to use those resources more efficiently, and combine efforts to provide public goods in rural areas of Mexico.
Likewise, we used a dataset on crime to approach the problem of violence in Mexico.... We decided to use rural areas under the assumption that violence in those areas must be related, unlike violence in urban areas, to drug cartels activities... ????

+++ Description of datasets +++

+++ Challenge 1: Cleaning up datasets +++
The first challenge we went through was that we had the dataset on public goods and crime in different levels of aggregation. While the crime dataset contained the information for each municipality, the information on the '3x1' program was stored at the locality level (one municipality contains several localities). 
We overcome this by noting that each locality has a unique id made of 'state id' & 'municipality id' & 'locality id', and so we used state and municipality ids to group the localities into one municipality. This id was useful in further steps of transforming the database into a geopandas dataframe.
(ESCRIBIR AQUI CODIGO LIMPIO DE BASES DE DATOS)

+++ Challenge 2: 


+++ 