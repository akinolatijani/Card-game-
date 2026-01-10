import time
import game.ui as ui
from game.Deck import Deck
from game.Config import (STREAK_BONUS_3,
                            STREAK_BONUS_5,
                            BASE_POINTS,
                            ACE_MULTIPLIER,
                            RISK_MULTIPLIER,
                            RISK_LIFE_PENALTY,
                            NORMAL_LIFE_PENALTY
)
     
class HigherLower:
    def __init__(self):
        self.card_deck = Deck(include_jokers=True)
        self.card_deck.shuffle_deck()
        self.current_card = self.pick_new_card()

        self.points    = 0
        self.lives     = 4
        self.streak    = 0
        self.round_num = 0
        self.WIN_POINTS = 10
        self.start_game = False
        self.hints_remaining = 3

    def get_round_num(self):
        return self.round_num 

    def is_red(self,card):
        return card.suit.label in ("Hearts","Diamonds")
    
    def get_game_score(self):
        return self.lives,self.points

    def pick_new_card(self):
        while True:
            currenrt_card = self.card_deck.pick_a_card()

            if currenrt_card is None:
                self.start_game = False
                return None
           
            if currenrt_card.is_joker_card():
                print(f"{ui.INDENT}JOKER CARD!\n")
                continue

            return currenrt_card
        
    def draw_next_card(self, indent):
        next_card = self.card_deck.pick_a_card()
        if next_card is None:
            print(f"{indent}Deck is empty. I guess you WON! Kind of....")
            self.start_game = False
            return None
        return next_card

    def next_card_probability(self):
        if self.current_card is None:
            return {"higher": (0,0.0),"lower": (0,0.0),"equal": (0,0.0),"joker": (0,0.0),"total": (0,0.0)}
        
        remaining_cards = self.card_deck.cards
        total_cards = len(remaining_cards)

        if total_cards == 0:
            return {"higher": (0,0.0),"lower": (0,0.0),"equal": (0,0.0),"joker": (0,0.0),"total": (0,0.0)}

        current_value = self.current_card.value.value

        higher,lower,equal,joker = 0,0,0,0 

        for card in remaining_cards:
            if card.is_joker_card():
                joker += 1
                continue
            
            card_value = card.value.value

            if card_value > current_value:
                higher += 1
            elif card_value < current_value:
                lower += 1
            else:
                equal += 1

            
        return {"higher": (higher, higher / total_cards),"lower":  (lower, lower / total_cards),"equal": (equal, equal / total_cards),"joker":  (joker, joker / total_cards),"total": (total_cards, 1.0),}

    def display_probability_hint(self, rules_indent, indent):
        probabilities = self.next_card_probability()
        total_cards = probabilities["total"][0]

        if total_cards == 0:
            return
        
        higher_count, higher_prob = probabilities["higher"]
        lower_count, lower_prob = probabilities["lower"]
        equal_count, equal_prob = probabilities["equal"]
        joker_count, joker_prob = probabilities["joker"]

        message = [
        f"Next card odds (out of {total_cards})",
        f"Higher: {higher_prob * 100:.1f}% ({higher_count})",
        f"Lower: {lower_prob * 100:.1f}% ({lower_count})",
        f"Equal: {equal_prob * 100:.1f}% ({equal_count})",
        ]

        if joker_count > 0:
            message.append(f"Joker {joker_prob * 100:.1f}% ({joker_count})")
       
        for msg in message:
            print(f"{rules_indent}{msg}") 

    def show_current_card(self, rules_indent, indent):
        print( "\n", f"{rules_indent}    Current card : {self.current_card.value.name} of {self.current_card.suit.label}", )
        time.sleep(ui.DELAY_SHORT)

        print(f"\n{indent}{indent}TIME TO GUESS !".center(ui.SCREEN_WIDTH), "\n")
        time.sleep(ui.DELAY_LONG)

    def prompt_risk_mode(self, rules_indent, indent) -> bool:
        while True:
            risk_raw = (
                input(f"{indent}Risk Mode? (Y/N): ".center(ui.SCREEN_WIDTH))
                .strip()
                .lower()
            )
            if risk_raw in ("y", "yes"):
                return True
            if risk_raw in ("n", "no"):
                return False
            print("\n" + f"{rules_indent}Invalid input. Yes/No or Y/N: \n")

    def prompt_higher_lower(self, rules_indent, indent) -> str:
        while True:
            raw_answer = (input(f"{indent}Pick (H)Higher or (L)Lower: ".center(ui.SCREEN_WIDTH)).strip().lower())
            if raw_answer in ("h", "higher"):
                return "higher"
            if raw_answer in ("l", "lower"):
                return "lower"
            print("\n"+ f"{rules_indent}Invalid input. Please type H/L or Higher/Lower.\n")

    def prompt_red_black(self, rules_indent, indent):
        color_guess = (
            input(f"{indent}Pick (R)ed or (B)lack: ".center(60)).strip().lower() )
        if color_guess in ("r", "red"):
            return True
        if color_guess in ("b", "black"):
            return False

        print(f"{rules_indent}Invalid input. No bonus/penalty applied.\n")
        return None

    def reveal_next_card(self, next_card, indent):
        time.sleep(ui.DELAY_SHORT)
        ui.display_card(next_card.value.value, next_card.suit.symbol)
        print(f"{indent}The card was {next_card.value.name} of {next_card.suit.label}")

    def handle_joker(self, indent):
        print("\n" + f"{indent}JOKER CARD !\n".center(ui.SCREEN_WIDTH))
        print(f"{indent}Points reset! JOKES ON YOU!\n".center(ui.SCREEN_WIDTH))

        self.points = 0
        self.current_card = self.pick_new_card()
        return True

    def handle_stalemate(self, next_card, rules_indent, indent):
        print("\n"f"{rules_indent}STALEMATE! Values are equal.\n".center(ui.SCREEN_WIDTH))
        print(f"{rules_indent}BONUS ROUND: Guess the colour of the card (R/B)".center(ui.SCREEN_WIDTH)+ "\n" )

        guessed_red = self._prompt_red_black(rules_indent, indent)
        if guessed_red is None:
            self.current_card = next_card
            return True

        actual_red = self.is_red(next_card)

        if guessed_red == actual_red:
            self.points += 1
            print(f"{indent}CORRECT COLOUR! (+1 bonus point)\n".center(ui.SCREEN_WIDTH))
        else:
            self.lives -= 1
            print(f"{indent}WRONG COLOUR! (-1 life)\n".center(ui.SCREEN_WIDTH))

        self.current_card = next_card
        self.round_num += 1
        return True

    def correct_answer(self, curr_value: int, next_value: int) -> str:
        return "higher" if next_value > curr_value else "lower"

    def check_end_conditions(self, indent) -> bool:
        if self.lives <= 0:
            ui.print_borderline()
            print(f"{indent}LIVES RAN OUT ! GAME OVER".center(ui.SCREEN_WIDTH), "\n")
            ui.print_borderline()
            self.start_game = False
            return True

        if self.points >= self.WIN_POINTS:
            ui.print_borderline()
            print(f"{indent}YOU WON GAME ! CONGRATULATIONS".center(ui.SCREEN_WIDTH), "\n")
            ui.print_borderline()
            self.start_game = False
            return True

        return False


    def make_a_guess(self,rules_indent, indent):

        if self.current_card is None:
            self.start_game = False
            return False

        self.show_current_card(rules_indent, indent)
        hint_request = input(f"{indent}   Enter need a hint (Y/N): ").lower().strip()
        if hint_request == "y":
            if self.hints_remaining > 0:
                self.hints_remaining -= 1
                self.display_probability_hint(rules_indent, indent)
            else:
                print(f"{indent}No hints remaining")

        risk_mode = self.prompt_risk_mode(rules_indent, indent)
        answer = self.prompt_higher_lower(rules_indent, indent)

        print("\n"+ f"{rules_indent}You picked {answer}! Let's see if you're right....")
        time.sleep(1)

        next_card = self.draw_next_card(indent)
        if next_card is None:
            return False 

        if next_card.is_joker_card():
            return self.handle_joker(indent)
        
        curr = self.current_card.value.value
        nxt = next_card.value.value

        if curr == nxt:
                return self.handle_stalemate(next_card, rules_indent, indent)

        self.reveal_next_card(next_card, indent)

        correct_answer = self.correct_answer(curr,nxt)
        self.check_guess(answer, correct_answer, next_card, risk_mode)
               
        self.round_num += 1

        if self.check_end_conditions(indent):
            return False
        
        self.current_card = next_card
        return True

    def check_guess(self,answer,correct_answer, next_card, risk_mode): 
        if (answer == correct_answer):
            self.streak += 1
           
            if self.streak >= 5:
                gained = STREAK_BONUS_5
            elif self.streak >= 3:
                gained = STREAK_BONUS_3
            else:
                gained = BASE_POINTS
            
            if next_card.value.name == "ACE":
                gained *= ACE_MULTIPLIER
                print("\n"+f"{ui.INDENT} ACE BONUS! DOUBLE POINTS!\n".center(ui.SCREEN_WIDTH)) 
    
            if risk_mode:
                gained *= RISK_MULTIPLIER
                print("\n"+f"{ui.INDENT} RISK MODE WIN! Points doubled again!\n".center(ui.SCREEN_WIDTH))

            self.points += gained
            print("\n"+f"{ui.INDENT} CORRECT! (+{gained} points)  Streak: {self.streak}\n".center(ui.SCREEN_WIDTH))
            return None
        
        
        self.streak = 0
        self.points -= BASE_POINTS

        if risk_mode:
            self.lives -= RISK_LIFE_PENALTY
            print("\n"+f"{ui.INDENT} WRONG in RISK MODE! (-1 point, -2 lives)\n".center(ui.SCREEN_WIDTH))
        else:
            self.lives -= NORMAL_LIFE_PENALTY
            print("\n"+f"{ui.INDENT} WRONG! (-1 point, -1 life)\n".center(ui.SCREEN_WIDTH))
        return None
    
    

def game_a_main():
    ui.print_game_title("WELCOME TO HIGHER OR LOWER GAME ")
    ui.print_game_title("GAME INSTRUCTIONS")
    ui.print_rules(ui.HIGHER_OR_LOWER_RULES)
    ui.print_game_info()

    while True:
        game = HigherLower()

        Start_game = input(f"{ui.INDENT}  PRESS (S) TO START GAME ").strip().lower()
        if Start_game != "s":
            break

        game.start_game = True 
            
        while game.start_game:
            if game.make_a_guess(ui.RULES_INDENT, ui.INDENT) is False:
                break  
        
            lives, points = game.get_game_score()
            ui.print_round_summary(points, lives,game.get_round_num())
        
        play_again = input("PRESS (P) to PLAY AGAIN\n".center((ui.SCREEN_WIDTH))).strip().lower()
        if play_again != "p":
            break

        ui.print_game_title("Thanks for playing my game ! Hope you enjoyed !")


