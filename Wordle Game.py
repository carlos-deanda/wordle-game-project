"""
Wordle
Andres Tellez Bermudez A01640907
Carlos Felipe De Anda Gallardo A01640711
Maximiliano Villegas Ruiz A01640966
"""

import random
from colorama import Fore

""" Function 1: In this function we open a file with the words and arrange them by rows because we separate them in the excel by 
How many letters they have, then we use a for that so we can separate them """

def words():       
    f = open("Words.csv","r", encoding= "UTF-8")   
    lista = []
    for row in f:
        lista.append(row)
    f.close()
    words = []
    for elementos in lista:
        words.append(elementos.lower().strip().split(",")) 
    return words

""" Function 2: In this function we ask the user of how many letters he wants to guess and with that we use a while true so he can put from 4 to 8 
else it will put an error that says that isnt an option, then it will break the while and follow so with the library random 
So we can choose the letter in the matriz, We then create a list and add each character the letter has and return that list"""

def letters(matrix):    
    size = int(input("Of how many letters do you want your word? (It can be min. 4, max, 8): "))
    while True:
        if size < 4 or size > 8:
            size = int(input("Sorry that is not an available option, please try again: "))   
        else:
            break
    n_column = random.randint(0,len(matrix[size-4])-1)
    word = matrix[size-4][n_column]
    word_list = []
    for char in word:
        word_list.append(char)
    return word_list 
"""Function 3: This is the function of the game and this is just simple as we do an input for the word and then use a while to see if its 
the same lenght as the secret_word and if it is we use a break to that while and we use lower() and strip() to check each of the letters
here we have a library name FORE that can change the color of the letters and print it then if you got the secret world it prints yay you got 
it and asks for your name so we can add it to the hall of fame
"""
def game(secret_word):            
    print("You have 6 attempts to guess the word: ")
    game_over = 0
    for x in range(6):
        checker = len(secret_word)*[0]
        attempt1 = []
        attempt = input()
        
        
        letterCounter = {}
        #I create a dictionary "letterCounter" to have control of the letters
        for letter in secret_word:
            if letter in letterCounter:
                letterCounter[letter] += 1
            else:
                letterCounter[letter] = 1

        """"This is a loop if the user enters incorrect number of letters"""
        
        while True:         
            if len(attempt) != len(secret_word):
                attempt = (input("Sorry, incorrect lenght, try again: "))
            else:
                break
        attempt = attempt.lower()
        attempt = attempt.strip()
        for char in attempt:
            attempt1.append(char)
        
        """First we check for green"""
        
        for x in range(len(secret_word)):  # x represents the letter in my attempt
            if attempt1[x] == secret_word[x]:
                letterCounter[attempt1[x]] -= 1

        
        
        for x in range(len(secret_word)):
            if attempt1[x] in letterCounter:  #if letter is in word
                if attempt1[x] == secret_word[x]: #if letter is in correct position in word
                    print(f"{Fore.GREEN}{attempt1[x]}{Fore.RESET}", end="")
                elif letterCounter[attempt1[x]] > 0 and attempt1[x] != secret_word[x]:  #if letter in word but in incorrect position
                    letterCounter[attempt1[x]] -= 1
                    print(f"{Fore.YELLOW}{attempt1[x]}{Fore.RESET}", end="")
                else:  #if a letter that is in the word is already guessed in correctly (so that it prints gray)
                    print(f"{Fore.RESET}{attempt1[x]}", end="")
                    
            else:
                print(f"{Fore.RESET}{attempt1[x]}", end="")  

        """If the player wins, the game ends"""
        if attempt1 == secret_word:  
            print()
            print(f"{Fore.RESET} Congrats!!!, you've got the secret word")
            game_over += 1
            break
        print()
    """if the player loses"""
    if game_over == 0:    
        secret = "".join(secret_word)    
        print(f"{Fore.RESET}Sorry, the correct word was '{secret}', maybe next time")
    
   
    return game_over

"""Now In this function we just ask for your name and add it with the word you find to the hall of fame"""

def greatest_table(greatest, word):
    name = input("Welcome to the hall of fame. You are now one of the greatest of the greatest, what is your name? ")
    lista = [name, word]
    greatest.append(lista)
    print(F"{Fore.GREEN}Greatest -------- Word{Fore.RESET}")
    print("-----------------------")
    for x in greatest:
        print(f"{Fore.BLUE}{x[0]}{Fore.RESET} -------- {Fore.YELLOW}{x[1]}{Fore.RESET}")
    
    
    outfile = open("HallFame.txt", "a")
    outfile.write(f"\n{name}\t\t{word}")   
    
    return greatest
    
"""This is just the menu were all its happening
""" 
def menu1(greatest): 
    menu = int(input("Do you want to play? 1. Yes 2. No : "))
    while menu < 1 or menu > 2:
        menu = int(input("Sorry, that is not an available option, please try again: "))
    if menu == 1:    
        matrix_words = words()   
        secret_word = letters(matrix_words)  
        win = game(secret_word)         
        secret_word = "".join(secret_word)
        if win == 1:  
            greatest = greatest_table(greatest, secret_word) 
        menu1(greatest)
        
    else:
        print("Have a Nice Day!!!")         

"""Here is main were you only create the list for the name of the greatest and print the instructions"""

def main():
    greatest = []
    print("""Welcome to the Wordle game, the game consists of guessing the secret word, you only have 6 attempts, Good Luck!!
            Green = Correct position
            Yellow = incorrect position but the word has that letter
            Gray = It doesn't have that letter""")
    menu1(greatest)
main()

