from enum import Enum
from art.text_images import Hearts_image, Diamonds_image, Clubs_image, Spades_image

class Card_type(Enum):
    NORMAL = 1
    JOKER = 2

class Card_suits(Enum):
    HEARTS  = ("Hearts",Hearts_image)
    DIA     = ("Diamonds",Diamonds_image)
    CLUBS   = ("Clubs",Clubs_image)
    SPADES  = ("Spades",Spades_image)
    
    def __init__(self, label, symbol):
        self.label = label
        self.symbol = symbol

class Card_values(Enum):
    TWO   = 2 
    THREE = 3
    FOUR  = 4
    FIVE  = 5 
    SIX   = 6
    SEVEN = 7
    EIGHT = 8
    NINE  = 9 
    TEN   = 10 
    JACK  = 11
    QUEEN = 12
    KING  = 13 
    ACE   = 14
