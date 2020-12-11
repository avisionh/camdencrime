from src.utils.helper_geo import get_lat_long_centre

import os
import pandas as pd
import geopandas as gpd
import branca.colormap as cm
import folium
from folium.plugins import TimeSliderChoropleth

DATA_FOLDER = os.environ.get('DIR_DATA_RAW')
DATA_CRIME = 'On_Street_Crime_In_Camden.csv'
DATA_MAP = 'geo_export_d270a7b6-0fb4-4fdc-9ed6-15853f2fa0d1.shp'
DATA_LIGHTING = 'geo_export_e87e8b43-cf73-48e4-ad5c-692f56b45394.shp'

df = pd.read_csv(filepath_or_buffer=DATA_FOLDER + '/' + DATA_CRIME,
                 parse_dates=['Outcome Date', 'Epoch'])
shp_camden = gpd.read_file(filename=DATA_FOLDER + '/camden_ward_boundary/' + DATA_MAP)
shp_lighting = gpd.read_file(filename=DATA_FOLDER + '/camden_street_lighting/' + DATA_LIGHTING)

# count number of incidents per ward per date
df_transform = df.value_counts(subset=['Outcome Date', 'Ward Name']).reset_index()
df_transform = df_transform.rename(columns={0: 'Crime Incidences'})
df_transform = df_transform.sort_values(by=['Ward Name', 'Outcome Date'], axis=0)

# remove NaT from Outcome Date column
df_transform = df_transform.dropna(subset=['Outcome Date'])


# join between df_crime and shp_camden on ward_name
# check they are consistent
crime_wards = df_transform['Ward Name'].unique()
boundary_wards = shp_camden['name'].unique()
len(crime_wards) == len(boundary_wards)
crime_wards.sort() == boundary_wards.sort()

df_camden = df_transform.merge(right=shp_camden, how='left', left_on='Ward Name', right_on='name')

# convert Outcome Date to unix time in nanoseconds so can output html
df_camden['Outcome Sec'] = df_camden['Outcome Date'].astype(int) / 10**9
df_camden['Outcome Sec'] = df_camden['Outcome Sec'].astype(int).astype(str)
df_camden = df_camden[['Outcome Sec', 'Ward Name', 'Crime Incidences', 'geometry']]

# plotting on map
# https://www.jumpingrivers.com/blog/interactive-maps-python-covid-19-spread/
# define colour map w.r.t Crime Incidences
max_colour = max(df_camden['Crime Incidences'])
min_colour = min(df_camden['Crime Incidences'])
cmap = cm.linear.YlOrRd_09.scale(min_colour, max_colour)
df_camden['Colour'] = df_camden['Crime Incidences'].map(cmap)

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
gdf_ward = df_camden[['geometry']]
gdf_ward = gpd.GeoDataFrame(data=gdf_ward)
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
cmap.caption = "Number of crime incidences per Ward"
slider_map.save(outfile='outputs/timesliderchoropleth_crimeincidences.html')
