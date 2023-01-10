import math

class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float):
        """Initializes the object with instance variables
        Args:
            name: name of the planet in string format
            radius: radius of the planet in float
            mass: mass of the planet in float
            distance: how far planet is from sun
        """
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__distance = distance

    def get_volume(self) -> float:
        """Returns the volume of the planet as a float"""
        volume = (4/3) * math.pi * (self.__radius * self.__radius * self.__radius)
        return volume

    def get_surface_area(self) -> float:
        """Returns the surface area of the planet as a float"""
        surface_area = 4 * math.pi * (self.__radius**2)
        return surface_area

    def get_density(self) -> float:
        """Returns the density of the planet as a float
        """
        density = self.__mass / self.get_volume()
        return density

    def get_radius(self) -> float:
        """Returns the radius of the planet"""
        return self.__radius

    def get_mass(self) -> float:
        """Returns the mass of the planet"""
        return self.__mass

    def get_distance(self) -> float:
        """Returns the distance of the planet to the sun"""
        return self.__distance

    def set_name(self, new_name:str) -> str:
        """ Sets the name to the planet
        Args:
            name: the name of the planet
        """
        self.__name = new_name
        return new_name

    def __str__(self):
        """Provides string representation for object
        Args:
            name: name to be converted into a string
            radius: radius of planet in string form
            mass: mass of the planet in string form
            distance: distance of planet from sun in string form
        """
        return self.__name

    def get_name(self) -> str:
        """Returns the name of the planet"""
        return self.__name
        
        
        