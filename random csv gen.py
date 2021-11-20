import pandas as pd
import numpy as np
import geopandas as gpd
import shapefile as shp

df = pd.read_excel("data/bp-stats-review-2021-consolidated-dataset-panel-format.xlsx")
df2 = df[df["Year"] == 2015]
df3 = df2[["Country", "coalcons_ej"]]
remove_entries = ['USSR','China Hong Kong SAR','Total Africa', 'Total Asia Pacific', 'Total CIS', 'Total Central America', 'Total Eastern Africa', 'Total Europe',
                  'Total European Union', 'Total Middle Africa', 'Total Middle East', 'Total Non-OECD', 'Total North America', 
                  'Total OECD', 'Total S. & Cent. America', 'Total Western Africa']
df4 = df3.set_index('Country')
### Changing Russian Federation to Russia
as_list = df4.index.tolist()
idx = as_list.index('Russian Federation')
as_list[idx] = 'Russia'
df4.index = as_list
### Changing US to United States
as_list = df4.index.tolist()
idx = as_list.index('US')
as_list[idx] = 'United States'
df4.index = as_list

df4.index.name = 'Country'

df4 = df4.drop(remove_entries, axis=0)
df4.to_csv(r'countryx2_random.csv')