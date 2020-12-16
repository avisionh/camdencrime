from src.utils.preprocess import count_sort_crime


def test_count_sort_crime(df_ungroup, df_group):
    count_sort_crime(df=df_ungroup,
                     date_col='Outcome Date',
                     group_cols=['Ward Name', 'Category']).equals(df_group)
