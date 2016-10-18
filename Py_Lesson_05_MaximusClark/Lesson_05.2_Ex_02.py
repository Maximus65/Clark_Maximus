Username = "clarkm7287"
Password = "password"
user = input("Please enter your Username: ")
pas = input("Please enter your Password: ")

            
if(user == Username and pas == Password):
    print("access granted!")

if(user != Username and pas == Password):
    print("Yor username is incorrect!")

if(user == Username and pas != Password):
    print("Your password is incorrect!")
    
if(user != Username and pas != Password):
    print("Your username and password is incorrect!") 

