secret =22

for i in range(5):
    guess = int(raw_input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print "You guessed it - congratulations! It's number %s :)" %secret
        break
    elif guess > secret:
        print "Your guess is greater than secret number"
    elif guess < secret:
        print "your guess is lower than secret nuber."
    else:
        print "Sorry, your guess is not correct... Secret number is not " + str(guess)

    if not guess:
        print "I will slep for 15s"
        for j in range(15):
            print "Try again in: %s" %str(15-j)
            time.sleep(1)