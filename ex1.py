import random
comp = random.randint(0,9)
num = 10
while num:
    user = input('Enter number: ')
    if comp < int(user):
        print('<')
    elif comp > int(user):
        print('>')
    else:
        print('you win')
        break
    num -= 1
