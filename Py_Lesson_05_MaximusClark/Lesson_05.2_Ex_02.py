Username = "clarkm7287"
Password = "password"
user = input("Please enter your Username: ")
pas = input("Please enter your Password: ")

            
if(user == Username and pas == Password):
    print("access granted!")

else:
    if(user != Username and pas == Password):
        print("Yor username is incorrect!")
else:
    if(user == Username and pas != Password):
        print("Your password is incorrect!")
else:
    if(user != Username and pas != Password):
        print("Your username and password is incorrect!") 
