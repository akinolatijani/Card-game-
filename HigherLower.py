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
        self.start_game = False

    def get_round_num(self):
        return self.round_num 

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
        
    def is_red(self,card):
        return card.suit.label in ("Hearts","Diamonds")
    
    def get_game_score(self):
        return self.lives,self.points
    
    def make_a_guess(self,RULES_INDENT,INDENT):

        if self.current_card is None:
            self.start_game = False
            return False

        print("\n",f"{RULES_INDENT}Current card : {self.current_card.value.name} of {self.current_card.suit.label}")
        time.sleep(ui.DELAY_SHORT)

        print(f"\n{INDENT}TIME TO GUESS !".center(ui.SCREEN_WIDTH),"\n") 
        time.sleep(ui.DELAY_LONG)
        
        while True:
            risk_raw = input(f"{INDENT}Risk Mode? (Y/N): ".center(ui.SCREEN_WIDTH)).strip().lower()
            if risk_raw  in ("y", "yes"):
                risk_mode = True
                break
            if risk_raw  in ("n", "no"):
                risk_mode = False
                break
            print("\n"+f"{RULES_INDENT}Invalid input. Yes/No or Y/N: \n")

        while True:
            raw_answer = input(f"{INDENT}Pick (H)Higher or (L)Lower: ".center(ui.SCREEN_WIDTH)).strip().lower()
            if raw_answer in ("h","higher"):
                answer = "higher"
                break
            if raw_answer in ("l","lower"):
                answer = "lower"
                break
            print("\n"+f"{RULES_INDENT}Invalid input. Please type H/L or Higher/Lower.\n")
        
        print("\n"+f"{RULES_INDENT}You picked ",answer,"! Let's see if your right....")
        time.sleep(1)

        next_card = self.card_deck.pick_a_card()

        if next_card is None:
            print(f"{INDENT}Deck is empty.I Guess you WON! Kind of....")
            self.start_game = False
            return False 

        if next_card.is_joker_card():
            print("\n"+f"{INDENT}JOKER CARD !\n".center(ui.SCREEN_WIDTH))
            print(f"{INDENT}Points reset! JOKES ON YOU!\n".center(ui.SCREEN_WIDTH))
            
            self.points = 0
            self.current_card = self.pick_new_card()
            return True 
        
        curr = self.current_card.value.value
        nxt = next_card.value.value

        if curr == nxt:
            print("\n"f"{RULES_INDENT}STALEMATE! Values are equal.\n".center(ui.SCREEN_WIDTH))
            print(f"{RULES_INDENT}BONUS ROUND: Guess the color of the card (R/B)".center(ui.SCREEN_WIDTH)+"\n")

            color_guess = input(f"{INDENT}Pick (R)ed or (B)lack: ".center(60)).strip().lower()
            if color_guess in ("r", "red"):
                guessed_red = True
            elif color_guess in ("b", "black"):
                guessed_red = False
            else:
                print(f"{RULES_INDENT}Invalid input. No bonus/penalty applied.\n")
                self.current_card = next_card
                return True

            actual_red = self.is_red(next_card)

            if guessed_red == actual_red:
                self.points += 1
                print(f"{INDENT}CORRECT COLOR! (+1 bonus point)\n".center(ui.SCREEN_WIDTH))
            else:
                self.lives -= 1
                print(f"{INDENT}WRONG COLOR! (-1 life)\n".center(ui.SCREEN_WIDTH))

            self.current_card = next_card
            self.round_num += 1
            return True
        
        
        time.sleep(ui.DELAY_SHORT)
        ui.display_card(next_card.value.value,next_card.suit.symbol)
        print(f"{INDENT}The card was",next_card.value.name,"of",next_card.suit.label)

        correct_answer = "higher" if nxt > curr else "lower"
        self.check_guess(answer,correct_answer,next_card, risk_mode)
       
        if self.lives <= 0: 
            ui.print_borderline()
            print(f"{INDENT}LIVES RAN OUT ! GAME OVER".center(ui.SCREEN_WIDTH),"\n" ) 
            ui.print_borderline()
            self.start_game = False
            return False
        
        if self.points >= 10:
            ui.print_borderline()
            print(f"{INDENT}YOU WON GAME ! CONGRATULATIONS".center(ui.SCREEN_WIDTH),"\n" ) 
            ui.print_borderline()
            self.start_game = False
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
    ui.print_rules(ui.RULES)
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


