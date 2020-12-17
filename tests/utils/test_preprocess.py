from src.utils.preprocess import count_sort_crime, standardise_column_names


def test_count_sort_crime(df_ungroup, df_group):
    count_sort_crime(df=df_ungroup,
                     date_col='Outcome Date',
                     group_cols=['Ward Name', 'Category']).equals(df_group)


def test_standardise_column_names(df_messy_names, df_clean_names):
    df = standardise_column_names(df=df_messy_names,
                                  remove_punct=True)
    df.equals(df_clean_names)
