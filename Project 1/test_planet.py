import unittest
import planet

class T0_Planet_test_methods(unittest.TestCase):
    """ Tests the methods of the Planet class """
    
    def test_get_volume(self):
        """Check whether volume for planet is correct"""
        planet_object = planet.Planet('Elphaba', 300, 1e12, 1e10)
        self.assertEqual(round(planet_object.get_volume(), 2), 113097335.53)

    def test_get_surface_area(self):
        """Checks whether or not surface area for planet is correct"""
        planet_object = planet.Planet('Elphaba', 200, 1e12, 1e10)
        self.assertEqual(round(planet_object.get_surface_area(), 2), 502654.82)
    
    def test_get_density(self):
        """Checks if density for planet is correct"""
        planet_object = planet.Planet('Elphaba', 300, 1e12, 1e10)
        self.assertEqual(round(planet_object.get_density(), 2), 8841.94)

    def test_get_name(self):
        """Checks if name is correct for planet"""
        planet_object = planet.Planet('Elphaba', 300, 1e12, 1e10)
        self.assertEqual(planet_object.get_name(), 'Elphaba')

    def test_get_radius(self):
        """Checks if radius is correct for planet"""
        planet_object = planet.Planet('Elphaba', 300, 1e12, 1e10)
        self.assertEqual(planet_object.get_radius(), 300)

    def test_get_mass(self):
        """Checks if mass is correct for planet"""
        planet_object = planet.Planet('Elphaba', 300, 1e12, 1e10)
        self.assertEqual(planet_object.get_mass(), 1e12)

    def test_get_distance(self):
        """Checks if distance is correct for planet"""
        planet_object = planet.Planet('Elphaba', 300, 1e12, 1e10)
        self.assertEqual(planet_object.get_distance(), 1e10)

    def test_set_name(self):
        """Checks if method can set name for planet"""
        planet_object = planet.Planet('Elphaba', 300, 1e12, 1e10)
        self.assertEqual(planet_object.set_name('Wicked Witch of the West'), 'Wicked Witch of the West')
    
if __name__ == '__main__':
    unittest.main()