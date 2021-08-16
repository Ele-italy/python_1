from geopy.geocoders import Nominatim
import numpy as np


def get_distance(locA, locB):
    #use haversine forumla
    earth_rad = 6371.0
    dlat = np.deg2rad(locB[0] - locA[0])
    dlon = np.deg2rad(locB[1] - locA[1])
    a = np.sin(dlat/2) * np.sin(dlat/2) + \
        np.cos(np.deg2rad(locA[0])) * np.cos(np.deg2rad(locB[0])) * \
        np.sin(dlon/2) * np.sin(dlon/2) 
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return round(earth_rad * c)

def get_latlongs(location):
    geolocator = Nominatim(user_agent='API_KEY')
    result = geolocator.geocode(location)
    return result.latitude, result.longitude

def main(cityA, cityB):
    #get first city
    #cityA = input('Type the first City: ')
    
    #get second city
    #cityB = input('Type the secong City: ')

            
    #find the distance in km
    try:
        distance = get_distance(get_latlongs(cityA), get_latlongs(cityB))
        return (f'Distance between {cityA} and {cityB}: {str(distance)} km')
            
    except:
        return ('Error raised.  Are the input cities correct?')
        
            
#if __name__ == '__main__':
   # main()


