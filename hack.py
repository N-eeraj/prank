import time
import os
from termcolor import colored

try:
	print('\n\nPreparing to hack')
	print('Starting\n', end = '')

	for i in range(0, 101):
		if i % 25 or 90<i<95: #speeding up
			time.sleep(i / 250)
		else:
			time.sleep(i / 150) #loading speed
		if i == 100:
			time.sleep(7) #wait at 99%
		os.system('clear')
		if i % 10 == 0: # update at every 10s
			j = i
		if i > 94: #show % after 94
			j = i
		print(colored('\nBypassing Security.\n' + str(j) + '%\n\n', 'cyan'), end = '\n')
		print('\033[0;32;42m \033[0;37;40m' * int(4  * i / 3)) #green space for loading

	time.sleep(1)
	os.system('clear')
	print('\n' * 10 + 'Hacking Succesfull\n\n')

	for i in range(0, 101):
		time.sleep(i / 200) #loading speed
		if i == 100:
			time.sleep(5) #wait at 99%
		os.system('clear')
		print(colored('\n\n\n\nDecrypting Files.\n' + str(i) + '%\n\n', 'cyan'), end = '\n')

	time.sleep(1)
	os.system('clear')
	print('Decryption Successful\n\n')
	print('Reading files\n')
	time.sleep(1.25)
	print('\n' * 10 + 'Thank You for your time :p\n\n')

except KeyboardInterrupt:
	print(colored('Error\t' * int(i ** 2)  + '\n\nAborted', 'red')) #print error, lots of errors
