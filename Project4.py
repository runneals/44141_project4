# This link may help you: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

# Define Variables that are used throughout the program:
str1 = [] #DNA Strand 1 List
str2 = [] #DNA Strand 2 List
strand1 = "" #After it is input, it is used throughout the program to print strand 1
strand2 = "" #After it is input, it is used throughout the program to print strand 1
count = 0 #Iterator Count
position = 0 #Position (input)
strand = 0 #Strand Number (input)

# Get DNA Strands input as strings
strand1 = str(input("Enter DNA Strand 1: "))
strand2 = str(input("Enter DNA Strand 2: "))

# Force DNA strands to lowercase
strand1 = strand1.lower()
strand2 = strand2.lower()

# Convert strand strings to str Lists
for n in strand1:
	str1.append(strand1[count])
	count += 1
count = 0
for n in strand2:
	str2.append(strand2[count])
	count += 1

# Get Initial menu command
menu = str(input("\nCommand Menu:  (a)dd indel  ~~  (d)elete indel  ~~  (s)core  ~~  (q)uit\nEnter a Command: "))

#Menu Loop
while menu != 'q':
	if menu == 'a': # Add Indel Module
		# Get user input
		strand = int(input("Which Strand to work on (1 or 2): "))
		position = int(input("Before which index to place the indel (start at 0): "))
		
		# If strand # and position < strand length
		if strand == 1 and position <= len(str1): #check if strand is 1 & position < length
			str1.insert(position, '-') #add indel

		elif strand == 2 and position <= len(str2): #check if strand is 2 & position < length
			str1.insert(position, '-') #add indel
				
		else: #Throw error if strand is outside of strand ranges
			print("Error.")
			
		#join lists together
		strand1 = ''.join(str1)
		strand2 = ''.join(str2)
		#print strands
		print("Strand 1:",strand1)
		print("Strand 2:",strand2)		
			
	elif menu == 'd': # Delete Indel Module
		# Get user input
		strand = int(input("Which Strand to work on (1 or 2): "))
		position = int(input("Delete what index (start at 0): "))
		
		# If strand # and position == Indel
		if strand == 1 and str1[position] == '-':
			del str1[position] #delete if it is an indel
			
		elif strand == 2 and str2[position] == '-':
			del str2[position] #delete if it is an indel
			
		else: #Throw error if character is not an indel
			print("Error.")	
		
		#join lists together
		strand1 = "".join(str1)
		strand2 = "".join(str2)
		#print strands
		print("Strand 1:",strand1)
		print("Strand 2:",strand2)			
		
	elif menu == 's': # Scoring Module
		# Define Variables	
		match = 0 #matches
		mismatch = 0 #mismatches
		position = 0 #position
		#make temporary lists for scoring module
		strand1 = str1.copy()
		strand2 = str2.copy()
		strand1b = []
		strand2b = []
		
		#Insert Temporary Indels to make the length equal
		while len(strand1) != len(strand2):
			if len(strand1) < len(strand2):
				strand1.append('-')
			elif len(strand2) < len(strand1):
				strand2.append('-')		
		
		# Compare loop
		for n in range(len(strand1)):
			if strand1[position] == strand2[position]: #Matching
				match += 1
				#add the character to the end of the lists
				strand1b.append(strand1[position])
				strand2b.append(strand2[position])
			elif strand1[position] != strand2[position]: #MisMatching
				mismatch += 1
				#pull the characters from the lists
				letter1 = strand1[position]
				letter2 = strand2[position]
				#make uppercase letters
				letter1 = letter1.upper()
				letter2 = letter2.upper()
				#return the uppercase characters to the lists
				strand1b.append(letter1)
				strand2b.append(letter2)
			position += 1
		
		#join lists together
		strand1 = "".join(strand1b)
		strand2 = "".join(strand2b)
		#print matches/mismatches & strands
		print("Matches:",match,"\tMisMatches:",mismatch)
		print("Strand 1:",strand1)
		print("Strand 2:",strand2)
	else:
		print("Error. Please enter a valid selection.")		
	menu = str(input("\nCommand Menu:  (a)dd indel  ~~  (d)elete indel  ~~  (s)core  ~~  (q)uit\nEnter a Command: "))
	
print("Goodbye")