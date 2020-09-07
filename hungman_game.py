import random
from collections import Counter

items = {
    'fruits': 'apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya '
              'berry peach lychee muskmelon',
    'animals': 'tiger lion camel horse cat dog peacock duck hen rabbit',
    'vegetable': 'carrot tomato beans potato onion brinjal beetroot',
}

title = random.choice(['fruits', 'animals', 'vegetable'])
word = random.choice(items[title].split(' '))

if __name__ == '__main__':
    print('Guess the word! Hint it is a {}'.format(title))
    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter: '))
            except:
                print('Print only the letter')
                continue

            # Validate the guessed Letter
            if not guess.isalpha():
                print('Enter only letters')
                continue
            elif len(guess) > 1:
                print('Enter only one letter')
                continue
            elif guess in letterGuessed:
                print('Letter already guessed')

            # If the letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            # Printing the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                # If user guessed all the letter
                elif (Counter(letterGuessed) == Counter(word)):
                    flag = 1
                    print('The word is: ', word)
                    print('Congratulation you have won')
                    break
                    break
                else:
                    print('_', end=' ')

        # If all the chances are completed
        if chances < 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You have lost')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye!')
        exit()
