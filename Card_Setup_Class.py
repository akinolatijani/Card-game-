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
           # print(num,self.cards[x],"swapped with",self.cards[j]) 

    def pick_a_card(self):
        if self.cards == 0:
            print("Deck is empty")
        else:
            card = self.cards.pop()
            return card
        
class HigherLower:
    def __init__(self):
        self.card_deck = Deck_of_cards()
        self.current_card = self.card_deck.pick_a_card()  
        self.points = 0
        self.lives = 4
        self.start_game = False
    
    def get_game_score(self):
        return self.lives,self.points
    
    def make_a_guess(self):
    
        print(f"Current card : {self.current_card.value.name} of {self.current_card.suit.value}")
        print("\n TIME TO GUESS !".center(70),"\n") 
        
        raw_answer = input("Pick (H)Higher or (L)Lower: ".center(60)).strip().lower()
        if raw_answer in ("h","higher"):
            answer = "higher"

        elif raw_answer in ("l","lower"):
            answer = "lower"
        else:
            print("\nInvalid input. Please type H/L or Higher/Lower.\n")
            
        print("\n You picked ",answer,"! Lets see if your right....\n")
        next_card = self.card_deck.pick_a_card()

        if self.current_card.value.value < next_card.value.value: 
            correct_answer = "higher"
        elif self.current_card.value.value > next_card.value.value: 
            correct_answer = "lower"
        
        self.check_guess(answer,correct_answer)
        print("The card was",next_card.value.name,"of",next_card.suit.value)

        if self.lives == 0: 
            print("LIVES RAN OUT ! GAME OVER".center(70,"*"),"\n" ) 
            self.start_game = False

        else:
            self.currentCard = next_card
            

    def check_guess(self,answer,correct_answer): 
        if (answer == correct_answer):
            self.points += 1
            print("\n CORRECT !".center(70),"\n")

        elif (answer != correct_answer):
            self.lives -=1
            self.points -=1
            print("\n WRONG !".center(70),"\n")
            
        elif (answer == correct_answer):
            print("STALEMATE")
 
def main():
    print("WELCOME TO HIGHER/LOWER".center(70, "*"),"\n")
    print("INSTRUCTIONS OF THE GAME ".center(70,),"\n")
    print("*" * 70)
 
    rules = [
        "You have a deck of 52 cards",
        "At the beginning of the game, a card is drawn",
        "Your aim is to guess if the next card is higher or lower",
        "+2 points for a correct answer, -1 point for an incorrect answer",
        "If the current and next card are equal: no points gained or lost (STALEMATE)",         
    ]
     

    for rule in rules:
        print(f"  • {rule}")

    print("\n" + "HOW DO YOU WIN".center(70))
    print("*" * 70,"\n")
    print("  • Reach 10 points to WIN the game")
    print("  • BONUS: Correct guess + ACE give DOUBLE points \n")
    
    print("HOW DO YOU LOSE".center(70))
    print("*" * 70,"\n")
    print("  • You have 4 LIVES *** Each point lost is a Live gone")
    print("  • Lose all LIVES....GAME OVER \n")
    print("*" * 70,"\n")
    print("GOODLUCK !".center(70),"\n")

    game = HigherLower()

    Start_game = input("PRESS (S) TO START GAME".center(70,"*"))
    if Start_game.strip().lower() == "s":
        game.start_game = True
        
    while game.start_game:
        game.make_a_guess() 
        
        if not game.start_game:
            break  
    
        lives,points = game.get_game_score()
        
        print("*" * 70)
        print("NEXT ROUND !        YOUR SCORE:", points,
            "\n                     YOUR LIVES:", lives)
        print("*" * 70)
    
       
   

if __name__ == "__main__":
    main()