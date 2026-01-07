from game.Card import Cards
from game.Deck import Deck_of_cards
from art.text_images import print_card_grid, make_card_border,make_grid_card

class CardHunt: 
    def __init__(self ,size=3):
        self.card_deck = Deck_of_cards()
        self.card_deck.shuffle_deck()
        self.size = size 
        self.grid_cards = []
        self.grid_cells = [] 

    def populate_grid(self): 
        for i in range(self.size **2):
            card = self.card_deck.pick_a_card()
        
            card_value = card.value.value
            suit_symbol = card.suit.value[1]

            empty_lines, suit_lines = make_card_border(card_value, suit_symbol)
            
            grid_card_lines = make_grid_card(empty_lines, "?")      
            #grid_card_lines = make_grid_card(empty_lines, card_value)
            
            self.grid_cards.append(card)
            self.grid_cells.append(grid_card_lines)

#game = CardHunt(size=3)
#game.populate_grid()

#print_card_grid(3, game.grid_cells)
