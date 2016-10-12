

def calcPoints(grad):
    if grad == "A":
        return 4.0
    if grad == "B":
        return 3.0
    if grad == "C":
        return 2.0
    if grad == "D":
        return 1.0
    if grad == "F":
        return 0.0

Grade1 = input("What is your first letter grade? ")
Grade2 = input("What is your second letter grade? ")
Grade3 = input("What is your third letter grade? ")
Grade4 = input("What is your fourth letter grade? ")
Grade5 = input("What is your fith letter grade? ")
Grade6 = input("What is your sixth letter grade? ")
Grade7 = input("What is your seventh letter grade? ")


gPoints = (calcPoints(Grade1) + calcPoints(Grade2) + calcPoints(Grade3) + calcPoints(Grade4) + calcPoints(Grade5) + calcPoints(Grade6) + calcPoints(Grade7))
GPA = gPoints/7
print("Your GPA is", GPA) 
