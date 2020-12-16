from typing import Union
import pandas as pd


def count_sort_crime(df: pd.DataFrame, date_col: Union[list, str], group_cols: list) -> pd.DataFrame:
    """
    Groups by a Outcome Date and another column before counting rows and sorting results.

    :param df: Dataframe to group, count and sort.
    :param date_col: List or string of column that has date information in.
    :param group_cols: List or dictionary of columns to group by, excluding date.
                        Pass columns in order you want to group by.
    :return: Dataframe of grouped counts that is sorted.
    """
    if isinstance(date_col, str):
        date_col = [date_col]

    df = df.value_counts(subset=date_col + group_cols).reset_index()
    df = df.rename(columns={0: 'Crime Incidences'})
    df = df.sort_values(by=group_cols + date_col, axis=0)

    return df
