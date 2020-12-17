import os
import pandas as pd

FOLDER_RAW = os.getenv('DIR_DATA_RAW')
DATA_WARD = 'On_Street_Crime_In_Camden.csv'

# load data
df_ward = pd.read_csv(filepath_or_buffer=FOLDER_RAW + "/" + DATA_WARD)

# get unique wards
wards = df_ward["Ward Name"].unique()
wards = pd.DataFrame(data={"ward_name": wards})

# export to csv
wards.to_csv(path_or_buf="outputs/wards.csv")
