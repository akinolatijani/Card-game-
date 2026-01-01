from enum import Enum
import random
import time

delay = 1
Indent = " " * 70
Astericks_Indent = " " * 35
Rules_Indent = " " * 38


def enter_button(message = "Press Enter to continue...."):
    input(f"{Indent}\n" + message)

#creating a class defining joker card and normal cards
class Card_type(Enum):
    NORMAL = 1
    JOKER = 2

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
    def __init__(self, card_suits = None, card_values=None,card_type = Card_type.NORMAL):
        self.suit = card_suits
        self.value = card_values
        self.card_type = card_type
        
    def is_joker_card(self):
        return self.card_type == Card_type.JOKER 
    
    def __str__(self):
        if self.is_joker_card():
            return "JOKER"
        return f"{self.value.name} of {self.suit.value}"
         

class Deck_of_cards():
    def __init__(self):
        #loop through set of cards to create full deck of 52 cards
        self.cards = [ Cards(suit,value, Card_type.NORMAL) 
                    for suit in  Card_suits
                    for value in Card_values ]
        
        for i in range(0,2):
            self.cards.append((Cards(card_type=Card_type.JOKER)))

    def listOfCards(self):
        for i in self.cards:
            #Test print of full deck of cards
           print(i)
        return self.cards

    #Method for shuffling deck of cards
    def shuffle_deck(self):
        num = 1
        #Loop through deck of cards starting from last card in deck 
        for x in range(len(self.cards) -1 ,0,-1):
            #generates random value to swap current index value with
            j = random.randint(0,x)
            self.cards[x] , self.cards[j] = self.cards[j], self.cards[x]
            num+= 1

    def pick_a_card(self):
        if len(self.cards) == 0:
            print("Deck is empty")
            return None
        return self.cards.pop()

        
class HigherLower:
    def __init__(self):
        self.card_deck = Deck_of_cards()
        self.card_deck.shuffle_deck()
        self.current_card = self.pick_new_card()
        self.points = 0
        self.lives = 4
        self.start_game = False
        self.streak = 0

    def pick_new_card(self):
        while True:
            currenrt_card = self.card_deck.pick_a_card()
            if currenrt_card is None:
                self.start_game = False
                return None
           
            if currenrt_card.is_joker_card():
                print(f"{Indent}JOKER CARD! (current card replaced)\n")
                continue
            return currenrt_card
        
    def is_red(self,card):
        return card.suit in (Card_suits.HEARTS, Card_suits.DIA)
    
    def get_game_score(self):
        return self.lives,self.points
    
    def make_a_guess(self):
    
        print(f"{Rules_Indent}Current card : {self.current_card.value.name} of {self.current_card.suit.value}")
        time.sleep(delay)
        print(f"\n{Indent}TIME TO GUESS !".center(100),"\n") 
        time.sleep(2)
        
        risk_raw = input(f"{Indent}Risk Mode? (Y/N): ".center(100)).strip().lower()
        risk_mode = risk_raw in ("y", "yes")

        raw_answer = input(f"{Indent}Pick (H)Higher or (L)Lower: ".center(100)).strip().lower()
        if raw_answer in ("h","higher"):
            answer = "higher"

        elif raw_answer in ("l","lower"):
            answer = "lower"
        else:
            print("\n"+f"{Rules_Indent}Invalid input. Please type H/L or Higher/Lower.\n")
            return None 
        
        print("\n"+f"{Rules_Indent}You picked ",answer,"! Lets see if your right....")
        time.sleep(2)

        next_card = self.card_deck.pick_a_card()

        if next_card is None:
            print(f"{Indent}Deck is empty...I Guess you WON! Kind of....")
            self.start_game = False
            return None 


        #ADD CONSEQUENCE LATER
        if next_card.is_joker_card():
            print("\n"+f"{Indent}JOKER CARD !\n")
            self.current_card = self.pick_new_card()
            return None 
        
        curr = self.current_card.value.value
        nxt = next_card.value.value

        if curr == nxt:
            print("\n"f"{Rules_Indent}STALEMATE! Values are equal.\n".center(100))
            print(f"{Rules_Indent}BONUS ROUND: Guess the color of the next card (R/B)".center(100)+"\n")

            color_guess = input(f"{Indent}Pick (R)ed or (B)lack: ".center(60)).strip().lower()
            if color_guess in ("r", "red"):
                guessed_red = True
            elif color_guess in ("b", "black"):
                guessed_red = False
            else:
                print(f"{Rules_Indent}Invalid input. No bonus/penalty applied.\n")
                self.current_card = next_card
                return

            actual_red = self.is_red(next_card)

            if guessed_red == actual_red:
                self.points += 1
                print(f"{Indent}CORRECT COLOR! (+1 bonus point)\n".center(100))
            else:
                self.lives -= 1
                print(f"{Indent}WRONG COLOR! (-1 life)\n".center(100))

            # move on to next round
            self.current_card = next_card
            return
        
        if curr < nxt: 
            correct_answer = "higher"
            self.check_guess(answer,correct_answer,next_card, risk_mode)
        elif curr > nxt: 
            correct_answer = "lower"
            self.check_guess(answer,correct_answer,next_card, risk_mode)

        time.sleep(delay)
        print(f"{Rules_Indent}The card was",next_card.value.name,"of",next_card.suit.value)

        if self.lives <= 0: 
            print("\n"+Astericks_Indent + "*" * 100)
            print(f"{Indent}LIVES RAN OUT ! GAME OVER".center(100,"*"),"\n" ) 

            self.start_game = False
        elif self.points >= 10:
            print(f"{Indent}YOU WON GAME ! CONGRATULATIONS".center(100,"*"),"\n" ) 
            self.start_game = False

        else:
            self.current_card = next_card
            

    def check_guess(self,answer,correct_answer,next_card,risk_mode): 
        if (answer == correct_answer):
            self.streak += 1
           
            if self.streak >= 5:
                gained = 3
            elif self.streak >= 3:
                gained = 2
            else:
                gained = 1 
            
            if next_card.value == Card_values.ACE:
                gained *= 2
                print("\n"+f"{Indent} ACE BONUS! DOUBLE POINTS!\n".center(100)) 
    
            if risk_mode:
                gained *= 2
                print("\n"+f"{Indent} RISK MODE WIN! Points doubled again!\n".center(100))

            self.points += gained
            print("\n"+f"{Indent} CORRECT! (+{gained} points)  Streak: {self.streak}\n".center(100))

        else:
            self.streak = 0

            self.points -= 1

            if risk_mode:
                self.lives -= 2
                print("\n"+f"{Indent} WRONG in RISK MODE! (-1 point, -2 lives)\n".center(100))
            else:
                self.lives -= 1
                print("\n"+f"{Indent} WRONG! (-1 point, -1 life)\n".center(100))
 
def main():
    print(f"{Indent}WELCOME TO HIGHER/LOWER".center(100, "*"),"\n")
    print(f"{Indent}INSTRUCTIONS OF THE GAME ".center(100,),"\n")
    print(Astericks_Indent + "*" * 100)
 
    rules = [
            "52-card deck + 2 Jokers",
            "One card is drawn to start the game",
            "Each round, guess Higher or Lower",
            "Correct: +1 point | Wrong: -1 point and -1 life",
            "Risk Mode (optional): double points or lose 2 lives",
            "Streaks: 3 correct = +2, 5 correct = +3",
            "ACE doubles points on a correct guess",
            "Stalemate: guess Red/Black (+1 point or -1 life)",
            "Joker: round is skipped and a new card is drawn"
    ]
     
    for rule in rules:
        print(f"{Rules_Indent} • {rule}") 
        time.sleep(delay) 

    enter_button("\n"+"Press to ENTER to see HOW DO YOU WIN".center(100))
    print("\n" + f"{Indent}HOW DO YOU WIN".center(100))

    print(Astericks_Indent + "*" * 100)
    print(f"{Rules_Indent}  • Reach 10 points to WIN the game")
    print(f"{Rules_Indent}  • Bonus points can be earned through streaks, Risk Mode, and ACE cards\n")
    
    enter_button("\n"+"Press ENTER to see HOW YOU LOSE".center((100)))
    print(f"{Indent}HOW DO YOU LOSE".center(100))

    print("\n"+Astericks_Indent + "*" * 100)
    print(f"{Rules_Indent}  • You have 4 LIVES ****")
    print(f"{Rules_Indent}  • Lose all LIVES....GAME OVER \n")
    print(Astericks_Indent + "*" * 100)
    print(f"{Indent}GOODLUCK !".center(100),"\n")

    game = HigherLower()

    Start_game = input(f"{Indent}PRESS (S) TO START GAME".center(100,"*"))
    if Start_game.strip().lower() == "s":
        game.start_game = True 
        
    while game.start_game:
        game.make_a_guess() 
        
        if not game.start_game:
            break  
    
        lives,points = game.get_game_score()
        time.sleep(delay)
        print("\n"+Astericks_Indent + "*" * 100)
        print(f"{Indent}NEXT ROUND !                       YOUR SCORE:", points,
            "\n"+f"{Indent}                                YOUR LIVES:", lives)
        print(Astericks_Indent + "*" * 100)
        time.sleep(2)
     
       
   

if __name__ == "__main__":
    main()