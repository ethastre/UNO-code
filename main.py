import random

print("Welcome to Uno")
Colors = ['Red', 'Green', 'Blue', 'Yellow']
Deck = []
Hand1 = []
Hand2 = []
Discard = []
for h in range(0,2):
   for color in Colors:
       Deck.append([color,"+2"])

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

def turn1():
    print("The Top Of Discard is", Discard[-1])
    print("Player 1 your hand is", Hand1)
    print("Type the position of the card starting at zero, if none match type '0'")
    position = int(input())
    if Hand1 is not None:
        if Hand1[position][0] != Discard[-1][0] and Hand1[position][1] != Discard[-1][1]:
            Hand1.append(Deck.pop())
            print('No Match')
        if Hand1[position][0] == Discard[-1][0] and Hand1[position][1] == "+2":
            for i in range(0, 2):
                Hand2.append(Deck.pop())
        if Hand1[position][0] == Discard[-1][0] or Hand1[position][1] == Discard[-1][1]:
            Discard.append(Hand1.pop(position))

def turn2():
    print("The Top Of Discard is", Discard[-1])
    print("Player 2 your hand is", Hand2)
    print("Type the position of the card starting at zero, if none match type '0'")
    position =int(input())
    if Hand2 is not None:
        if Hand2[position][0] != Discard[-1][0] and Hand2[position][1] != Discard[-1][1]:
            Hand2.append(Deck.pop())
            print('No Match')
        if Hand2[position][0] == Discard[-1][0] and Hand2[position][1] == "+2":
            for i in range(0,2):
                Hand1.append(Deck.pop())
        if Hand2[position][0] == Discard[-1][0] or Hand2[position][1] == Discard[-1][1]:
            Discard.append(Hand2.pop(position))


print(Deck)
while len(Hand1)>0 and len(Hand2)>0:
    turn1()
    if len(Hand1)==0:
        print("Congrats Player 1, you won!")
        break
    turn2()
    if len(Hand2)==0:
        print("Congrats Player 2, you won!")
        break
