import random
word_list = ["Monopoly", "Ajedrez", "Checkers", "Domino", "Solitario", "Clue", "Candy Land", "Operation", "Guess Who", "Uno"]
def display_hangman(tries):
    stages = ["""
                    --------
                    |       |
                    |       O
                    |      /|\\
                    |       |
                    |      /|\\ 
                    |
                    -
                    """
                       ,
                    """
                    --------
                    |       |
                    |       O
                    |      /|\\ 
                    |       |
                    |      /| 
                    -
                    """
                       ,
                    """ 
                     --------
                    |       |
                    |       O
                    |      /|\\ 
                    |       |
                    |        
                    -
                    """
                       ,
                    """ 
                    --------
                    |       |
                    |       O
                    |      /| 
                    |       |
                    |       
                    -
                    """
                       ,
                    """ 
                    --------
                    |       |
                    |       O
                    |       |
                    |       |
                    |       
                    -
                    """
                       ,
                    """ 
                    --------
                    |       |
                    |       O
                    |       
                    |       
                    |      
                    -
                    """
                       ,
                    """
                    --------
                    |       |
                    |       
                    |       
                    |       
                    |       
                    -
                    """
                    ]