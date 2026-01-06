# Higher/Lower Card Game

## Project Scope 

This project is a command-line implementation of a Higher / Lower card game written in Python.
The game uses a standard 52-card deck with the addition of two Joker cards. At the start of each round, the player is shown a card and must guess whether the next card drawn will be higher or lower in value.

While the game mechanics themselves are intentionally simple, the main focus of this project was on clean design, structure, and extensibility, rather than just making the game functional.

## Design Decisons 

- The core requirements of the project included:

- Modelling a standard deck of cards

- Implementing shuffling and safe card drawing

- Defining clear game rules

- Building a playable CLI interface

Beyond the base requirements, several additional features were added to improve gameplay and demonstrate design thinking, such as Joker cards, Risk Mode, streak bonuses, and a more polished user interface.

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


### HigherLower Class 
The HigherLower class contains the core game logic

Manages:
- Game flow

- Handling player input

- Scoring and lives

- Streak and bonus logic

- Determining Win and lose conditions

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

## Use of Enums
Enums were used because card suits, values, and types are fixed sets of valid options, and using Enums improves readability, safety, and consistency compared to variables or dictionaries.


# HOW TO RUN 
Run in command line:
             python higherLower