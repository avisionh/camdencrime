from math import cos, sin, atan2, sqrt, radians, degrees


def get_lat_long_centre(geolocations: tuple) -> tuple:
    """
    Get a relatively accurate centre for latitude and longitude coordinates passed in.

    :param geolocations: Tuple of tuples of latitude and longitude in degrees
    :return: Tuple of central latitude and longitude in radians
    """

    x, y, z = 0, 0, 0

    for lat, lon in geolocations:
        lat_rad, lon_rad = radians(lat), radians(lon)
        lat, lon = float(lat_rad), float(lon_rad)
        x += cos(lat) * cos(lon)
        y += cos(lat) * sin(lon)
        z += sin(lat)

    x = float(x / len(geolocations))
    y = float(y / len(geolocations))
    z = float(z / len(geolocations))

    hyp = sqrt(x * x + y * y)
    lat = degrees(atan2(z, hyp))
    lon = degrees(atan2(y, x))

    return lat, lon
