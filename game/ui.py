import time
from art.text_images import make_card_border

SCREEN_WIDTH = 100 
BORDER = "*" * SCREEN_WIDTH

DELAY_SHORT       = 1
DELAY_LONG        = 2
CARD_REVEAL_DELAY = 0.5

INDENT           = " " * 35
RULES_INDENT     = " " * 38
ASTERICKS_INDENT = " " * 25
CARD_INDENT      = " " * 75

RULES = [
            "52-card deck + 2 Jokers",
            "One card is drawn to start the game",
            "Each round, guess Higher or Lower",
            "Correct: +1 point | Wrong: -1 point and -1 life",
            "Risk Mode (optional): double points or lose 2 lives",
            "Streaks: 3 correct = +2, 5 correct = +3",
            "ACE doubles points on a correct guess",
            "Stalemate: guess Red/Black (+1 point or -1 life)",
            ]


def display_card(value, suit_symbol):
    cursor_move   =  "\033[F"
    cursor_erase  =  "\033[K"

    empty_lines, suit_lines = make_card_border(value, suit_symbol)
    
    for line in empty_lines:
        print(f"{CARD_INDENT}{line}")
        time.sleep(CARD_REVEAL_DELAY)

    time.sleep(CARD_REVEAL_DELAY*2)

    lines_up = len(empty_lines) - 4
    for x in range(lines_up):
        print(cursor_move, end="") 

    print(cursor_erase, end="")
    print(f"{CARD_INDENT}{suit_lines}")

    print("\n\n\n\n\n")


def enter_button(message = "Press Enter to continue...."):
    input(f"{INDENT}\n" + message)

def print_borderline():
    print(ASTERICKS_INDENT + BORDER)

def print_game_title(text):
    print(f"{INDENT}{text}".center(SCREEN_WIDTH),"\n")

def print_rules(rules):
    print_borderline()
    for rule in rules:
        print(f"{RULES_INDENT} • {rule}") 
        time.sleep(DELAY_SHORT) 
    print_borderline()

def print_game_info():
    enter_button("\n"+"Press to ENTER to see HOW DO YOU WIN".center(SCREEN_WIDTH))
    print("\n" + f"{INDENT}HOW DO YOU WIN".center(SCREEN_WIDTH))
    print_borderline()
    print(f"{RULES_INDENT}  • Reach 10 points to WIN the game")
    print(f"{RULES_INDENT}  • Bonus points can be earned through streaks, Risk Mode, and ACE cards\n")
    
    enter_button("Press ENTER to see HOW YOU LOSE".center((SCREEN_WIDTH)))
    print("\n"+  (INDENT + "HOW DO YOU LOSE").center(SCREEN_WIDTH))
    print_borderline()
    print(f"{RULES_INDENT}  • You have 4 LIVES ****")
    print(f"{RULES_INDENT}  • Lose all LIVES....GAME OVER \n")
    print(f"{INDENT}GOODLUCK !".center(SCREEN_WIDTH),"\n")

    print_borderline()

def print_round_summary(points, lives):
    print_borderline()
    print(  
            f"{INDENT}NEXT ROUND !                          YOUR SCORE: {points}\n"
            f"{INDENT}                                      YOUR LIVES: {lives}"
        )
    print_borderline()
    time.sleep(DELAY_LONG)

        