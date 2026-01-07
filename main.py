import time
import game.ui as ui
from game.Deck import Deck_of_cards
from art.text_images import print_card_grid
from CardHunt import CardHunt

def main():
    ui.print_game_title("WELCOME TO GUESS THE CARD ")
    ui.print_game_title("GAME INSTRUCTIONS")
    #ui.print_rules(ui.RULES)
    ui.print_game_info()

    
    game = CardHunt(size=3)
    game.populate_grid()

    print_card_grid(3, game.grid_cells)

    Start_game = input(f"{ui.INDENT}  PRESS (S) TO START GAME ").strip().lower()
        

    """game.start_game = True 
        
    while game.start_game:
        if game.make_a_guess(ui.RULES_INDENT, ui.INDENT) is False:
            break  
    
        lives, points = game.get_game_score()
        ui.print_round_summary(points, lives)
    
    play_again = input("PRESS (P) to PLAY AGAIN".center((ui.SCREEN_WIDTH))).strip().lower()
    if play_again != "p":
        break

ui.print_game_title("Thanks for playing my game ! Hope you enjoyed !")


"""
if __name__ == "__main__":
    main()


