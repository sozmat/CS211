import unittest
import solarsystem

class T0_SolarSystem_test_methods(unittest.TestCase):
    """Test the methods of the SolarSystem class"""

    def test_add_planet(self):
        """Checks if SolarSystem class can add planet"""
        solarsystem_object = solarsystem.SolarSystem('Burning Ball of Gas')
        self.assertEqual(solarsystem_object.add_planet('Elphaba'), None)

    def test_show_planets(self):
        """Checks if SolarSystem can show planets accurately"""
        solarsystem_object = solarsystem.SolarSystem('Burning Ball of Gas')
        self.assertEqual(solarsystem_object.show_planets('name'), None)



if __name__ == '__main__':
    unittest.main()
    

    