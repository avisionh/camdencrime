from src.utils.preprocess import count_crime_sort

import os
import pandas as pd


FOLDER_RAW = os.environ.get('DIR_DATA_RAW')
FOLDER_INTERIM = os.environ.get('DIR_DATA_INTERIM')
DATA_CRIME = 'On_Street_Crime_In_Camden.csv'

df = pd.read_csv(filepath_or_buffer=FOLDER_RAW + '/' + DATA_CRIME,
                 parse_dates=['Outcome Date', 'Epoch'])

# explore unique values of possible categorical variables
# to confirm if they are categorical or id variables;
# not many categories for Service nor Location Subtype
# so not very interesting to explore further
categorical_variables = ['Category', 'Outcome Category', 'Service', 'Location Subtype']
unique_categories = [df[x].dropna().unique() for x in categorical_variables]
[len(x) for x in unique_categories]
unique_categories = [sorted(x) for x in unique_categories]

# grouping by Category and Outcome Category to get crime counts
df_category = count_crime_sort(df=df, col='Category')
df_outcome = count_crime_sort(df=df, col='Outcome Category')

# output to files for visualisation
data_dict = {'df_category': df_category, 'df_outcome': df_outcome}
for k, v in data_dict.items():
    v.to_csv(path_or_buf=FOLDER_INTERIM + "/" + k + ".csv", index=False)
