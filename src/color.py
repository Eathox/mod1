#!/usr/bin/env python
""" Color Management """

def hex_to_float(hex, alpha=False):
    """ Convert hex color string to float color array """
    if (not hex.startswith("#")):
        print ("Wrong formated hex {0}".format(hex))
        return (0)

    color = []
    color.append(int(hex[1:3], 16) / 255) # R
    color.append(int(hex[3:5], 16) / 255) # G
    color.append(int(hex[5:7], 16) / 255) # B
    if (alpha):
        if (len(hex) < 9):
            color.append(255)
        else:
            color.append(int(hex[7:9], 16) / 255)
    return (color)
