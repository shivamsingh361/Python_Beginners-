import random
from words import words
import string

def get_valid_word(words):
	word = random.choice(words) #randomly chooses word
	while '-' in word or ' ' in word:
		word = random.choice(words)
	print('In get_valid_word method',word)
	return word

def hangman():
	word = get_valid_word(words)
	print('in hangman method', word)
	word_letters = set(word) #storing the letters of word which is randomly choosen as set
	print(word_letters)

	# alphabet = set(string.ascii_uppercase) #storing all 26 alphabet in uppercase
	# used_letters = set() #what user has entered

	while len(word_letters) > 0: #iterate untill length of letters > 0

		#letters used 
		print ('You have used these letters ', ' '.join(used_letters))

		print ('used letters set',used_letters)
		#current status of word
		
		word_list = [letter if letter in used_letters else '-' for letter in word]
		print('Current Word status: ', ' '.join(word_list))
		#getting user input
		user_letter = input('Guess a letter: ').upper()

		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if used_letters in word_letters:
				word_letters.remove(used_letters)

		elif user_letter in used_letters:
			print('You have already used that character')

		else:
			print('Invalid character')



hangman();