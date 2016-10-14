answer1 = int(input("Good evening, are ready to be put in a story (1 = yes 2 = no)? "))
if answer1 == 1:
        answer2 = int(input("Well here we go, you are trick or treating, and you come across a black house and a white house, which house do you go to? The balck house = 1 and white house = 2 "))
        if answer2 == 1:
               answer3 = int(input("You knock on the door and the door slowly opens, but no one is there! You see a light switch, do you try it or no? 1 = yes 2 = no "))
               if answer3 == 1:
                      answer4 = int(input("The light switch doesn't work, you search the house for the owner, you finally find an evil scientist he asks you, how would you like to die, by suffacation, or electric chair? 1 = suffacation 2 = electric chair"))
                      if answer4 == 1:
                              print("He kills you and you die!!!!!!!")
                      if answer4 == 2:
                              print(" The electric chair doesn't work (because the power is out) and he lets you go")
               if answer3 == 2:
                       answer4 = int(input("You search the house for the owner, you finally find an evil scientist he asks you, how would you like to die, by suffacation, or electric chair? 1 = suffacation 2 = electric chair"))
                       if answer4 == 1:
                              print("He kills you and you die!!!!!!!")
                       if answer4 == 2:
                              print(" The electric chair doesn't work (because the power is out, which you would've known if you tried the light switch) and he lets you go")
        if answer2 == 2:
                answer3 = int(input("You knock on the door and a woamen answers, she says, hi there little one, here is your candy. it looks suspecius, do you eat it or no? 1 = yes 2 =no"))
                if answer3 == 1:
                        print("The candy was poisined and she finds your body and puts it with here collection of other victoms!")
                if  answer3 == 2:
                        print("You made a good desion, the candy was poisioned and you go home and eat your trick or treat candy!")
                
else:
        print("Well your no fun")
print("THANKS FOR PLAYING!") 
