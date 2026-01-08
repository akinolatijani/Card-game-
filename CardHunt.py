from game.Card import Cards
from game.Deck import Deck_of_cards
from game.Enums import Card_type
from art.text_images import print_card_grid, make_card_border,make_grid_card
import random

class CardHunt: 
    def __init__(self ,size=3):
        self.card_deck = Deck_of_cards()
        self.card_deck.shuffle_deck()
        self.size = size 
        self.round_num = 0
        self.start_game = False

        self.grid_cards = []
        self.grid_cells = [] 

    def reveal_card(self,index):
        card = self.grid_cards[index]
        card_value = card.value.name
        suit_symbol = card.suit.value[1]

        empty_lines,_ = make_card_border(card_value,suit_symbol)
        self.grid_cells[index] = make_grid_card(empty_lines, "CORRECT")


    def show_grid(self):
        print(f"\n ROUND {self.round_num} ")
        print_card_grid(self.size, self.grid_cells)
        print(f"Cards left in deck: {len(self.card_deck.cards)}")

    def remaining_cards(self):
         return sum(1 for cards in self.card_deck.cards if cards.card_type != Card_type.JOKER)
   
    def new_round(self):
        needed = self.size **2
        cards_found = [] 

        if self.remaining_cards() < needed:
            self.start_game = False
            return False
        
        self.round_num += 1
        self.card_deck.shuffle_deck()
        self.populate_grid()
        self.show_grid()

        while True:
            while len(cards_found) <= 9:
                current_card_Index = random.randint(0,8)

                if not current_card_Index in cards_found:
                    cards_found.append(current_card_Index) 

                    answer = input(f"Guess cell for :{self.grid_cards[current_card_Index]}: ")
                    self.show_grid()

                    if answer == str(current_card_Index+1).strip():

                        print("CORRECT GUESS !")
                        self.reveal_card(current_card_Index)
                        self.show_grid()

                    else:
                        print("INCORRECT")
                        self.show_grid()



    def populate_grid(self):
        self.grid_cards = []
        self.grid_cells = []

        print("TESTINGGGG 2")

        needed = self.size ** 2

        for grid_number in range(1, needed + 1):
            while True:

                card = self.card_deck.pick_a_card()
                if card is None:
                    print("Deck is empty while populating the grid.")
                    self.start_game = False
                    return

                if card.card_type == Card_type.JOKER:
                    continue

                card_value = card.value.name        
                suit_symbol = card.suit.value[1]

                empty_lines, _ = make_card_border(card_value, suit_symbol)

                #grid_card_lines = make_grid_card(empty_lines, "?")
                #grid_card_lines = make_grid_card(empty_lines, card_value)
                grid_card_lines = make_grid_card(empty_lines, grid_number)

                self.grid_cards.append(card)
                self.grid_cells.append(grid_card_lines)

                break

    