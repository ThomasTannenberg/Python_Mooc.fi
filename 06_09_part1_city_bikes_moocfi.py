import math

def read_file(filename: str):

    station_list = []

    with open(filename) as file:
        for line in file:
            line = line.replace('\n', '')

            if 'Longitude' in line:
                continue

            rows = line.split(';')

            station_list.append(rows)

    return station_list

def get_station_data(filename: str):
    station_list = read_file(filename)

    stations = {}

    for station in station_list:
        name = station[3]
        longtitude = float(station[0])
        latitude = float(station[1])

        stations[name] = (longtitude, latitude)
    
    return stations

def distance(stations: dict, station1: str, station2: str):

    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2

    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

# Debug and Testing code
if __name__ == "__main__":
    print('DEBUG: read_file output: ')
    print(read_file('stations1.csv'))
    print('-----------------')
    print('-----------------')
    print('-----------------')
    print('DEBUG: get_station_data: ')
    print(get_station_data('stations1.csv'))
    print('-----------------')
    print('-----------------')
    print('-----------------')
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
