import game.ui as ui

card_top_left        = "\u250C"
card_top_right       = "\u2510" 
card_botton_left     = "\u2514"
card_bottom_right    = "\u2518"
card_horizontal_line = "\u2500"
card_vertical_line   = "\u2502"

card_mm =  "\u253c"
card_mr = "\u2524" 
card_ml = "\u251c" 
card_bm = "\u2534"   
card_tm = "\u252c"

Hearts_image   = "\u2665"
Diamonds_image = "\u2666"
Clubs_image    = "\u2663"
Spades_image   = "\u2660"

def grid_top(size, cell_width):
    return (
        card_top_left +
        card_tm.join(card_horizontal_line * (cell_width + 2) for x in range(size)) +
        card_top_right
    )

def grid_middle(size, cell_width):
    return (
        card_ml +
        card_mm.join(card_horizontal_line * (cell_width + 2) for x in range(size)) +
        card_mr
    )

def grid_top(cols, cell_width):
    return (
        card_top_left +
        card_tm.join(card_horizontal_line * (cell_width + 2) for _ in range(cols)) +
        card_top_right
    )

def grid_middle(cols, cell_width):
    return (
        card_ml +
        card_mm.join(card_horizontal_line * (cell_width + 2) for _ in range(cols)) +
        card_mr
    )

def grid_bottom(cols, cell_width):
    return (
        card_botton_left +
        card_bm.join(card_horizontal_line * (cell_width + 2) for _ in range(cols)) +
        card_bottom_right
    )

def empty_content_line(cols, cell_width):
    blank_cell = " " * (cell_width + 2)
    return card_vertical_line + card_vertical_line.join(blank_cell for x in range(cols)) + card_vertical_line

def print_card_grid(size, cells):
  
    cell_height = len(cells[0])              
    cell_width = len(cells[0][0]) - 2      

    print(ui.INDENT+grid_top(size, cell_width))

    for r in range(size):   
        row_cells = cells[r*size:(r+1)*size]

        for line_i in range(cell_height):
            print(ui.INDENT+
                card_vertical_line +
                card_vertical_line.join(row_cells[c][line_i] for c in range(size)) +
                card_vertical_line
            )

        if r != size - 1:
            print(ui.INDENT+grid_middle(size, cell_width))

    print(ui.INDENT+grid_bottom(size, cell_width))


Card_top_border = card_top_left + (card_horizontal_line*17) + card_top_right 
Card_side_border = card_vertical_line +(" " * 17) + card_vertical_line
Card_bottom_border = card_botton_left + (card_horizontal_line*17) + card_bottom_right

def make_card_border(value, suit):
    top_line_value      = f"{card_vertical_line}{suit:<2}{' ' * 15}{card_vertical_line}"
    bottom_line_value   = f"{card_vertical_line}{' ' * 15}{suit:<2}{card_vertical_line}"
    middle__line_suit   = f"{card_vertical_line}{' ' * 8}{value:<2}{' '*7}{card_vertical_line}"
    
    lines = [
                Card_top_border,
                top_line_value,
                Card_side_border,
                Card_side_border,
                Card_side_border,
                Card_side_border,
                Card_side_border,
                Card_side_border,
                bottom_line_value,
                Card_bottom_border
            ]
    
    return lines, middle__line_suit

def make_grid_card(lines, centre_text):
 
    card_lines = lines.copy()

    centre_index = len(card_lines) // 2
    inner_width = len(card_lines[0]) - 2 

    card_lines[centre_index] = (
        card_vertical_line +
        str(centre_text).center(inner_width) +
        card_vertical_line
    )
    return card_lines
