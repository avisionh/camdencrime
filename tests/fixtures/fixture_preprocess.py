import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def df_ungroup():
    return pd.DataFrame(data={'Outcome Date': ['2017-04-01',
                                               pd.NaT,
                                               '2016-07-01',
                                               '2016-07-01'],
                              'Ward Name': ["King's Cross",
                                            "Highgate",
                                            "Kilburn",
                                            "Kilburn"],
                              'Category': ['Other theft',
                                           'Anti-social behaviour',
                                           'Drugs',
                                           'Drugs'],
                              'Outcome Category': [np.nan,
                                                   'Under investigation',
                                                   'Under investigation',
                                                   'Offender sent to prison'],
                              'Population': [34655,
                                             67981,
                                             22322,
                                             22322]})


@pytest.fixture
def df_group():
    return pd.DataFrame(data={'Outcome Date': ['2016-07-01', '2017-04-01'],
                              'Ward Name': ["Kilburn", "King's Cross"],
                              'Category': ['Drugs', 'Other theft'],
                              'Crime Incidences': [2, 1],
                              'Population': [22322, 34655]})


@pytest.fixture
def df_messy_names():
    return pd.DataFrame({'Column With Spaces': [1, 2, 3, 4, 5],
                         'Column-With-Hyphens&Others/': [6, 7, 8, 9, 10],
                         'Too    Many Spaces': [11, 12, 13, 14, 15]})


@pytest.fixture
def df_clean_names():
    return pd.DataFrame({'column_with_spaces': [1, 2, 3, 4, 5],
                         'column_with_hyphens_others': [6, 7, 8, 9, 10],
                         'too_many_spaces': [11, 12, 13, 14, 15]})
