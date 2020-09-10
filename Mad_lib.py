def enter(pos):
    return input('Enter any {}: '.format(pos))

def tell_your_love():
    one = enter('season')
    two = enter('verb')
    three = enter('adjective')
    four = enter('verb')
    five = enter('noun')
    six = enter('verb')
    seven = enter('verb')
    eight = enter('noun')
    nine = enter('body part')
    ten = enter('Time span')

    print('Your story is ')
    print('When you are in love, everyday feels like {}'.format(one))
    print('The sun is always {}, the air feels {}, and the birds are always {}. '
          'You see the world through rose-colored {}.'.format(two, three, four, five))
    print('When you see the person you see your heart {}. You cannot {} because they take your'
          ' {} away.'.format(six, seven, eight))
    print('The person you love is always on your {} and you cannot imagine a {} without them'.format(nine, ten))

tell_your_love()
