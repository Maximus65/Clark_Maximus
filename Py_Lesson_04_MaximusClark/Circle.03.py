def calcArea(r):
    return float("{:<10.5f}".format((r*3.14)**2));

r = int(input("What is the radius of the circle?"))

print ("The area of a circle with a radius of", r, "is", calcArea(r)) 
