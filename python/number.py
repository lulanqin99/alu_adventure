import random

secret_number = random.randint(1,100)
guess_num = 1

#while guess_num != secret_number:
for guess_num in range (5):

    guess = raw_input("Guess the secret number : ")
    guess_num = int(guess)
    if guess_num == secret_number:
        print "Yes"
    elif guess_num < secret_number:
        print "Too low"
    elif guess_num + 1 == secret_number or guess_num -1 == secret_number:
        print "Close"
    elif guess_num > secret_number:
        print "Too high"
