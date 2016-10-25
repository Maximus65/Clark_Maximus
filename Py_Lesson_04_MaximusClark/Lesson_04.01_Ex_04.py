R = int(input ("What is the intrest rate on the bank account? "))
p = int(input("What is the pricible of the bank account?"))
n = int(input ("What is the number of times the loan is compounded per year? "))
t = int(input ("How long have you had the loan in year? "))
A = p * (1 + R/n)**n*t
print ("Your monthly payment amount on the loan is",A)
