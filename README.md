# Higher/Lower Card Game

## Project Scope 

It was originally designed as a Higher / Lower card game, but was later extended with an alternative game mode to demonstrate flexibility, reuse of core logic, and design thinking.

The project uses a standard 52-card deck with the addition of two Joker cards.
Both games are played entirely in the terminal using a text-based user interface, with an emphasis on clean structure, extensibility, and readable output rather than graphical complexity.

The goal of this project was not only to meet the functional requirements, but also to show thoughtful software design, particularly around object-oriented programming, separation of concerns, and future scalability.

## Design Decisons 

- The core requirements of the project included:

- Modelling a standard deck of cards

- Implementing shuffling and safe card drawing

- Defining clear game rules

- Building a playable CLI interface

Beyond these requirements, the project was extended to include:

- Two Joker cards with special handling

- A reusable deck and card model shared across multiple games

- A second game mode (Card Hunt) using the same card and deck logic

- A structured UI layer to separate presentation from game logic

OOP in this project would:
- Reduced repetition when handling cards and the deck

- Clear separation between game logic and card logic

- Easier debugging and future improvements

- Better organisation as the project grew in complexity

For implementation the game was setup with classes with its own set of responsiblities.

## OOP(Object- Orientated Programming) Approach

The project was implemented using Object-Oriented Programming (OOP). This approach was chosen because it maps naturally to the domain of a card game, where cards, decks, and the game itself each have distinct responsibilities.

Using OOP allowed the project to:

- Reduce repetition when handling cards and decks

- Keep card logic separate from game rules

- Make the code easier to debug and reason about

- Support additional features without major refactoring


## Class Structure: 

### Cards Class
This class was developed for representing single playing card e.g 5 of Spades

The Cards holds:
- A suit 
- A vaue 
- Card Type (e.g. Normal or Joker Card)

This highlights the suitabilty of OOP as it allowed the storage of the attributes within the class 
Any card logic would be maintained within one place .

### Deck_of_cards Class

The class represents the full deck of 52 cards in the game 

Responsibilities:
- Create a standard 52-card deck

- Add 2 Joker cards

- Shuffling the deck

- Safely draw cards from the deck

Separating deck logic into its own class ensures that the game logic does not directly manipulate card collections, which helps prevent invalid states and simplifies future extensions.

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

This function was key ensuring the joker cards were handled consistently 

### make_a_guess() 

This method represents a single round of gameplay and acts as the main game loop step.
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

Builds a grid using remaining cards from the deck while skipping Joker cards.
Ensures that a new round only starts if enough cards are available.

### new_round()

- Controls round progression:

- Shuffles remaining cards

- Deals a new grid

- Handles player guesses

- Determines when to move to the next round or end the game

Implementing this method ,it was important to separate and design cleanly the round logic from the game lifecycle logic 

## Use of Enums

Enums were used because card suits, values, and types are fixed sets of valid options, and using Enums improves readability, safety, and consistency compared to variables or dictionaries.


# How to Run
Run the project from the in command line:
   ```
   python main.py 