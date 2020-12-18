from typing import Union
import pandas as pd
import string
import re


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


def standardise_column_names(df: pd.DataFrame, remove_punct: bool = True) -> pd.DataFrame:
    """
    Converts all DataFrame column names to lower case replacing whitespace of any
    length with a single underscore. Can also strip all punctuation from column names.
    Reference:
    - https://gist.github.com/georgerichardson/db66b686b4369de9e7196a65df45fc37

    :param df: DataFrame with non-standardised column names.
    :param remove_punct: Boolean (default True), if True will remove all punctuation from column names.

    :return: df: DataFrame with standardised column names.
    """

    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

    for c in df.columns:
        c_mod = c.lower()
        if remove_punct:
            c_mod = c_mod.translate(translator)
        c_mod = '_'.join(c_mod.split(' '))
        if c_mod[-1] == '_':
            c_mod = c_mod[:-1]
        c_mod = re.sub(r'\_+', '_', c_mod)
        df = df.rename(columns={c: c_mod}, inplace=False)
    return df
