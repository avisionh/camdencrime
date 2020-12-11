import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def df_ungroup():
    return pd.DataFrame(data={'Outcome Date': ['2017-04-01',
                                               pd.NaT,
                                               '2016-07-01',
                                               '2016-07-01'],
                              'Category': ['Other theft',
                                           'Anti-social behaviour',
                                           'Drugs',
                                           'Drugs'],
                              'Outcome Category': [np.nan,
                                                   'Under investigation',
                                                   'Under investigation',
                                                   'Offender sent to prison']})


@pytest.fixture
def df_group():
    return pd.DataFrame(data={'Outcome Date': ['2016-07-01', '2017-04-01'],
                              'Category': ['Drugs', 'Other theft'],
                              'Crime Incidences': [2, 1]})
