from cardmechanics import Card
from random import randint

class HoldemRules:
    SCORE = 0
    @staticmethod
    def goodDeal(hand,middle,cash,bet):
        thisHand = []
        thisHand.extend(hand)
        thisHand.extend(middle)
        bluff = randint(1,100) > 95
        if bet >0 and cash > 0:
            risk = randint(0,108-(100*bet)//cash)
        else:
            risk = randint(0,100)
        multiCard = HoldemRules.checkForPair(thisHand)
        highestCard = HoldemRules.checkForHighCard(thisHand)
        if len(thisHand) == 2:
            if bluff:
                return (3*cash*randint(90,100))//500
            elif multiCard == 2:
                if risk > 50:
                    return (cash*highestCard*risk*randint(90,100))//650000
                elif risk < 10:
                    if highestCard >= 10:
                        return "call"
                    return "fold"
                else:
                    return "call"
            else:
                if risk > 75:
                    return (cash*highestCard*risk*randint(90,100))//1300000
                elif risk < 15:
                    if highestCard > 10:
                        return "call"
                    return "fold"
                else:
                    return "call"
        else:
            straight = HoldemRules.checkForStraight(thisHand)
            flush = HoldemRules.checkForFlush(thisHand)
            if bluff:
                return (cash*randint(1,100))//100
            elif straight == "royal" and flush == 5:
                return cash
            elif straight == 5 and flush == 5:
                return (cash*randint(90,100))//100
            elif multiCard == 8:
                if risk < 5:
                    return "call"
                else:
                    return (cash*randint(90,100))//100
            elif multiCard == 6:
                if risk <10:
                    return "call"
                else:
                    return (cash*randint(90,100))//111
            elif (flush == 4 and len(thisHand) < 7) or flush == 5 :
                if risk < 12:
                    return "call"
                else:
                    return (cash*randint(90,100))//125
            elif ((straight == 4 and len(thisHand)<7) or straight == 5) or straight == "royal":
                if risk < 15:
                    return "call"
                else:
                    return (cash*randint(90,100))//167
            elif multiCard == 3:
                if risk < 20:
                    return "call"
                elif risk < 5:
                    return "fold"
                else:
                    return (cash*randint(90,100))//200
            elif multiCard == 4:
                if risk < 25:
                    return "call"
                elif risk < 5:
                    return "fold"
                else:
                    return (cash*risk*randint(90,100))//25000
            elif multiCard == 2:
                if risk < 30:
                    return "call"
                elif risk < 10:
                    return "fold"
                else:
                    return (cash*risk*randint(90,100))//100000
            else:
                if risk < 50:
                    return "call"
                elif risk < 15:
                    return "fold"
                else:
                    return (cash*highestCard*risk*randint(90,100))//1300000
                

    @staticmethod
    def results(thisHand,middle,opponent):
        highCardI = HoldemRules.checkForHighCard(thisHand)
        highCardU = HoldemRules.checkForHighCard(opponent)
        thisHand.extend(middle)
        opponent.extend(middle)
        multiCardI = HoldemRules.checkForPair(thisHand)
        straightI = HoldemRules.checkForStraight(thisHand)
        flushI = HoldemRules.checkForFlush(thisHand)
        multiCardU = HoldemRules.checkForPair(opponent)
        straightU = HoldemRules.checkForStraight(opponent)
        flushU = HoldemRules.checkForFlush(opponent)
        print("Lucky Lotto: " + str(highCardI) + " " + str(highCardU) + " " + str(multiCardI) + " " + str(multiCardU) + " " + str(straightI) + " " + str(straightU) + " " + str(flushI) + " " + str(flushU))
        if (straightI == "royal" and flushI == 5) and (straightU == "royal" and flushU == 5):
            if highCardI == highCardU:
                winner = "Tie"
            else:
                winner = True if highCardI > highCardU else False
            result = "royal flush and high card"
        elif (straightI == "royal" and flushI == 5) or (straightU == "royal" and flushU == 5):
            winner = True if straightI == "royal" and flushI == 5 else False
            result = "royal flush"
        elif (straightI == 5 and flushI == 5) and (straightU == 5 and flushU == 5):
            if highCardI == highCardU:
                winner = "Tie"
            else:
                winner = True if highCardI > highCardU else False
            result = "straight flush and high card"
        elif (straightI == 5 and flushI == 5) or (straightU == 5 and flushU == 5):
            winner = True if straightI == 5 and flushI == 5 else False
            result = "straight flush"
        elif multiCardI == 8 and multiCardU == 8:
            if highCardI == highCardU:
                winner = "Tie"
            else:
                winner = True if highCardI > highCardU else False
            result = "four of a kind and high card"
        elif multiCardI == 8 or multiCardU == 8:
            winner = True if multiCardI == 8 else False
            result = "four of a kind"
        elif multiCardI == 6 and multiCardU == 6:
            if highCardI == highCardU:
                winner = "Tie"
            else:
                winner = True if highCardI > highCardU else False
            result = "full house and high card"
        elif multiCardI == 6 or multiCardU == 6:
            winner = True if multiCardI == 6 else False
            result = "full house"
        elif flushI == 5 and flushU == 5:
            if highCardI == highCardU:
                winner = "Tie"
            else:
                winner = True if highCardI > highCardU else False
            result = "flush and high card"
        elif flushI == 5 or flushU == 5:
            winner = True if flushI == 5 else False
            result = "flush"
        elif (straightI == 5 or straightI == "royal") and (straightU == 5 or straightU == "royal"):
            if highCardI == highCardU:
                winner = "Tie"
            else:
                winner = True if highCardI > highCardU else False
            result = "straight and high card"
        elif (straightI == 5 or straightI == "royal") or (straightU == 5 or straightU == "royal"):
            winner = True if straightI == 5 or straightI == "royal" else False
            result = "straight"
        elif multiCardI == 3 and multiCardU == 3:
            if highCardI == highCardU:
                winner = "Tie"
            else:
                winner = True if highCardI > highCardU else False
            result = "three of a kind and high card"
        elif multiCardI == 3 or multiCardU == 3:
            winner = True if multiCardI == 3 else False
            result = "three of a kind"
        elif multiCardI == 4 and multiCardU == 4:
            if highCardI == highCardU:
                winner = "Tie"
            else:
                winner = True if highCardI > highCardU else False
            result = "set of pairs and high card"
        elif multiCardI == 4 or multiCardU == 4:
            winner = True if multiCardI == 4 else False
            result = "set of pairs"
        elif multiCardI == 2 and multiCardU == 2:
            if highCardI == highCardU:
                winner = "Tie"
            else:
                winner = True if highCardI > highCardU else False
            result = "pair and high card"
        elif multiCardI == 2 or multiCardU == 2:
            winner = True if multiCardI == 2 else False
            result = "pair"
        elif highCardI == highCardU:
            winner = "Tie"
            result = "high card"
        else:
            winner = True if highCardI > highCardU else False
            result = "high card"
        if winner == "Tie":
            return "You both tied with a {0}.".format(result)
        elif winner == True:
            return "You won with a {0}.".format(result)
        else:
            return "Your opponent won with a {0}.".format(result)

#return 2 for 1 pair, 4 for 2 pair, 3 for 3 or a kind, 6 for full house, and 8 for 4 of a kind
    @staticmethod
    def checkForPair(thisHand):
        values = []
        for c in thisHand:
            values.append(c.value)
        count = 1
        while len(values):
            current = values.pop()
            if values.count(current) + 1 == 4:
                return 8
            count *= values.count(current) + 1
            for v in values:
                if v == current:
                    values.remove(v)
        if count == 8:
            return 4
        else:
            return count
#returns highest card value or 14 for aces
    @staticmethod
    def checkForHighCard(thisHand):
        values = []
        for c in thisHand:
            values.append(c.value)
        highest = 0
        for v in values:
            if v == 1:
                return 14
            elif v > highest:
                highest = v
        return highest

#Returns the most number of cards within the same suit
    @staticmethod
    def checkForFlush(thisHand):
        suits = []
        for c in thisHand:
            suits.append(c.suit)
        most = 0
        for v in suits:            
            if suits.count(v) > most:
                most = suits.count(v)
        return most
#Returns the highest number of consecutive cards
    @staticmethod
    def checkForStraight(thisHand):
        values = []
        for c in thisHand:
            values.append(c.value)
        most = 1
        def consecutiveCards(upto,v,values):
            if values.count(v+upto)!=0 or (v+upto==14 and values.count(1)!=0):
                return 1 + consecutiveCards(upto+1,v,values)
            return 1
        for v in values:
            cc = consecutiveCards(1,v,values)
            if cc > most:
                most = cc
        if 13 in values and 1 in values and most == 5:
            return "royal"
        if most >= 5:
            return 5
        else:
            return most
