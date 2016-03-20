#Card class is constructed with a value [1-13] and suit [0-4]
#Cards can return their self.value, or self.suit in number form see suit dictionary
#Cards can also return their name in plain English
from random import randint
class Card:
    SUITS = {
       0:"♦",
       1:"♧",
       2:"♥",
       3:"♤"
       }
    FACECARDS = {
        1:"A",
        11:"J",
        12:"Q",
        13:"K"
        }
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '''\
 ----- 
|{0}{1}{2}  |
|     |
|     |
|  {2}{0}{1}|
 ----- 
'''.format(self.FACECARDS[self.value] if self.value in self.FACECARDS else self.value,self.SUITS[self.suit]," " if self.value != 10 else "")
#Decks are created with 52 cards in order by suit then by value
#Deck objects can shuffle themselves (Fisher Yates), return n(default 1) cards off the top of the deck removing them from the top, and reset themselves to an ordered deck
#Decks can also return all of their cards names in a bottom to top list
class Deck:
    
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(1,14):
                self.cards.append(Card(j,i))
                
    def __str__(self):
        string = ""
        for c in self.cards:
            string += c.__str__() + "\n"
        return string

    def shuffle(self):
        currentItem = len(self.cards)-1
        while(currentItem):
            tempItem = self.cards[currentItem]
            r = randint(0,currentItem)
            self.cards[currentItem] = self.cards[r]
            self.cards[r] = tempItem
            currentItem -= 1

    def deal(self,howmany=1):
        dealt = []
        while(howmany):
            dealt.append(self.cards.pop())
            howmany -= 1
        return dealt
    def reset(self):
        self.__init__()


