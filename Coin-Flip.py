import random

# random number of 1 or 2 to represent heads or tails
number= random.randint(1,2)

coin = number

flipCoin=True

# Loops the coin flip
while flipCoin == True:

    if number == 1:
        print('It\s heads!')
    else :
        print('It\'s tails!')

    # asks the user if they would like to flip again 
    flipAgain= input('Flip again?')
    if flipAgain == 'y' or flipAgain =='yes':
        flipCoin = True

    # Ends the coin flip for the user
    elif flipAgain == 'n' or flipAgain =='no':
        flipCoin = False
        break
print('Thanks for flipping')
