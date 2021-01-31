# Program to calculate the area and volume of various shapes with pre-specified mesurements

Length = 192006.12
# calculate area of a square with a side of the value "length"
print('Area of Square:', Length**2)
# calculate volume of a cube with a side of the value "length"
print('Volume of Cube:', Length**3)
pi = 3.1415927
# calculate area of a circle with a diameter of the value "length"
print('Area of Circle:', pi*(Length/2)**2)
# calculate volume of a sphere with a diameter of the value "length"
print('Volume of Sphere:', 4/3*pi*(Length/2)**3)
# calculate volume of a cylinder with a diameter of the value "length" and a height of the value "length"
print('Volume of Cylinder:', pi*Length*(Length/2)**2)
