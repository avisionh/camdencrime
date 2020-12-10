from src.utils.helper_geo import get_lat_long_centre


def test_get_lat_long_centre(lat_long):
    centre = get_lat_long_centre(geolocations=lat_long['input'])
    centre = tuple([round(number=x, ndigits=2) for x in centre])
    assert centre == lat_long['output']
