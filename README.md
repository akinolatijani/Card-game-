# GAME : Higher/Lower 

## Project Scope 

This project involved building a CLI-based Higher / Lower card game using Python.
The game uses a standard deck of 52 cards with the addition of 2 Joker cards. The player is shown a card and must guess whether the next card drawn will be higher or lower.

The main goal of this project was not just to make the game work, but to design it in a clean, structured way that is easy to understand, maintain, and extend.

## Design Decisons 

Structure of code used 
This game was implemented in Object Orientated Programming ,due to the order that allows the mapping of the deck of cards as Objects and it attributes and methods within the deck

OOP in this project would:
- Reduced repetition when handling cards and the deck
- Clear separation between game logic and card logic
- Easier debugging and future improvements
- Better organisation as the project grew in complexity

For implementation the game was setup with classes with its own set of responsiblities.

## CLass Structure: 

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
- Shuffle the deck
- Safely draw cards from the deck

Separating deck logic into its own class follows the single responsibility principle, ensuring that the deck only manages cards and nothing else.


### HigherLower Class 

The 'HigherLower' class is where the main game functionality takes place .

Manages:
- Game flow
- Player input
- Scoring and lives
- Streak and bonus logic
- Win and lose conditions

This class component was key for game rules and logic 

### Method chosen for HigherLower Game Class

#### Pick_new_card() 
This function was key ensuring the joker cards were handled consistently 

#### make_a_guess() 
 Would act as the core game loop for each round when called, handling:
     User input
     Card comparison
     Special cases(Joker card , Stalemate) 

#### check_guess()
 Reason for a seperate method was to isolate penalty logic ,making it easy to manage streaks,risk mode, bonuses ,reducing cluster in main game flow 

## Use of Enums
Enums were used because card suits, values, and types are fixed sets of valid options, and using Enums improves readability, safety, and consistency compared to variables or dictionaries.



