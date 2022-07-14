"""
File: boggle.py
Name: Leticia Chen
----------------------------------------
Boggle game is a wya to string together letters given by game,
Player shall choose the first letter to start the game,
Base on the first letter, to find its neighbor letters,
At the same time, player shall choose a letter from neighbor letters, and it will be string together
To repeat: choose one from neighbor-->string together this one-->find this one´s neighbor.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
# Dictionary to store all words from FILE
word_dict = {'part1': {}, 'part2': {}}


def main():
	"""
	To string together alphabets within 16 letters and to switch them with words form a dictionary list
	"""
	# read FILE file and put words into dictionary
	read_dictionary()

	print('Please input 4 letters and separated by space!')
	# Letters_list = ['fycl', 'iomg', 'oril', 'hjhu']
	letters_list = input_letters()

	start = time.time()
	# To get total number of words find in dictionary
	count = []
	# Shall assign a letter to start game, using it to find its neighbor
	for x in range(len(letters_list)):
		for y in range(len(letters_list[x])):
			ch = letters_list[x][y]
			helper(letters_list, x, y, ch, [(x, y)], [], count)
	print("There are " + str(sum(count)) + " words in total!")
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def helper(letters, x, y, new_word, i_number, result, count):
	"""
	After get starting alphabet, shall to find its neighbor alphabet
	And get the fist available alphabet (cannot repeat alphabet if they have the same index)
	Then to find its neighbor...same way continue
	:param letters: (list), a dictionary of words
	:param x: (int), index of list of inputted alphabet
	:param y: (int), index of string of alphabet which are in a list
	:param new_word: (string), to get a alphabet form input list
	:param i_number: (list), elements are Tuple (x, y), index of alphabets
	:param result: (list), elements are words switched in dictionary by alphabets boggle game
	:param count: (int), total number of words in result list
	:return: (int), count
	"""
	global word_dict
	if len(new_word) >= 4:										# Only vocabulary more than 4 letters
		if new_word[0] <= 'm':									# To short searching time, searching 'a' to 'm'
			if new_word[0] in word_dict['part1']:				# If letter is in part1 dictionary´s "key" (key-value)
				# if new_word is in new_word[0]´s "value" list (key-value)
				if new_word in word_dict['part1'][new_word[0]] and new_word not in result:
					result.append(new_word)
					count.append(1)
					print('Found: ' + new_word)
		else:
			if new_word[0] in word_dict['part2']:
				if new_word in word_dict['part2'][new_word[0]] and new_word not in result:
					result.append(new_word)
					count.append(1)
					print('Found: ' + new_word)

	# Recursion--> to find assign (x, y)´s neighbor alphabets
	if has_prefix(new_word):
		for i in range(-1, 2, 1):							# (start, end, step)to find starting letter´s neighbor letter
			for j in range(-1, 2, 1):
				l_index = x + i								# Alphabet in list´s index
				s_index = y + j								# Alphabet is sting´s index
				if 0 <= l_index < len(letters):				# List len
					if 0 <= s_index < len(letters[x]):		# String len
						ch = letters[l_index][s_index]
						index_inf = (l_index, s_index)  	# Get ch´s index (is Tuple)
						if index_inf in i_number:			# if ch´s index exist in i_number list, meaning duplicated alphabet
							pass
						else:
							# choose
							new_word += ch					# add new alphabet to new_word string
							i_number.append(index_inf)		# add new alphabet´s index to i_number list
							# explore
							helper(letters, l_index, s_index, new_word, i_number, result, count)
							# un-choose
							new_word = new_word[0:len(new_word) - 1]
							i_number.pop()
							l_index -= i
							s_index -= j


def input_letters():
	"""
	Input alphabets: fycl, iomg, oril, hjhu, between alphabets shall be separated by space
	:return: list type, list of alphabets inputted without space between alphabets
	"""
	letters_list = []												# To store input alphabets
	for i in range(1, 5):											# Input letters, total 4 rows strings letters
		while True:
			s = input(str(i) + ' row of letters: ')					# i is index of row

			illegal = False
			for j in range(1, len(s), 2):							# j is space´s index 1, 3, 5,...
				if s[j] != " ":										# If has space between letters
					print('Illegal input!')
					illegal = True
					break

			if not illegal:											# User input alphabets with space
				n_s = ""
				for j in range(len(s)):
					if s[j].isalpha():
						n_s += s[j]
				n_s = n_s.lower()
				letters_list.append(n_s)
				break
	return letters_list


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global word_dict
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip()
			if word[0] <= 'm':											# word_dict divided into 2 keys: part1 and part2
				if word[0] not in word_dict['part1']:					# part1 is a dictionary, word[0] is its key
					word_dict['part1'][word[0]] = [word]				# part1 divided into "a" to "m" keys to store words
				else:
					word_dict['part1'][word[0]].append(word)
			else:
				if word[0] not in word_dict['part2']:
					word_dict['part2'][word[0]] = [word]				# part2 divided into "n" to "z" keys to store words
				else:
					word_dict['part2'][word[0]].append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global word_dict
	if sub_s[0] <= 'm':
		if sub_s[0] in word_dict['part1']:								# sub_[0] is key of dictionary 'part1'
			for word in word_dict['part1'][sub_s[0]]:					# word is 'value' in dictionary 'part1'
				if word.startswith(sub_s):
					return True
			return False
	else:
		if sub_s[0] in word_dict['part2']:
			for word in word_dict['part2'][sub_s[0]]:
				if word.startswith(sub_s):
					return True
			return False


if __name__ == '__main__':
	main()
