class Sun:
    def __init__(self, name: str, mass: float, radius: float, temperature: float):
        """Initializes the object with instance variables
        Args:
            name: string that represents the name of sun
            mass: float that represents the mass of the sun
            radius: float the represents the radius of the sun
            temperature: float that represents temperature of sun
        """
        self.__name = name
        self.__mass = mass
        self.__radius = radius
        self.__temperature = temperature



    def get_mass(self) -> float:
        """Returns the mass of the sun as a float"""
        return self.__mass

    def get_radius(self) -> float:
        """Returns the radius of the sun as a float"""
        return self.__radius

    def get_temperature(self) -> float:
        """Returns the temperature of the sun as a float""" 
        return self.__temperature

    def __str__(self):
        """Returns sun instance variables in string format
        Args:
            name: name of the sun
            radius: radius of the sun
            mass: mass of the sun
            temperature: how hot the sun is
        """
        return self.__name + f'{(self.__mass, self.__radius, self.__temperature)}'

    def get_name(self):
        """Returns the name of the sun"""
        return self.__name
        
        