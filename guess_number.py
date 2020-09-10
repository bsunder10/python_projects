from random import randint

name = input('Hi, Please enter your name: ')
print('Hello, ', name)

played = 0
won = 0

while True:
    chances = 5
    print('I am thinking a number between 1-50')
    print('you have got 5 chances to guess')
    print('Good Luck')
    number = randint(1, 26)
    played += 1
    while True:
        print()
        chances -= 1
        guess = int(input('Take a guess: '))
        if guess > number:
            print('The guess is too high')
        if guess < number:
            print('The guess is too low')
        if guess == number:
            print('Congratulations you guessed it right')
            won += 1
            break
        elif guess != number and chances <= 0:
            print('There are no chances left')
            print('The number I taught was', number)
            break
        print('You have {} chances left'.format(chances))
    play = input('Do you want to play again yes/no: ')
    if play == 'no':
        print('Good Bye!')
        if played == won:
            print('We played {} times and you won all the games'.format(played))
        elif won == 0:
            print('We played {} times and you lost all the games'.format(played))
        else:
            print('We played {} times and you won {}'.format(played, won))
        break
