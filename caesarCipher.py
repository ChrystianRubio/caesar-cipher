import sys

#set rotation 
#set numbers or not in decrypt

print('Origin: ' + sys.argv[1])

decript = ''

for x in range(0, len(sys.argv[1])):

	if sys.argv[2] == '-e':
		decript += chr(ord(sys.argv[1][x]) + 3)
	

#		if x == (len(sys.argv[1]) -1 ):
	
#			print(f"Decrypt: {decript}")
	elif sys.argv[2] == '-d':
		decript += chr(ord(sys.argv[1][x]) - 3)
	

	if x == (len(sys.argv[1]) -1 ):
	
		print(f"Decrypt: {decript}")


