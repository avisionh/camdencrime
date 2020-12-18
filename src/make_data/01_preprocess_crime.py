from src.utils.preprocess import count_sort_crime

import os
import pandas as pd


FOLDER_RAW = os.environ.get('DIR_DATA_RAW')
FOLDER_INTERIM = os.environ.get('DIR_DATA_INTERIM')
DATA_CRIME = 'On_Street_Crime_In_Camden.csv'

# import data
df = pd.read_csv(filepath_or_buffer=FOLDER_RAW + "/" + DATA_CRIME,
                 parse_dates=["Outcome Date", "Epoch"])
# from src/make_data/graph_ward.py
df_pop = pd.read_csv(filepath_or_buffer='outputs/wards.csv')

# extract year
df["Outcome Year"] = pd.DatetimeIndex(data=df["Outcome Date"]).year
df["Outcome Month"] = pd.DatetimeIndex(data=df["Outcome Date"]).month

# explore unique values of possible categorical variables
# to confirm if they are categorical or id variables;
# not many categories for Service nor Location Subtype
# so not very interesting to explore further
categorical_variables = ["Category", "Outcome Category", "Service", "Location Subtype"]
unique_categories = [df[x].dropna().unique() for x in categorical_variables]
[len(x) for x in unique_categories]
unique_categories = [sorted(x) for x in unique_categories]

# join on population data
df = df.dropna(subset=["Outcome Year"])
df["Outcome Year"] = df["Outcome Year"].astype(int)
df_pop["Outcome Year"] = df_pop["Outcome Year"].astype(int)
df = df.merge(right=df_pop,
              how='left',
              on=["Ward Code", "Ward Name", "Outcome Year"],
              validate='many_to_one')

# grouping by Category and Outcome Category to get crime counts
df_category = count_sort_crime(df=df,
                               date_col=["Outcome Date", "Outcome Year", "Outcome Month"],
                               group_cols=["Ward Name", "Category", "Population"])
df_outcome = count_sort_crime(df=df,
                              date_col=["Outcome Date", "Outcome Year", "Outcome Month"],
                              group_cols=["Ward Name", "Outcome Category", "Population"])

# get proportions for comparing across wards
df_category["Crime Rate"] = df_category["Crime Incidences"] / df_category["Population"]
df_outcome["Crime Rate"] = df_outcome["Crime Incidences"] / df_outcome["Population"]

# output to files for visualisation
data_dict = {"df_category": df_category, "df_outcome": df_outcome, "df_pop": df_pop}
for k, v in data_dict.items():
    v.to_csv(path_or_buf=FOLDER_INTERIM + "/" + k + ".csv", index=False)
