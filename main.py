# Hangman game
# Kyle Sanquist

from os import name, system
import os
from time import sleep
import ascii_art as aa
from pynput.keyboard import Key, Listener
from phrases import get_random_phrase


stickman_5 = [
'    ---------',
'    |       |',
'    |       |',
'    |      ===',
'    |     =   =',
'    |      ===',
'    |       =',
'    |     =====',
'    |       =',
'    |      = =', 
'    |     =   =',
'    |          ',
'    |          ',
'-----------------'
]
stickman_4 = [
'    ---------',
'    |       |',
'    |       |',
'    |      ===',
'    |     =   =',
'    |      ===',
'    |       =',
'    |     =====',
'    |       =',
'    |      = ', 
'    |     =   ',
'    |          ',
'    |          ',
'-----------------'
] 
stickman_3 = [
'    ---------',
'    |       |',
'    |       |',
'    |      ===',
'    |     =   =',
'    |      ===',
'    |       =',
'    |     =====',
'    |       =',
'    |      ', 
'    |        ',
'    |          ',
'    |          ',
'-----------------'
]
stickman_2 = [
'    ---------',
'    |       |',
'    |       |',
'    |      ===',
'    |     =   =',
'    |      ===',
'    |       =',
'    |       =',
'    |       =',
'    |      ', 
'    |       ',
'    |          ',
'    |          ',
'-----------------'    
]
stickman_1 = [
'    ---------',
'    |       |',
'    |       |',
'    |      ===',
'    |     =   =',
'    |      ===',
'    |       ',
'    |       ',
'    |       ',
'    |      ', 
'    |       ',
'    |          ',
'    |          ',
'-----------------'    
]
stickman_0 = [
'    ---------',
'    |       |',
'    |       |',
'    |      ',
'    |     ',
'    |      ',
'    |       ',
'    |       ',
'    |       ',
'    |      ', 
'    |       ',
'    |          ',
'    |          ',
'-----------------'   
]


# Clears screen
def clear():
    if name == 'nt': system('cls') 
    else: system('clear')


# A 2D Array of blank lines
def format_phrase():
    blank_phrase_words = []
    blank_letter = aa.blank
    for word in phrase_words:
        blank_phrase_word = []
        for letter in word:
            blank_phrase_word.append(blank_letter)
        blank_phrase_words.append(blank_phrase_word) 
    return blank_phrase_words

def main():
    clear()
    paint_game(0)


# Paints the stickman, wrong letters, and phrase
def paint_game(stage):
    paint_stickman(stage)
    paint_wrong_letters(wrong_letters)
    paint_guess_phrase(guess_phrase_words)
    if len(wrong_letters) == 5:
        display_loss()
    elif has_won():
        display_win()
    else:
        get_guess()


# Runs based on key press
def enter_esc_key_pressed(key):
    if key == Key.enter:
        print(' '*25 + 'Restarting...')
        sleep(0.5)
        clear()
        system('python main.py')
    if key == Key.esc:
        print(' '*24 + 'Exiting Game...\n')
        sleep(0.5)
        os._exit(0)


# Checks to see if player has won through list containing correct letters
def has_won():
    has_won = True
    for word in correct_guessed_letters:
        if 'O' in word:
            has_won = False
            break
    return has_won
    

# Win screen
def display_win():
    print('\n' + '-'*65)
    print(aa.you_won)
    print('                ENTER : PLAY AGAIN / ESC : QUIT')
    
    with Listener(on_press = enter_esc_key_pressed) as listener:
        listener.join()


# Lose screen
def display_loss():
    print('\n')
    print(aa.you_lose)
    center = int(32-((len(phrase)+16)/2))  # Centers phrase text under aa.you_lose
    print(' ' * center + f'The Phrase was: {phrase.upper()}\n')
    print('                ENTER : PLAY AGAIN / ESC : QUIT')
    
    with Listener(on_press = enter_esc_key_pressed) as listener:
        listener.join()


# Gets user guess, makes sure it meets criteria
def get_guess():
    guess = input('GUESS: ')
    is_alpha_not_guessed = (guess.isalpha()) and (guess not in guessed_letters)
    if len(guess) == 1 and is_alpha_not_guessed:
        evaluate_letter(guess.lower())
    elif len(guess) > 1 and is_alpha_not_guessed:
        evaluate_word(guess.lower())
    else:
        get_guess()
    clear()
    paint_game(len(wrong_letters))


# Retrieves the key, value pairs of letter instances
# instances[word] = [letter, idx, ..., idx]
def get_letter_instances(letter_guess):
    instances = {}
    for word_idx,word in enumerate(phrase_words):
        for letter_idx,letter in enumerate(word):
            if letter_guess == letter:
                if word in instances: 
                    instances[word].append(letter_idx)
                    instances[word][1].append(word_idx)
                else: 
                    instances[word] = [letter, letter_idx]
                    instances[word].insert(1, [word_idx])
    return instances

# Search to see if letter is in phrase
# If yes : grab which word and index it's in through phrase_words and repaint guess_phrase
# If no : repaint stick figure and wrong letters
def evaluate_letter(letter_guess):
    guessed_letters.append(letter_guess)
    if phrase.count(letter_guess) == 0:
        update_wrong_letters(letter_guess)
    else:
        instances = get_letter_instances(letter_guess)
        for instance_key in instances.keys():
            idxs = []
            word_idxs = instances[instance_key][1]
            for word_idx in word_idxs:
                for i in range(2, len(instances[instance_key])):
                    idxs.append(instances[instance_key][i])
                for idx in idxs:
                    letter = instances[instance_key][0]
                    guess_phrase_words[word_idx][idx] = get_letter(letter)
                    correct_guessed_letters[word_idx][idx] = 'X'


# Converts text letter to class letter
def get_letter(letter):
    if letter == 'a': return aa.A
    elif letter == 'b': return aa.B
    elif letter == 'c': return aa.C
    elif letter == 'd': return aa.D
    elif letter == 'e': return aa.E
    elif letter == 'f': return aa.F
    elif letter == 'g': return aa.G
    elif letter == 'h': return aa.H
    elif letter == 'i': return aa.I
    elif letter == 'j': return aa.J
    elif letter == 'k': return aa.K
    elif letter == 'l': return aa.L
    elif letter == 'm': return aa.M
    elif letter == 'n': return aa.N
    elif letter == 'o': return aa.O
    elif letter == 'p': return aa.P
    elif letter == 'q': return aa.Q
    elif letter == 'r': return aa.R
    elif letter == 's': return aa.S
    elif letter == 't': return aa.T
    elif letter == 'u': return aa.U
    elif letter == 'v': return aa.V
    elif letter == 'w': return aa.W
    elif letter == 'x': return aa.X
    elif letter == 'y': return aa.Y
    elif letter == 'z': return aa.Z


# Updates wrong letters
def update_wrong_letters(letter):
    clear()
    wrong_letters.append(letter)
    paint_game(len(wrong_letters))


# returns every instance of a word
def get_word_instances(word_guess):
    instances = {}
    for idx,word in enumerate(phrase_words):
        if word in instances: instances[word].append(idx)
        else: instances[word] = [idx]
    return instances
        

# Converts letters to classes in order to add them to guess_phrase
def convert_letters_to_classes(word_guess):
    word_guess_letters = list(word_guess)
    word_guess_letter_classes = []
    for letter in word_guess_letters:
        word_guess_letter_classes.append(get_letter(letter))
    return word_guess_letter_classes


# Search to see if word is in phrase
# If yes : grab which index it's at through phrase_words
# If no : repaint stick figure
def evaluate_word(word_guess):
    if word_guess not in phrase_words: 
        update_wrong_letters(word_guess)
    else:
        instances = get_word_instances(word_guess)
        word_guess_letter_classes = convert_letters_to_classes(word_guess)
        for idx in instances[word_guess]:
            for i in range(0, len(word_guess)):
                guess_phrase_words[idx][i] = word_guess_letter_classes[i]
                correct_guessed_letters[idx][i] = word_guess_letter_classes[i]
        for letter in word_guess:
            evaluate_letter(letter)        

# Prints phrase
def paint_guess_phrase(guess_phrase):
    for idx,sentence in enumerate(guess_phrase):
        print()
        for i in range(0,4):
            row = [item[i] for item in sentence]
            for item in row:
                print(item, end='  ')
            print()
    print('\n')


# Prints wrong
def paint_wrong_letters(wrong_letters):
    sleep(0.08)
    print('WRONG |', end=' ', flush=True)
    sleep(0.1)
    for letter in wrong_letters:
        sleep(0.1)
        print(letter.upper(), end=' ', flush=True)


# prints stickman on screen
def paint_stickman(stage):
    if stage == 0: 
        for row in stickman_0: 
            sleep(0.08) 
            print(row)
    elif stage == 1:
        for row in stickman_1: 
            sleep(0.08) 
            print(row)
    elif stage == 2:
        for row in stickman_2: 
            sleep(0.08) 
            print(row)
    elif stage == 3:
        for row in stickman_3: 
            sleep(0.08) 
            print(row)
    elif stage == 4:
        for row in stickman_4: 
            sleep(0.08) 
            print(row)
    else:
        for row in stickman_5: 
            sleep(0.08) 
            print(row)


# Title Screen
def intro():
    print('''\
                         KYLE SANQUIST'S

██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝''')
    
    while True:
        try:
            difficulty = int(input('                   PHRASE DIFFICULTY (1-3): '))
        except ValueError:
            continue
        
        if difficulty > 3 or difficulty < 1: 
            pass
        else: 
            return get_random_phrase(difficulty)


if __name__ == '__main__':
    phrase = intro()
    phrase_words = phrase.split()
    wrong_letters = []
    guessed_letters = []
    guess_phrase_words = format_phrase()
    correct_guessed_letters = []

    for word in phrase_words: correct_guessed_letters.append([])
    for idx, word in enumerate(phrase_words):
        for letter in word:
            correct_guessed_letters[idx].append('O')
    
    clear()
    main()