#! usr/bin/env python
# *-* coding: utf-8 *-*
"""A testing module."""


import conversions 
import unittest 


class CelsiusToKelvin(unittest.TestCase):


    def test_pos(self): 
        "Test for positive input."
        results = conversions.convertCelsiusToKelvin(300)
        self.assertEqual(573.15, results)
        

    def test_neg(self):
        "Test for negative input."
        results = conversions.convertCelsiusToKelvin(-300)
        self.assertEqual(-26.85, results)
        

    def test_zero(self):
        "Test for zero input."
        results = conversions.convertCelsiusToKelvin(0)
        self.assertEqual(273.15, results)
        

    def test_non_whole_num(self): 
        "Test for non-whole input."
        results = conversions.convertCelsiusToKelvin(1.05)
        self.assertEqual(274.2, results)
        

    def test_large(self):
        "Test for large input."
        results = conversions.convertCelsiusToKelvin(567890)
        self.assertEqual(568163.15, results)
        
    
class CelsiusToFahrenheit(unittest.TestCase):


    def test_pos(self):
        "Test for positive input."
        results = conversions.convertCelsiusToFahrenheit(300)
        self.assertEqual(572.0, results)
        

    def test_neg(self):
        "Test for negative input."
        results = conversions.convertCelsiusToFahrenheit(-300)
        self.assertEqual(-508.0, results)
        

    def test_zero(self):
        "Test for zero input."
        results = conversions.convertCelsiusToFahrenheit(0)
        self.assertEqual(32.0, results)
        

    def test_non_whole_num(self):
        "Test for non-whole input."
        results = conversions.convertCelsiusToFahrenheit(1.005)
        self.assertEquals(33.809, results)
        

    def test_large(self):
        "Test for large input."
        results = conversions.convertCelsiusToFahrenheit(567890)
        self.assertEqual(1022234.0, results)

class FharenheitToKelvin(unittest.TestCase):


    def test_pos(self):
        "Test for positive input."
        results = conversions.convertFahrenheitToKelvin(300)
        self.assertEqual(422.039, results)
        

    def test_neg(self):
        "Test for negative input."
        results = conversions.convertFahrenheitToKelvin(-300)
        self.assertEqual(88.706, results)
        

    def test_zero(self):
        "Test for zero input."
        results = conversions.convertFahrenheitToKelvin(0)
        self.assertEqual(255.372, results)
        

    def test_non_whole_num(self):
        "Test for non-whole input."
        results = conversions.convertFahrenheitToKelvin(1.005)
        self.assertEquals(255.931, results)
        

    def test_large(self):
        "Test for large input."
        results = conversions.convertFahrenheitToKelvin(567890)
        self.assertEqual(315749.817, results)

class FahrenheitToCelsius(unittest.TestCase): 

    def test_pos(self):
        "Test for positive input."
        results = conversions.convertFahrenheitToCelsius(300)
        self.assertEqual(148.889, results)
        

    def test_neg(self):
        "Test for negative input."
        results = conversions.convertFahrenheitToCelsius(-300)
        self.assertEqual(-184.444, results)
        

    def test_zero(self):
        "Test for zero input."
        results = conversions.convertFahrenheitToCelsius(0)
        self.assertEqual(-17.778, results)
        

    def test_non_whole_num(self):
        "Test for non-whole input."
        results = conversions.convertFahrenheitToCelsius(1.005)
        self.assertEquals(-17.219, results)
        

    def test_large(self):
        "Test for large input."
        results = conversions.convertFahrenheitToCelsius(567890)
        self.assertEqual(315476.667, results)
        
class KelvinToCelsius(unittest.TestCase):

    def test_pos(self):
        "Test for positive input."
        results = conversions.convertKelvinToCelsius(300)
        self.assertEqual(26.85, results)
        

    def test_neg(self):
        "Test for negative input."
        results = conversions.convertKelvinToCelsius(-300)
        self.assertEqual(-573.15, results)
        

    def test_zero(self):
        "Test for zero input."
        results = conversions.convertKelvinToCelsius(0)
        self.assertEqual(-273.15, results)
        

    def test_non_whole_num(self):
        "Test for non-whole input."
        results = conversions.convertKelvinToCelsius(1.005)
        self.assertEquals(-272.145, results)
        

    def test_large(self):
        "Test for large input."
        results = conversions.convertKelvinToCelsius(567890)
        self.assertEqual(567616.85, results)
        
class KelvinToFahrenheit(unittest.TestCase):
    

    def test_pos(self):
        "Test for positive input."
        results = conversions.convertKelvinToFahrenheit(300)
        self.assertEqual(80.33, results)
        

    def test_neg(self):
        "Test for negative input."
        results = conversions.convertKelvinToFahrenheit(-300)
        self.assertEqual(-999.67, results)
        

    def test_zero(self):
        "Test for zero input."
        results = conversions.convertKelvinToFahrenheit(0)
        self.assertEqual(-459.67, results)
        

    def test_non_whole_num(self):
        "Test for non-whole input."
        results = conversions.convertKelvinToFahrenheit(1.005)
        self.assertEquals(-457.861, results)
        

    def test_large(self):
        "Test for large input."
        results = conversions.convertKelvinToFahrenheit(567890)
        self.assertEqual(1021742.33, results)




    
if __name__ == "__main__":
    unittest.main()
