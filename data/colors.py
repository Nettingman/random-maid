"""
Container for the colors.
"""
from random import randint
colorDict = {11: 'Red', 12: 'Purple', 21: 'Purple', 13: 'Orange', 31: 'Orange', 14: 'Pink', 41: 'Pink', 15: 'Brown', 51: 'Brown', 16: 'Vermillion', 61: 'Vermillion', 
   22: 'Blue', 23: 'Green', 32: 'Green', 24: 'Sky blue', 42: 'Sky blue', 25: 'Navy', 52: 'Navy', 26: 'Indigo', 62: 'Indigo', 
   33: 'Yellow', 34: 'Cream', 43: 'Cream', 35: 'Beige', 53: 'Beige', 36: 'Gold', 63: 'Gold', 44: 'White', 45: 'Gray', 
   54: 'Gray', 46: 'Silver', 64: 'Silver', 55: 'Black', 56: 'Metallic', 65: 'Metallic', 66: 'Transparent/Rainbow'}

def getColor():
    x = randint(1, 6)
    y = randint(1, 6)
    xy = int(str(x) + str(y))
    return colorDict[xy]
