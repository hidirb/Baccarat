import random
import os
def createDeck():
    Deck = []

    faceValues = ["A","J","Q","K"]
    for i in range(4):
        for card in range(2,11):
            Deck.append(str(card))

        for card in faceValues:
            Deck.append(card)
    random.shuffle(Deck)
    return Deck




class Player:

    def __init__(self,hand = [],money = 1000):
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0

    def __str__(self):
        currentHand = ""
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = "Player's Hand: " + currentHand + "Score " + str(self.score)

        return finalStatus


    def setScore(self):
        self.score = 0
        faceCardsDict = {"A":1,"J":0,"Q":0,"K":0,
                        "2":2,"3":3,"4":4,"5":5,"6":6,
                        "7":7,"8":8,"9":9,"10":0}

        for card in self.hand:
                self.score += faceCardsDict[card]
                if self.score > 9:
                    self.score -= 10
        return self.score

    def play(self,newHand):
        self.hand =newHand
        self.score = self.setScore()

    def playerBet(self,amount):
        self.money -= amount
        self.bet += amount

    def win(self,result):
        if result == True:
            self.money += 2*self.bet
            self.bet = 0
        else:
            self.bet = 0

    def baccarat(self):
        if self.score == 9:
            return True
        else:
            return False

    def tie(self):
        if chooseBet == 1 or chooseBet == 2: 
            self.money += self.bet
            self.bet = 0
        else:
            if chooseBet == 3 or chooseBet == 4:
                self.money += 2*self.bet
                self.bet = 0

    def playerWin(self):
        if player1.score > House.score:
            player1.win(True)


class Bank:
    def __init__(self,hand = [], money = 1000):
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0

    def __str__(self):
        currentHand = ""
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = "Banker's Hand: " + currentHand + "Score " + str(self.score)

        return finalStatus
    
    def setScore(self):
        self.score = 0
        faceCardsDict = {"A":1,"J":0,"Q":0,"K":0,
                        "2":2,"3":3,"4":4,"5":5,"6":6,
                        "7":7,"8":8,"9":9,"10":0}

        for card in self.hand:
                self.score += faceCardsDict[card]
                if self.score > 9:
                    self.score -= 10
        return self.score

    def play(self,newHand):
        self.hand =newHand
        self.score = self.setScore()

    # def win(self,result):
    #     if result == True:
    #         self.money += 2*self.bet
    #         self.bet = 0
    #     else:
    #         self.bet = 0

    # def playerBet(self,amount):
    #     self.money -= amount
    #     self.bet += amount

    # def bankWin(self):
    #     if player1.score < House.score:
    #         House.win(True)

def clear():
    helpTab = input("Type help for help ") 
    if helpTab == ("help"):
        os.system("help.txt")


cardDeck = createDeck()
firstHand = [cardDeck.pop(),cardDeck.pop()]
secondHand = [cardDeck.pop(),cardDeck.pop()]
player1 = Player(firstHand)
House = Bank(secondHand)
cardDeck = createDeck()

name = input("Please enter your name: ")
print("Welcome to baccarat ",name)
while(True):
    if len(cardDeck) < 49:
        cardDeck = createDeck()
    firstHand = [cardDeck.pop(),cardDeck.pop()]
    secondHand = [cardDeck.pop(),cardDeck.pop()]
    player1.play(firstHand)
    House.play(secondHand)
    print("Your total playable cash is ", player1.money)
    placeBet = int(input("Please enter your bet amount: "))
    print("\nHere are your bet choices: \n1) Player \n2) Bank \n3) Player/Tie \n4) Bank/Tie \n5 Help")
    chooseBet = input("Choose your bet: ")

    player1.playerBet(placeBet)
    print(player1)
    print(House)
    
    if chooseBet == 1:
        if player1.score > House.score:
            player1.win(True)
            print(name,"Wins")

        elif player1.score == House.score:
            player1.tie()

        else:
            player1.win(False)
            print(name,"Loses")

    elif chooseBet == 2:
        if player1.score < House.score:
            player1.win(True)
            print(name,"Wins")

        elif player1.score == House.score:
            player1.tie()

        else:
            player1.win(False)
            print(name,"Loses")

    elif chooseBet == 3:
        if player1.score > House.score:
            player1.win(True)
            print(name,"Wins")

        elif player1.score == House.score:
            player1.tie()

        else:
            player1.win(False)
            print(name,"Loses")


    elif chooseBet == 4:
        if player1.score < House.score:
            player1.win(True)
            print(name,"Wins")

        elif player1.score == House.score:
            player1.tie()

        else:
            player1.win(False)
            print(name,"Loses")


    else:
        clear()
