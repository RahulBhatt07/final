# python code to implement the above approach

# Function to print the words
def printWord(str, s):
	for i in range(0, len(str)):
		if (not (str[i] in s)):
			return

	print(str)

# Function to find the words
def findWord(str1, str2):
	s = ""
	for i in str2:
		s += i

	for i in range(0, len(str1)):
		printWord(str1[i], s)


str1 = ["go", "bat", "me", "eat", "goal", "boy", "run"]

str2 = ["e", "o", "b", "a", "m", "g", "l"]

findWord(str1, str2)


