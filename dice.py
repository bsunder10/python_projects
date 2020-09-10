from random import randint

while True:
    answer = input('Do you want me to spin (y/n): ')
    if answer.lower() == 'y':
        print('Your number is: {}'.format(randint(1, 6)))
    else:
        break
