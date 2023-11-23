#Enter a radius: 3.5
#Area of a circle with radius 3.50 is 38.48.
#Circumference of a circle with radius 3.50 is 21.99.
#Volume of sphere with radius 3.50 is 179.59.

import math

r = float(input('Enter a radius: '))

def area(r):
    area = math.pi*r*r
    return area

def circumference(r):
    circumference = 2*math.pi*r
    return circumference

def volume(r):
    volume = (4/3)*math.pi*r*r*r
    return volume

print('Area of a circle with radius',r,'is %.2f'%area(r))
print('Circumference of a circle with radius',r,'is %.2f'%circumference(r))
print('Volume of sphere with radius',r,'is %.2f'%volume(r))