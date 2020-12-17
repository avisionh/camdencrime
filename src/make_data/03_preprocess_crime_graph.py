import os
import pandas as pd
import geopandas as gpd

FOLDER_RAW = os.getenv('DIR_DATA_RAW')
FOLDER_PROCESSED = os.getenv('DIR_DATA_PROCESSED')
DATA_CRIME = 'df_crime_map.pkl'
DATA_LIGHT = 'geo_export_e87e8b43-cf73-48e4-ad5c-692f56b45394.shp'

df_camden = pd.read_pickle(filepath_or_buffer=FOLDER_PROCESSED + "/" + DATA_CRIME)
df_light = gpd.read_file(filename=FOLDER_RAW + "/camden_street_lighting/" + DATA_LIGHT)

# aggregate to get key info
df_lamp = df_light.groupby(by=["ward_name", "lamp_type"]).agg(func={"street_nam": 'count',
                                                                    "wattage": 'mean'})
df_lamp = df_lamp.reset_index()
df_lamp = df_lamp.rename(columns={"street_nam": "count_lamps",
                                  "wattage": "mean_wattage"})

# join to get relationships
df_crime_lamp = df_camden.merge(right=df_lamp,
                                how='left',
                                left_on="Ward Name",
                                right_on="ward_name",
                                validate='many_to_many')

# export to csv for neo4j
df_out = df_crime_lamp[["Outcome Date",
                        "Ward Name",
                        "Category",
                        "Crime Incidences",
                        "Population",
                        "Crime Rate",
                        "lamp_type",
                        "count_lams",
                        "mean_wattage"]]
