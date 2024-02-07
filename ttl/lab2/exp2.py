import random
import math

lo = int(input("Enter Lower bound: "))

hi = int(input("Enter Upper bound: "))

x = random.randint(lo, hi)
print("\nYou've only ", round(math.log(hi - lo + 1, 2)), " chances to guess the integer!\n")

cnt = 0

while cnt < math.log(hi - lo + 1, 2):
    cnt += 1

    guess = int(input("Guess a number: "))
    
    if x == guess:
        if cnt == 1:
            print("Congratulations, you did it in 1 try")
        else:
            print("Congratulations, you did it in ", cnt, " tries!")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

if cnt >= math.log(hi - lo + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
