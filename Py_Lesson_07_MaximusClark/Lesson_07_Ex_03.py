number = int(input("Please enter a number: "))
num = number
rev = 0
def Reverse(n):
    while num > 0:
        rev = rev*10
        rev += 1
        num = int(num / 10)
        print("The number", number, "is being reversed: ", rev) 
Reverse(number) 
