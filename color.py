#!/usr/bin/env python
""" Color Management """

def hex_to_float(hex):
    """ Convert hex color string to float color array """
    if (not hex.startswith("#")):
        print ("Wrong formated hex {0}".format(hex))
        return (0)

    r = int(hex[1:3], 16) / 255
    g = int(hex[3:5], 16) / 255
    b = int(hex[5:7], 16) / 255
    return ([r, g, b])
