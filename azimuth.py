import re
from math import radians, cos, sin, asin, sqrt

class location(object):
    def __init__(self, coord_string=""):
        super(location, self).__init__()
        self.coord_string = coord_string
        if self.coord_string:
            self.lon, self.lat = self.parse_lonlat(self.coord_string)
        else: self.lon, self.lat = 0.0, 0.0
        
    def parse_lonlat(self, coord):
        """ Pass in string in degrees like "( 24d37'55.25\"W, 73d42'10.75\"S)"
        Returns decimal tuple (lon, lat)
        """
        latlon_regex = r"\(\s*(\d+)d(\d+)'([\d.]+)\"([WE]),\s*(\d+)d(\d+)'([\d.]+)\"([NS])\s*\)"
        m = re.match(latlon_regex, coord)
        parts = m.groups()
        lat = int(parts[0]) + float(parts[1]) / 60 + float(parts[2]) / 3600
        if parts[3] == 'W':
            lat *= -1
        lon = int(parts[4]) + float(parts[5]) / 60 + float(parts[6]) / 3600
        if parts[7] == 'S':
            lon *= -1
        return (lon, lat)

    def haversine(self, other):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [self.lon, self.lat, other.lon, other.lat])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 

        # 6367 km is the radius of the Earth
        km = 6367 * c
        return km

    def manhattan(self, other):
        corner = location()
        corner.lon = other.lon
        corner.lat = self.lat
        xd = self.haversine(corner)
        yd = other.haversine(corner)
        return (xd,yd)



A = location("(18d26'10.71\"E, 33d54'32.83\"S)")
B = location("(18d25'22.15\"E, 33d56'19.19\"S)")

print "Distances\n=========\nLongitudinal: %f km\nLatitudinal:  %f km" % A.manhattan(B)
