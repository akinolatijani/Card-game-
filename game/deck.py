import random
from game.Card import Cards
from game.Enums import Card_suits, Card_values, Card_type

class Deck_of_cards():
    def __init__(self, include_jokers=False):

        #loop through set of cards to create full deck of 52 cards
        self.cards = [ Cards(suit,value, Card_type.NORMAL) 
            for suit in  Card_suits
            for value in Card_values ]

        if include_jokers:
            self.cards.extend(Cards(card_type=Card_type.JOKER) for x in range(2)) 
 
    #Method for shuffling deck of cards
    def shuffle_deck(self):
        num = 1
        for x in range(len(self.cards) -1 ,0,-1):
            j = random.randint(0,x)
            self.cards[x] , self.cards[j] = self.cards[j], self.cards[x]
            num+= 1

    def pick_a_card(self):
        if len(self.cards) == 0:
            print("Deck is empty")
            return None
        return self.cards.pop()