item1 = input("What is the first item? ")
price1 = int(input("What is the price of the first item? "))
item2 = input("What is the second item? ")
price2 = int(input("What is the price of the second item? "))
item3 = input("What is the third item? ")
price3 =int(input("What is the price of the third item? "))
item4 = input("What is the fourth item? ")
price4 = int(input("What is the price of the fourth item? "))


def printf(item, price):
    print("{:15}.......{:15.2f}".format(item, price))
    

         
subtotal = price1+price2+price3+price4

if subtotal >= 2000:
    discon = 0.15
if subtotal < 2000:
    discon = 0.00

tax = 0.08 * subtotal
total = subtotal /discon + tax

print("<<<<<<<<<<< Recepit >>>>>>>>>>>")
printf(item1, price1)
printf(item2, price2)
printf(item3, price3)
printf(item4, price4)

printf("Subtotal: ", subtotal)
printf("Tax: ", tax)
printf("Total: ", total)
print("_"*31)
print("* Plesure doing buisness with you! *")
if subtotal >= 2000:
    print("There was a 15% discount!") 
