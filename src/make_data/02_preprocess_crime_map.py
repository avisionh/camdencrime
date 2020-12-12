import os
import pandas as pd
import geopandas as gpd

FOLDER_RAW = os.environ.get('DIR_DATA_RAW')
FOLDER_INTERIM = os.environ.get('DIR_DATA_INTERIM')
FOLDER_PROCESSED = os.environ.get('DIR_DATA_PROCESSED')
DATA_CRIME_CATEGORY = 'df_category.csv'
DATA_MAP = 'geo_export_d270a7b6-0fb4-4fdc-9ed6-15853f2fa0d1.shp'


# load data
df_crime = pd.read_csv(filepath_or_buffer=FOLDER_INTERIM + "/" + DATA_CRIME_CATEGORY,
                       parse_dates=['Outcome Date'])
shp_camden = gpd.read_file(filename=FOLDER_RAW + "/camden_ward_boundary/" + DATA_MAP)

# check can join on 'Ward Name' - is okay
crime_wards = df_crime['Ward Name'].unique()
boundary_wards = shp_camden['name'].unique()
len(crime_wards) == len(boundary_wards)
crime_wards.sort() == boundary_wards.sort()

# join df_crime with shp_camden on 'Ward Name'
df_crime_map = df_crime.merge(right=shp_camden,
                              how='left',
                              left_on='Ward Name',
                              right_on='name')

# convert Outcome Date to unix time in nanoseconds so can output html
df_crime_map['Outcome Sec'] = df_crime_map['Outcome Date'].astype(int) / 10**9
df_crime_map['Outcome Sec'] = df_crime_map['Outcome Sec'].astype(int).astype(str)

# save for mapping
df_crime_map.to_pickle(path=FOLDER_PROCESSED + '/df_crime_map.pkl')
