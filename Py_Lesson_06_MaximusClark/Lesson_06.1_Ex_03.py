word = input("Please enter the word you would like to use: ")
def printf():
    for i in range(len(word), -1, -1):
        print(word[i:])
printf()

