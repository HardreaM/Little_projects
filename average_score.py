#Average score

import os

def Main():
	five = 	int(input('Пятерки: '))
	four = 	int(input('Четверки: '))
	three = int(input('Тройки: '))
	two = 	int(input('Двойки: '))

	return (five*5 + four*4 + three*3 + two*2)/(five + four + three + two)

while True:
	try:
		os.system('cls')
		print(Main())
		input()
		
	except ValueError:
		continue

	except KeyboardInterrupt:
		os.system('cls')
		exit()