#python program to shuffle a deck of card

import itertools, random

#make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

#shuffle the card
random.shuffle(deck)

#draw five cards
print('you got:')
for i in range(5):
    print(deck[i][0], 'of', deck[i][1])