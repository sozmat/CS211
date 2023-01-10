from sun import *
from planet import *
from solarsystem import * 

def main():


    sun = Sun('Sun', 5000, 1000, 6897)
    ss = SolarSystem(sun)

    p = Planet('Elphaba', 14, 10, 23)
    ss.add_planet(p)

    p = Planet('Glinda', 50, 28, 33)
    ss.add_planet(p)

    p = Planet('Fieryo', 11, 5, 90)
    ss.add_planet(p)

    p = Planet('Nessarose', 49, 3, 14)
    ss.add_planet(p)

    ss.show_planets('radius')

if __name__ == '__main__':
    main()

