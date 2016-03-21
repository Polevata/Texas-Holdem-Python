from cardmechanics import *
from holdemrules import *
import os

class TexasHoldem:
    CASH = 500
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.yourHand = []
        self.opponentsHand = []
        self.middle = []
        self.pot = 0
        self.theDeck = Deck()
        self.keepBetting = True

    def runGame(self):
        self.theDeck.shuffle()
        self.yourHand.extend(self.theDeck.deal(2))
        self.opponentsHand.extend(self.theDeck.deal(2))
        self.bet(0)
        self.middle.extend(self.theDeck.deal(3))
        if self.keepBetting == True:
            self.bet(1)
        if self.keepBetting == True:
            self.bet(2)
        if self.keepBetting == True:
            self.bet(3)
            self.showAll()
            result = HoldemRules.results(self.yourHand,self.middle,self.opponentsHand)
            self.endGame(result)
        else:
            self.endGame()
    def status(self):
        print("Your current net worth is ${0}.".format(self.CASH))
        print("The pot is at ${0}".format(self.pot))
        print("Your Hand:")
        for i in range(len(self.yourHand[0].__str__().splitlines())):
            for c in self.yourHand:
                print(c.__str__().splitlines()[i],end=" ")
            print()
        if len(self.middle) != 0:
            print("Community Cards:")
            for i in range(len(self.middle[0].__str__().splitlines())):
                for c in self.middle:
                    print(c.__str__().splitlines()[i],end=" ")
                print()

    def bet(self,round):
        self.status()
        if round == 0:
            b = int(input('Please enter a starting bid: $'))
        else:
            b = int(input('How much are you willing to raise: $'))
        if b>self.CASH:
            b=self.CASH
            self.CASH = 0
            self.pot += self.CASH
            print("You go all in")
        else:
            self.CASH -= b
            self.pot += b
        decision = HoldemRules.goodDeal(self.opponentsHand,self.middle,self.CASH,b)
        if decision == "call":
            self.pot += b
            print("Your opponent called. The pot is now up to ${0}".format(self.pot))
        elif decision == "fold":
            self.keepBetting = False
            self.CASH += self.pot
            print("You're a bit too rich for your opponent's blood. They fold. You've won ${0}.".format(self.pot))
        else:
            s = str(input("Your opponent raised you by ${0}! Do you wish to call or fold: ".format(decision)))
            if "call" in s or "Call" in s:
                if decision + b > self.CASH:
                    self.pot += self.CASH
                    self.keepBetting = False
                    print("You both go all in and begin the wait.")
                else:
                    self.pot += b + decision
                    self.CASH -= decision
            else:
                self.keepBetting = False
                print("Your oppoent smiles as you step away from the table.")
        print("\n")
        if round != 0:
            self.middle.extend(self.theDeck.deal())

    def showAll(self):
        self.status()
        print("Opponents Hand:")
        for i in range(len(self.yourHand[0].__str__().splitlines())):
            for c in self.opponentsHand:
                print(c.__str__().splitlines()[i],end=" ")
            print()
    def endGame(self,result=""):
        print(result)
        if "tied" in result:
            self.CASH += self.pot//2
            print("The pot of ${0} was split evenly between you.".format(self.pot))
        elif "opponent" in result:
            print("The pot of ${0} was all given to your opponent.".format(self.pot))
        elif "won" in result:
            self.CASH += self.pot
            print("You won all ${0} in the pot!".format(self.pot))
        else:
            print("You lost all ${0} in the pot!".format(self.pot))
        boo = str(input("Would you like to play again? (Y/N) "))
        if "Y" in boo or "y" in boo:
            print()
            self.__init__()
            self.runGame()
        else:
            print("Thanks for playing!")
            
if __name__ == '__main__':
    myGame = TexasHoldem()
    myGame.runGame()
    
