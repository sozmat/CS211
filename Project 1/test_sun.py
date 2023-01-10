import unittest
import sun

class T0_Sun_test_methods(unittest.TestCase):
    """ Tests the methods of the Sun class"""

    def test_get_mass(self):
        """Checks if mass is correct for sun"""
        sun_object = sun.Sun('Glinda', 33.00, 5.24, 26678987.00)
        self.assertEqual(sun_object.get_mass(), 33.00)

    def test_get_radius(self):
        """Checks if radius is correct for sun"""
        sun_object = sun.Sun('Glinda', 33.00, 5.24, 26678987.00)
        self.assertEqual(sun_object.get_radius(), 5.24)

    def test_get_temperature(self):
        """Checks if temperature is correct for sun"""
        sun_object = sun.Sun('Glinda', 33.00, 5.24, 26678987.00)
        self.assertEqual(sun_object.get_temperature(), 26678987.00)


if __name__ == '__main__':
    unittest.main()