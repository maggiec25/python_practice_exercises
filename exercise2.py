import random



random_num = random.randint(0, 100)

guesses = 0
Count = 0
while True:
    guess = int(input("guess a number \n"))
    if guess < random_num:
        print("the number you want is higher")
        Count = int(Count) + 1
    elif guess > random_num:
        print("the number you want is lower")
        Count = int(Count) + 1
    else:
        print("congrats! you guessed it")
        print("Your total number of guesses are " + str(Count))
        break