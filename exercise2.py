import random



# program that generates random number and has user guess what it is
random_num = random.randint(0, 100)
# upate program to keep trak of how many guesses user made

guesses = 0
while True:
    guess = int(input("guess a number \n"))
    if guess < random_num:
        print("the number you want is higher")
    elif guess > random_num:
        print("the number you want is lower")
    else:
        print("congrats! you guessed it")
        break