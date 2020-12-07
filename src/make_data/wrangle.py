import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


DATA_FOLDER = 'data/raw/'
DATA_CRIME = 'On_Street_Crime_In_Camden.csv'
DATA_MAP = 'geo_export_e87e8b43-cf73-48e4-ad5c-692f56b45394.shp'

df = pd.read_csv(filepath_or_buffer=DATA_FOLDER + '/' + DATA_CRIME,
                 parse_dates=['Outcome Date', 'Epoch'])
shp_camden = gpd.read_file(filename=DATA_FOLDER + '/camden_street_lighting/' + DATA_MAP)

# create points using lat and long
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
# create GeoDataFrame to hold the Geo Series
df_crime = gpd.GeoDataFrame(data=df, geometry=geometry)
