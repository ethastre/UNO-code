import random

print("Welcome to Uno")
Colors = ['Red', 'Green', 'Blue', 'Yellow']
Deck = []
Hand1 = []
Hand2 = []
Discard = []
for i in range(0,108):
   Deck.append ([random.choice(Colors), random.randint(0,9)])
for i in range(0,7):
    Hand1.append(random.choice(Deck))
for i in range(0,7):
    Hand2.append(random.choice(Deck))
Discard.append(random.choice(Deck))

print("The Top Of Discard is"+)