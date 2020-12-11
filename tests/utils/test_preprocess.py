from src.utils.preprocess import count_crime_sort


def test_count_crime_sort(df_ungroup, df_group):
    count_crime_sort(df=df_ungroup, col='Category').equals(df_group)
