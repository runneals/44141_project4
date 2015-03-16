
str1 = []
str2 = []

strand1 = input("Enter DNA Strand 1: ")
strand2 = input("Enter DNA Strand 2: ")

str1(strand1)
str2(strand2)

print(str1)

command = input("\nCommand Menu:  (a)dd indel  ~~  (d)elete indel  ~~  (s)core  ~~  (q)uit\nEnter a Command: ")


'''
Matches: 7	MisMatches: 2
String 1: aaAbbBccc
String 2: aaBbbCccc

Enter a command: 
a(add indel)
d(delete indel)
s(score)
q(quit): a
Which String to work on (1 or 2): 2
Before which index to place the indel?: 2
String1: aaabbbccc
String2: aa-bbbcccc

Enter a command: 
a(add indel)
d(delete indel)
s(score)
q(quit): s

Matches: 8	MisMatches: 2
String 1: aaAbbbccc-
String 2: aa-bbbcccC

Enter a command: 
a(add indel)
d(delete indel)
s(score)
q(quit): d
Which String to work on (1 or 2): 2
Delete what index (start at 0): 2
String1: aaabbbccc
String2: aabbbcccc

Enter a command: 
a(add indel)
d(delete indel)
s(score)
q(quit): s

Matches: 7	MisMatches: 2
String 1: aaAbbBccc
String 2: aaBbbCccc

Enter a command: 
a(add indel)
d(delete indel)
s(score)
q(quit): q
'''