import os
import pandas as pd
import geopandas as gpd

FOLDER_RAW = os.getenv('DIR_DATA_RAW')
FOLDER_PROCESSED = os.getenv('DIR_DATA_PROCESSED')
DATA_LIGHT = 'geo_export_e87e8b43-cf73-48e4-ad5c-692f56b45394.shp'

df_light = gpd.read_file(filename=FOLDER_RAW + "/camden_street_lighting/" + DATA_LIGHT)

# aggregate to get key info
df_lamp = df_light.groupby(by=["ward_name", "lamp_type"]).agg(func={"street_nam": 'count',
                                                                    "wattage": 'mean'})
df_lamp = df_lamp.reset_index()
df_lamp = df_lamp.rename(columns={"street_nam": "count_lamps",
                                  "wattage": "mean_wattage"})
df_lamp['date'] = pd.to_datetime('2020-12-04')

# ensure uniqueness so can use Cypher CREATE for efficient import
df_lamp = df_lamp.drop_duplicates(subset=["ward_name", "lamp_type"])

# export to csv for neo4j
df_lamp.to_csv(path_or_buf=FOLDER_PROCESSED + "/" + "df_lamp.csv",
               index=False)
