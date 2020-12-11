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

# grouping by Category to get crime counts
df_category = df.value_counts(subset=['Outcome Date', 'Category']).reset_index()
df_category = df_category.rename(columns={0: 'Crime Incidences'})
df_category = df_category.sort_values(by=['Category', 'Outcome Date'], axis=0)

# start grouping by Outcome Category
df_outcome = df.value_counts(subset=['Outcome Date', 'Outcome Category']).reset_index()
df_outcome = df_outcome.rename(columns={0: 'Crime Incidences'})
df_outcome = df_outcome.sort_values(by=['Outcome Category', 'Outcome Date'], axis=0)

# output to files for visualisation
df_category.to_csv(path_or_buf=FOLDER_INTERIM + "/" + "df_category.csv",
                   index=False)
df_outcome.to_csv(path_or_buf=FOLDER_INTERIM + "/" + "df_outcome.csv",
                  index=False)
