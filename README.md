azimuth.py
==========

Given a string representation of two geographical coordinates (longitude and latitude), this script can find the arc-distance between the coordinates and/or the Manhattan arc-distance between them (that is, traveling due east/west and then due north/south). 

This is useful if you have a Minecraft map (or similar) which is a scale replica of a real world area and you need to locate some new place given a known reference point. Finding the Manhattan distance from A to B and scaling appropriately (like 1 meter = 1 block) can give you the exact X & Z coordinates of your B location in Minecraft.
