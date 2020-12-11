import pandas as pd


def count_crime_sort(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Groups by a Outcome Date and another column before counting rows and sorting results.

    :param df: Dataframe to group, count and sort.
    :param col: Column to group by.
    :return: Dataframe of grouped counts that is sorted.
    """
    df = df.value_counts(subset=['Outcome Date', col]).reset_index()
    df = df.rename(columns={0: 'Crime Incidences'})
    df = df.sort_values(by=[col, 'Outcome Date'], axis=0)
    return df
