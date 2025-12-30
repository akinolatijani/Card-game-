from enum import Enum
import random



class Card_suits(Enum):
    HEARTS = "Hearts"
    DIA = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"


class Card_values(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5 
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE  = 9 
    TEN = 10 
    JACK = 11
    QUEEN = 12
    KING = 13 
    ACE = 14

class Cards: 
    def __init__(self, card_suits, card_values):
        self.suit = card_suits
        self.value = card_values
    
    def __str__(self):
        return f"{self.value.name} of {self.suit.value}"
         

class Deck_of_cards():
    def __init__(self):
        #loop through set of cards to create full deck of 52 cards
        self.cards = [ Cards(suit,value) 
                    for suit in  Card_suits
                    for value in Card_values ]
        
    def listOfCards(self):
        for i in self.cards:
            #Test print of full deck of cards
            print(i)

    #Method for shuffling deck of cards
    def shuffle_deck(self):
        num = 1
        #Loop through deck of cards starting from last card in deck 
        for x in range(len(self.cards) -1 ,0,-1):
            #generates random value to swap current index value with
            j = random.randint(0,x)
            self.cards[x] , self.cards[j] = self.cards[j], self.cards[x]
            num+= 1
           # print(num,self.cards[x],"swapped with",self.cards[j]) 

#TESTING PURPOSES REMOVE LATER
suitTest = Card_suits
valueTest = Card_values
FullCards = Deck_of_cards()
FullCards.listOfCards()
FullCards.shuffle_deck()
FullCards.listOfCards()


     
