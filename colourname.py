#!/usr/bin/env python
# Gives you the closest Wikipedia colour of a colour hex
import json, sys

i = raw_input("Colour: ").upper()
if len(i) == 6:
    i = "#"+i
if len(i) != 7:
    sys.exit("Invalid input.")

best = (1000, "")

r = int(i[1:3], 16)
g = int(i[3:5], 16)
b = int(i[5:7], 16)

with open("colours") as f:
    colours = json.loads(f.read())

for colour in colours.keys():
    if colour == i:
        best = (0, colour)
        break
    rr = int(colour[1:3], 16)
    gg = int(colour[3:5], 16)
    bb = int(colour[5:7], 16)
    diff = abs(rr - r) + abs(gg - g) + abs(bb - b)
    if diff < best[0]:
        best = (diff, colour)

print "Colour:", best[1]
print "Colour name:", colours[best[1]][0]
print "URL: https://en.wikipedia.org" + colours[best[1]][1]
print "Difference:", best[0]
