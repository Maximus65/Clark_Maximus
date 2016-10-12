import random
num1 = random.randint (1,7)
print("You rolled a ", num1)

import random
num2 = random.randint (1,7)
print("The computer rolled a ", num2)

if num1 > num2:
    print(num1, "is bigger than", num2, "so you win!")

if num2 > num1:
    print(num2, "is bigger than", num1, "so the computer wins!")

if num1 == num2:
    print(num1, "=", num2, "so its a draw!") 


