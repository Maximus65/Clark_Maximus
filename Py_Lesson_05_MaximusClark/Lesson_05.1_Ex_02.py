def calcBMI(out):
    if out < 18.5:
        print("You are underweight")
    elif out <= 24.9:
        print("You are Normal!")
    elif out <= 29.9:
        print("You are Overweight")
    elif out <= 34.9:
        print("You are Obese")
    elif out <= 39.9:
        print("You are Very Obese!")
    if out >= 40:
        print("You are Extremly Obeses!!!!!!!!") 


Hgth = int(input("What is your Heigth, in inches please? "))
Wght = int(input("What is your Weigth, in pounds please? "))
outcome = (Wght / (Hgth**2)) * 703
print("Your BMI is",outcome,"wich means...");calcBMI(outcome);
