#A Text Analyzer Program
#Input text
text = input("Input your text: ")
text = text.lower()
textInList = text
lengthOfText = len(text)
wordOne = textInList[0]
wordTwo = textInList[-1]

#Choosen words
choosenWords = []
firstWord = input("Input your first text: ").lower()
secondWord = input("Input your second text: ").lower()
thirdWord = input("Input your third text: ").lower()
print(f"The choosen letters are {firstWord}, {secondWord}, {thirdWord}")

#Add choosenWords to a list
choosenWords.append(firstWord)
choosenWords.append(secondWord)
choosenWords.append(thirdWord)

 

print(text)
print("\n")
print(f"The letter {firstWord} appears {text.count(firstWord)} times")
print(f"The letter {secondWord} appears {text.count(secondWord)} times")
print(f"The letter {thirdWord} appears {text.count(thirdWord)} times")
print("\n")
print(f"There are {lengthOfText} characters in total")
print("\n")
print(f"The first letter is \"{wordOne}\" and the last letter is \"{wordTwo}\"")
print("\n")
print(f"The inverted text is {text[::-1]}")
print("\n")
print("python" in text)
