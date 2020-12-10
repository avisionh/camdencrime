import pytest


@pytest.fixture
def lat_long():
    return {'input': [(56.012, -3.61), (56.016, -3.62)],
            'output': (56.01, -3.61)}
