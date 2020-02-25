import random

def pick_random_word():
    """Returns a random word from a list of predefined options"""
    word_list = ['PYTHON', 'PUMPKIN', 'QUEEN', 'ISTANBUL', 'PENINSULA', 'ARCHIPELAGO', 'COFFEE', 'ADDICTION', 'CHARISMA', 'KUCU']
    # Return random integer in range [a, b], including both end points.
    # random_index = random.randint(a, b)
    random_index = random.randint(0, len(word_list)-1)
    return word_list[random_index]
    
def input_guess_letter():
  """Takes and returns guess letter from user. Continues to ask for new letter if user enters invalid letter (length != 1)."""
  ## Your code starts here

   ## Your code ends here
    
    
def update_display_string(correct_word, display_string, guess_letter):
  """ Do stuff """
  ## Your code starts here

  ## Your code ends here

lives = 6
random_word = pick_random_word()
display_string = '_' * len(random_word)
print(f'Welcome to Hangman! You have {lives} lives to correctly guess the word.')

#Time to use functions and implement the game!