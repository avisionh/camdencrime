from src.utils.preprocess import standardise_column_names
import os
import pandas as pd

FOLDER_PROCESSED = os.getenv('DIR_DATA_PROCESSED')
DATA_CRIME_MAP = 'df_crime_map.pkl'

df = pd.read_pickle(filepath_or_buffer=FOLDER_PROCESSED + "/" + DATA_CRIME_MAP)

# select columns we need
df_crime = df[["Outcome Date",
               "Ward Name",
               "Category",
               "Crime Incidences",
               "Population",
               "Crime Rate"]]
df_crime = standardise_column_names(df=df_crime,
                                    remove_punct=True)

# ensure uniqueness so can use Cypher CREATE for efficient import
df_crime = df_crime.drop_duplicates(subset=["outcome_date",
                                            "ward_name",
                                            "category"])

# export to csv for neo4j
df_crime.to_csv(path_or_buf=FOLDER_PROCESSED + "/" + "df_crime.csv",
                index=False)
