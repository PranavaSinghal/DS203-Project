import geopandas as gpd
from matplotlib import pyplot as plt
import pandas as pd
import mapclassify
import libpysal

 # Importing the files
data = pd.read_csv('countryx2_random.csv')
countries = gpd.read_file("Shape file/World_Countries.shp")

countries = countries.rename(columns={'COUNTRY': 'Country'})

countries = countries.set_index('Country')
data = data.set_index('Country')
mergedDF = pd.merge(countries, data, left_index=True, right_index=True)

mergedDF.plot(cmap='OrRd', column='coalcons_ej', figsize= (70,35),scheme='quantiles',  k=20, legend = True)

x = pd.isnull(mergedDF["geometry"])
plt.savefig('foo.png')