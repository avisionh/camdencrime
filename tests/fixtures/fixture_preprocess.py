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
