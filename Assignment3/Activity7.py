# This program prompts the user for the name and age of their dog. The program then calculates and displays dog's age in dog years.
# References: Professor Braunsweig
print("What's your dog's name? ")
dogname = input()
print("How old is your dog in human years? ")
humanyears = int(input())
dogyears = humanyears * 7
print(dogname + " is " + str(dogyears) + " in dog years.")
