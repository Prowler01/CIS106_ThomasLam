def calculateArea(width, length):
    areaFeet = width * length
    
    return areaFeet

def calculateSquareYards(area):
    areaYards = area / 9
    
    return areaYards

def displayResult(area, areaYards):
    print("Total area in square feet: " + str(area))
    print("Total area in square yards: " + str(areaYards))

def getLength():
    print("Length (in feet): ")
    length = float(input())
    
    return length

def getWidth():
    print("Width (in feet): ")
    width = float(input())
    
    return width

# Main
# This program prompts the user for width and length of a room. It then uses these 2 variables to calculate surface area.
# References: Textbook
width = getWidth()
length = getLength()
area = calculateArea(width, length)
areaYards = calculateSquareYards(area)
displayResult(area, areaYards)
