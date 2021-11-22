# -*- coding: utf-8 -*-


import geopandas as gpd
from matplotlib import pyplot as plt
import pandas as pd


countries_shape = gpd.read_file("Shape file/World_Countries.shp")
countries_shape = countries_shape.rename(columns={'COUNTRY': 'Country'})
countries_shape = countries_shape.set_index('Country')  
                             
# data is the data to plot. Dataframe of countriesx2
def geoPlot(data, colorScheme = 'YlGn', fileName = 'plot'):
    data = data.set_index('Country')
    ### Changing Russian Federation to Russia
    as_list = data.index.tolist()
    idx = as_list.index('Russian Federation')
    as_list[idx] = 'Russia'
    data.index = as_list
    ### Changing US to United States
    as_list = data.index.tolist()
    idx = as_list.index('US')
    as_list[idx] = 'United States'
    data.index = as_list
    ### Changing "Curacao" to "Curacao (Netherlands)"
    as_list = data.index.tolist()
    idx = as_list.index('Curacao')
    as_list[idx] = 'Curacao (Netherlands)'
    data.index = as_list
    ### Changing "Democratic Republic of Congo" to "Democratic Republic of the Congo"
    as_list = data.index.tolist()
    idx = as_list.index('Democratic Republic of Congo')
    as_list[idx] = 'Democratic Republic of the Congo'
    data.index = as_list
    ### Changing "Trinidad & Tobago" to "Trinidad and Tobago"
    as_list = data.index.tolist()
    idx = as_list.index('Trinidad & Tobago')
    as_list[idx] = 'Trinidad and Tobago'
    data.index = as_list
    ### Setting index name
    data.index.name = 'Country'

    pd.data.columns = ['Country', 'Data']
    mergedDF = countries_shape.join(data)
    
    mergedDF.plot(cmap = colorScheme, column='Data', figsize= (70,35),
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
    plt.savefig(fileName + '.png')