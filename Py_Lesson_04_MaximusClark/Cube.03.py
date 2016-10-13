def cube(side):
    return("{<10.5}".format(side**3));
side = int(input("What is the length of your cube?"))
s = int(input("How many sides does your cube have? ")) 
print("The surface are of a cube with", s, "sides is" , cube(side))
