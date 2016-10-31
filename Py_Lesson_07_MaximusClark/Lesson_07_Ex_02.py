number = int(input("Please enter a number: "))
digits = 0
average = 0
while number > 0:
    digits += 1
    digits = (int(digits % 10)) + average 
    number = int(number / 10)
    print(digits) 
