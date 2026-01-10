from HigherLower import game_a_main
from CardHunt import game_b_main
import game.ui as ui

def main():
    while True:
        ui.print_game_title("CHOOSE GAME: ")
        choose_game = input(f"{ui.CARD_INDENT} A) Higher/Lower\n {ui.CARD_INDENT}B) Card hunt \n\n").strip().lower()
        ui.print_borderline()
        
        if choose_game == "a":
            game_a_main()
            return
        elif choose_game == "b":
            game_b_main()
            return
        else:
            print(f"{ui.INDb}Invalid choice. Type A or B \n")

if __name__ == "__main__":
    main()


