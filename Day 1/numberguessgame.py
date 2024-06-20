import random

while True :
    initialValue = int(input('Enter starting range :'))
    finalValue = int(input('Enter final range : '))
    number = random.randint(initialValue,finalValue)
    trials = 0
    while True :
        guess = int(input('Enter guess number : '))
        trials += 1
        if guess == number :
            break
        elif guess > number :
            print('Try lower number !')
        elif guess < number :
            print('Try higher number !')
    print(f'You guessed it correct in { trials } trials.')
    guess = input('Do you want to play again (y/n) : ')
    if guess == 'n' :
        break
print('Thank you !')