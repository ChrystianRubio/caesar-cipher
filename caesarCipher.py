import sys


print('Origin: ' + sys.argv[1])

decript = ''
rotation = int(input('Rotation: '))


for x in range(0, len(sys.argv[1])):

	if sys.argv[1][x].isalpha():
		if sys.argv[2] == '-e' : 
			decript += chr(ord(sys.argv[1][x]) + rotation)
	

	
		elif sys.argv[2] == '-d':
			decript += chr(ord(sys.argv[1][x]) - rotation)
	

	else:
		decript += sys.argv[1][x]



	if x == (len(sys.argv[1]) - 1 ):
	
		print(f"Decrypt: {decript}")


