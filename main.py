#!/usr/bin/env python

import argparse
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from colormath.color_objects import LabColor, sRGBColor


parser = argparse.ArgumentParser(description='Find the visually closest color from a set of colors')
parser.add_argument('colors_file', type=argparse.FileType('r'),
                    help='path to file containing hex colors separated by newline')
parser.add_argument('color', type=str,
                    help='target color in hex format')
args = parser.parse_args()

hex_color = sRGBColor.new_from_rgb_hex(args.color)
target_color = convert_color(hex_color, LabColor)

colors = []
for line in args.colors_file.readlines():
    hex_color = sRGBColor.new_from_rgb_hex(line.rstrip())
    colors.append(convert_color(hex_color, LabColor))

deltas = list(map(lambda x: delta_e_cie2000(target_color, x), colors))
min_delta_index = deltas.index(min(deltas))

closest_rgb_color = convert_color(colors[min_delta_index], sRGBColor)
print(closest_rgb_color.get_rgb_hex())
