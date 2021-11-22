import geopandas as gpd
from matplotlib import pyplot as plt
import pandas as pd


 # Importing the files
data = pd.read_csv('countryx2_random.csv')
countries_shape = gpd.read_file("Shape file/World_Countries.shp")



 # Renaming one column from Shapefile
countries_shape = countries_shape.rename(columns={'COUNTRY': 'Country'})
 # Setting index as countries and merging the DFs
countries_shape = countries_shape.set_index('Country')
data = data.set_index('Country')
mergedDF = countries_shape.join(data)

mergedDF.plot(cmap='YlGn', column='coalcons_ej', figsize= (70,35),
              scheme='quantiles',  k=19, 
              legend = True,
              missing_kwds={
                  "color": "lightgrey",
                  "edgecolor": "grey",
                  "hatch": "///",
                  "label": "Missing values",
                  },
              legend_kwds={
                  "fontsize":40,
                  "loc" :"lower left",
                  #"ncol" : 10,
                  'markerscale' : 4,
                  }
              )
plt.axis('off')
plt.savefig('YlGn.png')

#listOfCountry = []
#for countryInData in countryData:
 #   if not(countryInData in countryMap):
 #       listOfCountry.append(countryInData)