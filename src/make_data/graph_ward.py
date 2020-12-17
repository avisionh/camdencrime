from src.utils.preprocess import standardise_column_names
import os
import pandas as pd

FOLDER_RAW = os.getenv('DIR_DATA_RAW')
DATA_POP = 'Population_20Projections_20_latest_20GLA_20set_.xlsx'

# load data
df_pop = pd.read_excel(io=FOLDER_RAW + "/" + DATA_POP,
                       sheet_name="WardP Summry",
                       header=None,
                       names=['Ward Code',
                              'Ward Name',
                              '2015',
                              '2016',
                              '2017',
                              '2018',
                              '2019',
                              '2020'],
                       usecols="B,D,K:P",
                       skiprows=5,
                       nrows=18)

# unpivot/melt population data
df_pop = pd.melt(frame=df_pop,
                 id_vars=["Ward Code", "Ward Name"],
                 var_name="Outcome Year",
                 value_name="Population")

# standardise column names
df_pop = standardise_column_names(df=df_pop, remove_punct=True)
df_pop = df_pop.drop(columns=["unnamed_0"])

# export to csv
df_pop.to_csv(path_or_buf="outputs/wards.csv", index=False)
