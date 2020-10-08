#calculating distance between two points on the surface of the Earth
#knowing latitude/longitude of the two points using Haversine formula
#Haversine formula:
#a = sin^2(delta phi) + cos(phi1)*cos(phi2)*sin^2(delta lambda/2)
#c = 2*atan2(sqrt(a),sqrt(1-a))
#d = R * c
#where phi is latitude, lambda is longitude, R is earth's radius (R = 6371)

import math
import utils.get_input

def calculate_distance(latitude_one:float,latitude_two:float,longitude_one:float,longitude_two:float):
    r = 6371

    #convert degree to radian
    phi_one = latitude_one * math.pi/180
    phi_two = latitude_two * math.pi/180
    delta_phi = (latitude_two - latitude_one) * math.pi/180
    delta_lambda = (longitude_two - longitude_one) * math.pi/180

    #getting a
    a = pow(math.sin(delta_phi/2), 2) + math.cos(phi_one) * math.cos(phi_two) * pow(math.sin(delta_lambda/2), 2)

    #getting c
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    #calculating distance
    d = r * c

    return d

def main():
    latitude_one = float(utils.get_input.number("Enter the latitude of point 1: "))
    longitude_one = float(utils.get_input.number("Enter the longitude of point 1: "))
    latitude_two = float(utils.get_input.number("Enter the latitude of point 2: "))
    longitude_two = float(utils.get_input.number("Enter the longitude of point 2: "))

    distance = calculate_distance(latitude_one, latitude_two, longitude_one, longitude_two)
    print(f"The distance between two point is {distance:0.4f}km")

main()