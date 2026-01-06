from game.Enums import Card_type
 
class Cards: 
    def __init__(self, card_suits = None, card_values=None, card_type = Card_type.NORMAL):
        self.suit = card_suits
        self.value = card_values
        self.card_type = card_type
        
    def is_joker_card(self):
        return self.card_type == Card_type.JOKER 

    def __str__(self):
        if self.is_joker_card():
            return "JOKER"
        return f"{self.value.name} of {self.suit.value}"