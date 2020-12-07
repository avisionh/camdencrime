import pandas as pd
import geopandas as gpd


DATA_FOLDER = 'data/raw/'
DATA_CRIME = 'On_Street_Crime_In_Camden.csv'
DATA_MAP = 'geo_export_d270a7b6-0fb4-4fdc-9ed6-15853f2fa0d1.shp'
DATA_LIGHTING = 'geo_export_e87e8b43-cf73-48e4-ad5c-692f56b45394.shp'

df = pd.read_csv(filepath_or_buffer=DATA_FOLDER + '/' + DATA_CRIME,
                 parse_dates=['Outcome Date', 'Epoch'])
shp_camden = gpd.read_file(filename=DATA_FOLDER + '/camden_ward_boundary/' + DATA_MAP)
shp_lighting = gpd.read_file(filename=DATA_FOLDER + '/camden_street_lighting/' + DATA_LIGHTING)

# join between df_crime and shp_camden on ward_name
# check they are consistent
crime_wards = df['Ward Name'].unique()
boundary_wards = shp_camden['name'].unique()
len(crime_wards) == len(boundary_wards)
crime_wards.sort() == boundary_wards.sort()
