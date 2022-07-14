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
	data = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)? '))
	# This is the fist data inputted
	if data == QUIT:
		print('No temperatures were entered')
	else:
		# The first data is highest, lowest and cool, because only one data
		highest = data
		lowest = data
		cool = data
		if cool < 16:
			cool = 1
		else:
			cool = 0
	# Started to compare data will be bigger or smaller then fist data
		total = data
		n = 1				# Counter to count how many data inputted
		while True:
			data = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)? '))
			if data == QUIT:
				break
			n += 1					
			if data > highest:
				highest = data
			if data < lowest:
				lowest = data
			if data < 16:
				cool += 1
			total += data

		print('Highest Temperature = ' + str(highest))
		print('Lowest Temperature = ' + str(lowest))

		average = (total/n)
		print('Average = ' + str(average))

		print(str(cool) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
