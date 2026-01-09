# Higher/Lower Card Game

## Project Scope 

This project was initially designed as a Higher / Lower card game and was later extended with an alternative game mode to demonstrate how a single, reusable card system could support multiple gameplay styles.

The project uses a standard 52-card deck with the addition of two Joker cards. Both games are played entirely in the terminal using a text-based user interface. The focus was on producing clear, maintainable logic and extensible design rather than graphical complexity.

The primary aim of this project was to demonstrate decision-making around structure, extensibility, and responsibility boundaries, rather than maximising feature count.

## Design Decisons 

The core requirements of the project were intentionally implemented first, before introducing extensions:

A standard deck abstraction to avoid duplicating card logic

A controlled shuffling and drawing mechanism to prevent invalid game states

Explicit rule handling to keep gameplay predictable and testable

A CLI-based interface to prioritise logic clarity over presentation

Beyond these requirements, the project was extended with the following decisions in mind:

Joker cards were added to introduce non-linear outcomes and force explicit handling of exceptional states

A shared deck and card model was used to ensure both games relied on the same core logic, reducing duplication

A second game mode (Card Hunt) was implemented to validate that the card and deck abstractions were flexible enough to support alternative rules

A separate UI module was introduced to avoid embedding formatting and presentation logic directly into game rules

The main trade-off of this approach is increased upfront structure for a relatively small project. This was considered acceptable in order to demonstrate scalability and reasoning rather than minimalism.

## OOP(Object- Orientated Programming) Approach

Object-Oriented Programming was chosen because it aligns naturally with the problem domain and allows behaviour to be grouped with the data it operates on.

Rather than focusing on OOP principles in isolation, this project uses OOP to:

Enforce clear ownership of responsibilities

Limit how and where card state can be modified

Make it easier to introduce new game modes without altering existing logic

An alternative procedural approach would have reduced boilerplate but would have made reuse across multiple games more error-prone.

## Class Structure: 

### Cards Class
The Cards class represents a single playing card and acts as a simple data holder with minimal behaviour.

This design was chosen to:

   - Keep card state immutable during gameplay

   - Avoid spreading suit/value logic across multiple files

   - Make Joker handling explicit via a dedicated card type

More complex behaviour (such as scoring) was deliberately kept out of this class to avoid mixing responsibilities.

### Deck_of_cards Class

The deck class owns the lifecycle of all cards and is the only component allowed to create, shuffle, or remove cards from play.

This prevents:

- Games directly manipulating the underlying card collection

- Accidental reuse of cards already drawn

- Inconsistent shuffling behaviour across different game modes

The trade-off is that games must interact with the deck through a fixed interface, slightly reducing flexibility in favour of safety.

## Game Modes

## HigherLower Game

### HigherLower Class 
The HigherLower class contains the core game logic

Manages:
- Game flow

- Handling player input

- Scoring and lives

- Streak and bonus logic

- Determining Win and lose conditions

Each round presents the player with a card and asks them to guess whether the next card will be higher or lower in value.

Additional mechanics such as streak bonuses, Risk Mode, and ACE multipliers were added to increase strategic depth while keeping the core gameplay simple.

This class component was key for contorlling the game, coordinating interactions between the deck, the player and user interface

## Key Methods for HigherLower Game Class

### Pick_new_card() 

This method exists to ensure Joker handling is consistent and does not leak into multiple areas of the game logic.

By centralising this behaviour, rule changes affecting Jokers can be made in one place without modifying round logic.

### make_a_guess() 

This method represents a single round of gameplay and acts as the main game loop step.

Although the method is longer than ideal, this was a conscious decision to keep the full round lifecycle visible in one place, making the flow easier to reason about during debugging.

- It handles:

- User input (including validation)

- Risk Mode selection

- Card comparison

- Special cases such as Jokers and stalemates

- Win and loss checks

Keeping this logic in one method ensures the round flow is easy to follow and modify.

### check_guess()

 Reason for a seperate method was to isolate penalty logic ,making it easy to manage streaks,risk mode, bonuses ,reducing cluster in main game flow 

- This method manages:

- Correct and incorrect guesses

- Streak bonuses

- Risk Mode multipliers

- ACE bonus handling

## Card Hunt(Alternative Game)
As an extension task an alternative game mode was implemenented called Card Hunt

This game utilises the same card and deck classes but applies them in a different variation

### Game Overview
 - Cards are dealt onto a 3x3 grid
 - Each cell is numbered and hidden from player
 - The player is shown a card description:
    - Value
    - Suit
- Correct guesses reveal the card and incorrect guesses reduce player lives
- The game loops until there are no more cards in the deck remaining to fill the grid   

The reason for developing this game mode demonstrated:
- Reuse of existing systems without duplication and memory efficency
- An innovative style of problem solving and user interaction

## Key Methods for Card Hunt Class

### populate_grid()

This method ensures that a round only starts when enough valid cards remain, preventing partial or invalid grids.

Skipping Joker cards here avoids introducing special cases into the guessing logic.

### new_round()

This method separates round progression from overall game lifecycle management.

- Controls round progression:

- Shuffles remaining cards

- Deals a new grid

- Handles player guesses

- Determines when to move to the next round or end the game

Implementing this method ,it was important to separate and design cleanly the round logic from the game lifecycle logic 

## Use of Enums

Enums were used because card suits, values, and types are fixed sets of valid options, and using Enums improves readability, safety, and consistency compared to variables or dictionaries.

## Future Improvements

 #### Graphical User Interface (GUI)
Implement a simple Tkinter-based GUI to improve usability. The existing separation between the game logic and CLI would allow the current models and rules to be reused with minimal changes.

#### Game State Logging
Add support for saving and loading game state so players can resume sessions, further testing the robustness of the game model.


# How to Run
Run the project from the in command line:
   ```
   python main.py 