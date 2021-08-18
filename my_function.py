from geopy.geocoders import Nominatim
from geopy import distance


def get_distance(locA, locB):
    #use haversine forumla
    cityA = (locA[0], locA[1])
    cityB = (locB[0], locB[1])
    return round(distance.distance(cityA, cityB).km)

def get_latlongs(location):
    geolocator = Nominatim(user_agent='API_KEY')
    result = geolocator.geocode(location)
    return result.latitude, result.longitude

def main(cityA, cityB):
    try:
        distance = get_distance(get_latlongs(cityA), get_latlongs(cityB))
        return (f'Distance between {cityA} and {cityB}: {str(distance)} km')
            
    except:
        return ('Error raised.  Are the input cities correct?')




