from src.utils.preprocess import count_sort_crime

import os
import pandas as pd


FOLDER_RAW = os.environ.get('DIR_DATA_RAW')
FOLDER_INTERIM = os.environ.get('DIR_DATA_INTERIM')
DATA_CRIME = 'On_Street_Crime_In_Camden.csv'
DATA_POP = 'Population_20Projections_20_latest_20GLA_20set_.xlsx'


# import data
df = pd.read_csv(filepath_or_buffer=FOLDER_RAW + "/" + DATA_CRIME,
                 parse_dates=["Outcome Date", "Epoch"])
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
                 var_name="Date Year",
                 value_name="Population")

# extract year
df["Date Year"] = pd.DatetimeIndex(data=df["Outcome Date"]).year
df["Date Month"] = pd.DatetimeIndex(data=df["Outcome Date"]).month

# explore unique values of possible categorical variables
# to confirm if they are categorical or id variables;
# not many categories for Service nor Location Subtype
# so not very interesting to explore further
categorical_variables = ["Category", "Outcome Category", "Service", "Location Subtype"]
unique_categories = [df[x].dropna().unique() for x in categorical_variables]
[len(x) for x in unique_categories]
unique_categories = [sorted(x) for x in unique_categories]

# join on population data
df = df.dropna(subset=["Date Year"])
df["Date Year"] = df["Date Year"].astype(int)
df_pop["Date Year"] = df_pop["Date Year"].astype(int)
df = df.merge(right=df_pop,
              how='left',
              on=["Ward Code", "Ward Name", "Date Year"],
              validate='many_to_one')
df = df.rename(columns={"Date Year": "Outcome Year",
                        "Date Month": "Outcome Month"})

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

# get year and month
df_category["Date Year"] = pd.DatetimeIndex(data=df_category["Outcome Date"]).year
df_category["Date Month"] = pd.DatetimeIndex(data=df_category["Outcome Date"]).month
df_outcome["Date Year"] = pd.DatetimeIndex(data=df_outcome["Outcome Date"]).year
df_outcome["Date Month"] = pd.DatetimeIndex(data=df_outcome["Outcome Date"]).month

# output to files for visualisation
data_dict = {"df_category": df_category, "df_outcome": df_outcome}
for k, v in data_dict.items():
    v.to_csv(path_or_buf=FOLDER_INTERIM + "/" + k + ".csv", index=False)
