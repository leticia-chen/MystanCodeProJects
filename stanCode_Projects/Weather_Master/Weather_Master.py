"""
File: weather_master.py
Name: Leticia Chen
-----------------------
This program will register weather data inputted by user
Will compute and show the average, highest, lowest,
how many day are cold days among the inputs.

"""

"""
This number controls when to stop the program
"""
QUIT = 100


def main():
	"""
	User will input temperature and will be registered.
	Finished temperature input, program show highest, lowest, average temperature,
	and cold days less than 16 degree.
	"""

	print('StanCode \"Weather Master 4.0\"!')
	prompt = f'Next Temperature: (or {QUIT} to quit)? '

	while True:
		try:
			data = int(input(prompt))
			break
		except ValueError:
			print('Invalid input. Please enter a valid integer.')

	# This is the fist data inputted
	if data == QUIT:
		print('No temperatures were entered')
	else:
		# Initialize values with the first data input
		highest = lowest = data
		cool = 0
		if data < 16:
			cool += 1
		total = data
		# Counter to count how many data inputted
		count = 1

		while True:
			try:
				data = int(input(prompt))
			except ValueError:
				print('Invalid input. Please enter a valid integer.')
				continue

			if data == QUIT:
				break
			if data > highest:
				highest = data
			if data < lowest:
				lowest = data
			if data < 16:
				cool += 1

			total += data
			count += 1

		print('Highest Temperature = ' + str(highest))
		print('Lowest Temperature = ' + str(lowest))

		average = (total/count)
		print('Average = ' + str(average))

		print(str(cool) + ' cold day(s)')


if __name__ == "__main__":
	main()


if __name__ == "__main__":
	main()
