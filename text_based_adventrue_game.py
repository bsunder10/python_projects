name = input('Hello, Enter your Name: ')
print('Hello', name)

while True:
    answer = input('Do you want to play: yes/no  ')
    if answer.lower() == 'yes':
        print("You find yourself on the edge of a dark forest.")
        print("Can you find your way through?\n")
        answer = input("Would you like to step into the forest?\nyes/no\n")
        if answer.lower() == 'yes':
            print("You head into the forest. You hear crows cawing in the distance.\n")
            print("To your left, you see a bear.")
            print("To your right, there is more forest.")
            print("There is a rock wall directly in front of you.")
            print("Behind you is the forest exit.\n")
            answer = input("What direction do you move?\nleft/right/forward/backward\n")
            if answer.lower() == 'forward':
                print('You cannot pass or jump over the wall')
                print('The bear attacked you')
                print('You lost')
                break
            if answer.lower() == 'backward':
                print('You took a back step')
                print('You lost')
                break
            if answer.lower() == 'left':
                print('The bear ate you')
                print('You lost')
                break
            if answer.lower() == 'right':
                print('You headed deep into the forest')
                print('Now you can see a light on your right')
                print('Some animals sound on your left shouting')
                print('More forest infront of you')
                answer = input('What direction do you move?\nleft/right/forward/backward\n')
                if answer.lower() == 'forward':
                    print('You headed deeper in the forest and lost inside it')
                    print('You lost')
                    break
                if answer.lower() == 'backward':
                    print('The bear ate you on your way back')
                    print('You lost')
                    break
                if answer.lower() == 'right':
                    print('The light was from the tribes in the forest')
                    print('They killed you')
                    print('you lost')
                    break
                if answer.lower() == 'left':
                    print('The sound was of a dog. You headed towards the a forest office.')
                    print('They saved you')
                    print('You reached home safely')
                    break
                else:
                    print('I could not undestand')
            else:
                print('could not undestand')
        if answer.lower() == 'no':
            print("You are not ready for this quest. Goodbye, " + name + ".")
            break
        else:
            print('could not undestand')
    else:
        print('Good Bye!')