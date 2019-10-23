#!/usr/bin/env python
""" Color Management """

class Color:
    """ Color class """
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 255

def _pair_to_float(pair):
    """ Convert pair to a hex pair """
    num = int(pair, 16)
    return (num / 255)

def hex_to_float(hex):
    """ Convert hex color string to float color array """
    if (not hex.startswith("#")):
        print ("Wrong formated hex {0}".format(hex))
        return

    color = Color()
    color.r = _pair_to_float(hex[1:3])
    color.g = _pair_to_float(hex[3:5])
    color.b = _pair_to_float(hex[5:7])
    if (len(hex) >= 9):
        color.a = _pair_to_float(hex[7:9])
    return (color)
