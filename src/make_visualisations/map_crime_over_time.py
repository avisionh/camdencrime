from src.utils.helper_geo import get_lat_long_centre

import os
import pandas as pd
import geopandas as gpd
import branca.colormap as cm
import folium
from folium.plugins import TimeSliderChoropleth

FOLDER_PROCESSED = os.environ.get('DIR_DATA_PROCESSED')
DATA_CRIME_MAP = 'df_crime_map.pkl'

# plotting on map
# https://www.jumpingrivers.com/blog/interactive-maps-python-covid-19-spread/

df_camden = pd.read_pickle(filepath_or_buffer=FOLDER_PROCESSED + "/" + DATA_CRIME_MAP)
# remove NaT from Outcome Date column
df_camden = df_camden.dropna(subset=['Outcome Sec'])

# define colour map w.r.t Crime Rate
max_colour = max(df_camden['Crime Rate'])
min_colour = min(df_camden['Crime Rate'])
cmap = cm.linear.YlOrRd_09.scale(min_colour, max_colour)
df_camden['Colour'] = df_camden['Crime Rate'].map(cmap)

# construct style dictionary for choropleth mapping
ward_list = df_camden['Ward Name'].unique().tolist()
ward_idx = range(len(ward_list))

style_dict = {}
for i in ward_idx:
    ward = ward_list[i]
    result = df_camden[df_camden['Ward Name'] == ward]
    inner_dict = {}
    for _, r in result.iterrows():
        inner_dict[r['Outcome Sec']] = {'color': r['Colour'], 'opacity': 0.7}
    style_dict[str(i)] = inner_dict

# make df with features of each ward
gdf_ward = gpd.GeoDataFrame(data=df_camden[['geometry']])
gdf_ward = gdf_ward.drop_duplicates().reset_index()

# set projection for accurate centroid mapping
centroid = gdf_ward.centroid
centroid = list(zip(list(centroid.x), list(centroid.y)))
centroid = get_lat_long_centre(geolocations=centroid)
# reverse ordering for centering map
centroid = (centroid[1], centroid[0])

# make map and add colourbar
# - can then add some prediction on crime levels in future
# - add labels of wards
# - add popups of crime level numbers
slider_map = folium.Map(location=centroid,
                        zoom_start=13,
                        max_bounds=True,
                        tiles='cartodbpositron')
_ = TimeSliderChoropleth(data=gdf_ward.to_json(),
                         styledict=style_dict).add_to(slider_map)
_ = cmap.add_to(slider_map)
cmap.caption = "Crime Rate per Ward"
slider_map.save(outfile='outputs/timesliderchoropleth_crimeincidences.html')
