import random

print("Welcome to Uno")
Colors = ['Red', 'Green', 'Blue', 'Yellow']
Deck = []
Hand1 = []
Hand2 = []
Discard = []

def turn1():
    print("The Top Of Discard is", Discard[-1])
    print("Player 1 your hand is", Hand1)
    print("Type the position of the card starting at zero, if none match type 'none'")
    Position = int(input())
    if Hand1[Position][0] != Discard[0][0] and Hand1[Position][1] != Discard[0][1]:
        Hand1.append(Deck.pop())
    if Hand1[Position][0] == Discard[0][0] or Hand1[Position][1] == Discard[0][1]:
        Discard.append(Hand1.pop(Position))
    print('Your hand is now', Hand1)

def turn2():
    print("The Top Of Discard is", Discard[-1])
    print("Player 2 your hand is", Hand2)
    print("Type the position of the card starting at zero, if none match type 'none'")
    position =int(input())
    if Hand2[position][0] != Discard[0][0] and Hand2[position][1] != Discard[0][1]:
        Hand2.append(Deck.pop())
    if Hand2[position][0] == Discard[0][0] or Hand2[position][1] == Discard[0][1]:
        Discard.append(Hand2.pop(position))
    print('Your hand is now', Hand2)

for h in range(0,2):
    for color in Colors:
        for i in range(0,10):
            Deck.append([color, str(i)])
random.shuffle(Deck)
for i in range(0,7):
    Hand1.append(Deck.pop())
for i in range(0,7):
    Hand2.append(Deck.pop())
Discard.append(Deck.pop())


while len(Hand1)>0 and len(Hand2)>0:
    turn1()
    turn2()
    if len(Hand1)==0:
        break
