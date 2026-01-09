from HigherLower import game_A_main
from CardHunt import game_B_main
import game.ui as ui

def main():
    ui.print_game_title("CHOOSE GAME: ")
    choose_game = input(f"{ui.CARD_INDENT} A) Higher/Lower\n {ui.CARD_INDENT}B) Card hunt \n\n").strip().lower()
    ui.print_borderline()
    
    if choose_game == "a":
        game_A_main()
    elif choose_game == "b":
        game_B_main()
           
if __name__ == "__main__":
    main()


