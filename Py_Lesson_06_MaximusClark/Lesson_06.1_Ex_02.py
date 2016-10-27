word = input("Please enter the word you would like to use: ")
def printf():
    for m in range(len(word), 0,-1):
        print(word[0:m])
printf()
