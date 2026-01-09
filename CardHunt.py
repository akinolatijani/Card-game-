import random
from game.Card import Cards
from game.Deck import Deck
from game.Enums import Card_type
from art.text_images import print_card_grid, make_card_border,make_grid_card
import game.ui as ui
import time 
from game.Config import (CARDHUNT_DEFAULT_GRID_SIZE, CARDHUNT_STARTING_LIVES, CARDHUNT_POINTS_PER )

class CardHunt: 
    def __init__(self ,size=3):
        self.card_deck = Deck(include_jokers=False)
        self.card_deck.shuffle_deck()
        self.size = size 
       
        self.lives = CARDHUNT_STARTING_LIVES
        self.points = 0

        self.round_num = 0
        self.start_game = False

        self.grid_cards = []
        self.grid_cells = [] 

    def reveal_card(self,index,message):
        card = self.grid_cards[index]
        card_value = card.value.name
        suit_symbol = card.suit.value[1]

        empty_lines,_ = make_card_border(card_value,suit_symbol)
        self.grid_cells[index] = make_grid_card(empty_lines, message)

    def show_grid(self):
        print_card_grid(self.size, self.grid_cells)
        print(f"Cards left in deck: {len(self.card_deck.cards)}")

    def remaining_cards(self):
        return sum(1 for cards in self.card_deck.cards if cards.card_type != Card_type.JOKER)
   
    def get_game_score(self):
        return self.lives,self.points
    
    def get_round_num(self):
        return self.round_num
    
    def new_round(self):
        needed = self.size **2
        cards_found = [] 

        if self.remaining_cards() < needed:
            self.start_game = False
            return False
        
        self.round_num += 1
        self.card_deck.shuffle_deck()
        
        if not self.populate_grid():
            self.start_game = False
            return False
            
        self.show_grid()

        while len(cards_found) < needed:
            current_card_Index = random.randint(0,needed - 1)

            if  current_card_Index in cards_found:
                continue
            cards_found.append(current_card_Index) 

            answer = input(f"      {ui.RULES_INDENT}Guess cell for {self.grid_cards[current_card_Index].value.name} of {self.grid_cards[current_card_Index].suit.label}: ").strip()
    
            if answer == str(current_card_Index+1):
                self.points += CARDHUNT_POINTS_PER
                print(f"{         ui.INDENT}CORRECT GUESS !\n")
                self.reveal_card(current_card_Index, "CORRECT")
                self.show_grid()   

                time.sleep(ui.DELAY_SHORT)
                self.reveal_card(current_card_Index, self.grid_cards[current_card_Index].value.name)
            else:
                self.lives -= 1
                print(f"\n{ui.INDENT}INCORRECT !\n")  
            
            ui.print_round_summary(self.points, self.lives, self.get_round_num())
            self.show_grid()   

            if self.lives <= 0:
                ui.print_borderline()
                print(f"        {ui.INDENT}LIVES RAN OUT! GAME OVER !\n")
                self.start_game = False
                return False
        
        return True

    def populate_grid(self):
        self.grid_cards = []
        self.grid_cells = []

        needed = self.size ** 2

        for grid_number in range(1, needed + 1):
            while True:

                card = self.card_deck.pick_a_card()
                if card is None:
                    print("Deck is empty while populating the grid.")
                    self.start_game = False
                    return False

                if card.card_type == Card_type.JOKER:
                    continue

                card_value = card.value.name        
                suit_symbol = card.suit.value[1]

                empty_lines, _ = make_card_border(card_value, suit_symbol)
                grid_card_lines = make_grid_card(empty_lines, grid_number)

                self.grid_cards.append(card)
                self.grid_cells.append(grid_card_lines)
                break

        return True
    
def game_b_main():
       while True:
        game = CardHunt(size =CARDHUNT_DEFAULT_GRID_SIZE)
        ui.print_game_title("WELCOME TO GUESS THE CARD ")
        ui.print_game_title("GAME INSTRUCTIONS")
        ui.print_borderline()
        ui.print_game_info()

        Start_game = input(f"{ui.INDENT}  PRESS (S) TO START GAME ").strip().lower()
        if Start_game == "s":
            game.start_game = True
    
        while game.start_game:
            if not game.new_round():
                break
            lives,points = game.get_game_score()

            ui.print_round_summary(points, lives, game.get_round_num())

        play_again = input("PRESS (P) to PLAY AGAIN\n".center((ui.SCREEN_WIDTH))).strip().lower()
        if play_again != "p":
            break
            
        ui.print_game_title("Thanks for playing my game ! Hope you enjoyed !")
