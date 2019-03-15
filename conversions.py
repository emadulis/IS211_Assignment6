#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is module for temperature conversions."""


def convertCelsiusToKelvin(temp):
    """conversion of Celsius to Kelvin
    
    Args:
        conversion(float): Celcius to Kelvin conversion.
    Returns:
        conversion(float): Returns Kelvin result.
    Example:
        >>> convertCelsiusToKelvin(300)
        573.15
    """
    total = temp + 273.15
    return float("%.3f" % total)
    

def convertCelsiusToFahrenheit(temp):
    """conversion of Celsius to Kelvin
    
    Args:
        conversion(float): Celcius to Kelvin conversion.
    Returns:
        conversion(float): Returns Kelvin result.
    Example:
        >>> convertCelsiusToFarenheit(300)
        572.0
    """
    total = (1.8 * temp) + 32
    return float("%.3f" % total)


def convertFahrenheitToKelvin(temp):
    """conversion of Celsius to Kelvin
    
    Args:
        conversion(float): Celcius to Kelvin conversion.
    Returns:
        conversion(float): Returns Kelvin result.
    Example:
        >>> convertFahrenheitToKelvin(300)
        422.039
    """
    total = ((temp - 32) / 1.8) + 273.15
    return float("%.3f" % total)


def convertFahrenheitToCelsius(temp):
    """conversion of Celsius to Kelvin
    
    Args:
        conversion(float): Celcius to Kelvin conversion.
    Returns:
        conversion(float): Returns Kelvin result.
    Example:
        >>> convertFahrenheitToCelsius(300)
    148.889
    """
    total = (temp - 32) / 1.8
    return float("%.3f" % total)


def convertKelvinToCelsius(temp):
    """conversion of Celsius to Kelvin
    
    Args:
        conversion(float): Celcius to Kelvin conversion.
    Returns:
        conversion(float): Returns Kelvin result.
    Example:
        >>> convertKelvinToCelsius(300)
    26.85
    """
    total = temp - 273.15
    return float("%.3f" % total)
    

def convertKelvinToFahrenheit(temp):
    """conversion of Celsius to Kelvin
    
    Args:
        conversion(float): Celcius to Kelvin conversion.
    Returns:
        conversion(float): Returns Kelvin result.
    Example:
        >>> convertKelvinToFahrenheit(300)
    80.33
    """
    total = (temp - 273.15) * 1.8 + 32
    return float("%.3f" % total)
