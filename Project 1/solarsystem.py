import planet

class SolarSystem:
    def __init__(self, a_sun:str):
        """Initializes the object and makes instance variables
        Args:
            a_sun: a string that represents the sun in the solar system
        """
        self.__the_sun = a_sun
        self.__planets = []

    def add_planet(self, a_planet):
        """Adds planets into the solar system
        Args:
            a_planet: a planet that is to be added into the solar system
        """
        self.__planets.append(a_planet)
        #when i print this list it is a list of object addresses



    def show_planets(self, sortby: str = None):
        """ Prints the planets sorted by a specific factor
        Args:
            sortby: describes by which element to sort the planets
        """
        if sortby == 'name':
            variable = planet.Planet.get_name
            
        elif sortby == 'distance':
            variable = planet.Planet.get_distance

        elif sortby == 'mass':
            variable = planet.Planet.get_mass

        else:
            variable = planet.Planet.get_radius

        
        for a_planet in sorted(self.__planets, key = variable):
            print(a_planet)




            

                

                


