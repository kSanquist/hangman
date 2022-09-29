# HANGMAN
A command-line hangman game with fancy ascii art

## What You'll Find
### ascii_art.py
  - Used to store the ascii art elements in the game i.e. the title, the letters, win and lose screens
### phrases.py
  - Used to store the various phrases ranging in difficulity from 1 to 3
### main.py
  - Where the magic happens. All the code that runs the game is here

## ASCII_ART.PY
### Ascii elements:
  - ascii alphabet including a blank space for unguessed letters
  - a you lose graphic
  - a you win graphic

## PHRASES.PY
### Phrase difficulty Examples:
  - lvl 1: 'pepper', 'midnight', 'legendary'
  - lvl 2: 'i call bullshit', 'excellent specimen', 'no shit sherlock'
  - lvl 3: 'razzmatazz', 'antidisestablishmentarianism', 'pneumonoultramicroscopicsilicovolcanoconiosis'
### Methods:
  - get_random_phrase_idx() : returns the index random phrase from the list associated with the provided difficulty
  - get_random_phrase() : uses idex given by get_random_phrase_idx() to return a random phrase

## MAIN.PY
 - Allows users to guess both letters and words
 - Handles the logic for inputting letters and words, and verifying if they're correct
 - If you guess 5 letters or words wrong, the hangman is complete and you lose, guess the word and you win
 - Logic prevents users from entering non-alpha values or repeating a guess more than once
 - Uses ascii elements from ascii_art.py to paint the game's graphics (it might be command-line but it's pretty nice)
