card_top_left        = "\u250C"
card_top_right       = "\u2510" 
card_botton_left     = "\u2514"
card_bottom_right    = "\u2518"
card_horizontal_line = "\u2500"
card_vertical_line   = "\u2502"

Hearts_image   = "\u2665"
Diamonds_image = "\u2666"
Clubs_image    = "\u2663"
Spades_image   = "\u2660"

Card_top_border = card_top_left + (card_horizontal_line*17) + card_top_right 
Card_side_border = card_vertical_line +(" " * 17) + card_vertical_line
Card_bottom_border = card_botton_left + (card_horizontal_line*17) + card_bottom_right


def Card_side_with_value(value,suit):
    return f"{card_vertical_line}{value:<2}{' ' * 15}{card_vertical_line}",f"{card_vertical_line}{' ' * 15}{value:<2}{card_vertical_line}",f"{card_vertical_line}{' ' * 8}{suit:<2}{' '*7}{card_vertical_line}"

