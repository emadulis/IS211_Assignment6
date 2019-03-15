#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A refactoring module."""


import unittest

class ConversionNotPossible(Exception):
    pass

distance = {'met': {'yar':(0,1.09361,0),
                    'mil':(0,0.000621371,0)},
            'yar': {'mil':(0,0.000568182,0),
                    'met':(0,0.9144,0)},
            'mil': {'met':(0,1609.34,0),
                    'yar':(0,1760,0)}
            }
temp = {'kel':{'cel':(0,1,-273.15),
               'fah':(-273.15,9/5,32)},
        'cel':{'kel':(0,1,273.15),
               'fah':(0,9/5,32)},
        'fah':{'kel':(-32,5.0/9.0,273.15),
               'cel':(-32,5.0/9.0,0)}
        }

def convert(from_unit, to_unit, value):
    """A function for convert."""
    from_unit = from_unit[0:3]
    to_unit = to_unit[0:3]
    if not ((from_unit in distance and to_unit in distance
             ) or (from_unit in temp and to_unit in temp)):
        raise ConversionNotPossible
    else:
        if from_unit == to_unit:
            ret_val = value
        elif from_unit in distance:
            ret_val = (
                (value + distance[from_unit][to_unit][0])
                * distance[from_unit][to_unit][1]
                + distance[from_unit][to_unit][2]
                )
        else:
            ret_val = (
                (value + temp[from_unit][to_unit][0])
                * temp[from_unit][to_unit][1]
                + temp[from_unit][to_unit][2])

    return float("%0.2f" %ret_val)


class ConvertTests(unittest.TestCase):

    def testTemperature(self):
        self.assertEqual(convert('celsius','fahrenheit',0),32.0)
        self.assertEqual(convert('celsius','kelvin',0),273.15)
        self.assertEqual(convert('kelvin','fahrenheit',0),-241.15)
        self.assertEqual(convert('kelvin','celcius',273.15),0.0)
        self.assertEqual(convert('fahrenheit','celcius',32),0.0)
        self.assertEqual(convert('fahrenheit','kelvin',0),255.37)

    def testDistance(self):
        self.assertEqual(convert('meter','mile',100),0.06)
        self.assertEqual(convert('meter','yard',10),10.94)
        self.assertEqual(convert('mile','meter',10),16093.4)
        self.assertEqual(convert('mile','yard',10),17600.00)
        self.assertEqual(convert('yard','meter',3),2.74)
        self.assertEqual(convert('yard','mile',300),0.17)

    def testSanity(self):
        for test in distance:
            self.assertEqual(convert(test, test, 10), 10)
        for test in temp:
            self.assertEqual(convert(test, test, 10), 10)

    def testErrors(self):
        self.assertRaises(ConversionNotPossible,convert,'met','cel',0)

if __name__ == '__main__':
    unittest.main()
