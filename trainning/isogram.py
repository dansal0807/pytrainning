#Determine if a word or phrase is an isogram.
#An isogram (also known as a "nonpattern word") is a word or 
#phrase without a repeating letter, however spaces and hyphens are 
#allowed to appear multiple times.

gword = input("give me a word and I will tell you if it's a isogram: ")

def isogram(word):
    letters = []  
    for letter in word:
        if letter in letters:
            return False
        letters.append(letter)
    return True

result = isogram(gword)

if result == True:
    print(f"the word {gword} is a isogram")
else:
    print(f"the word {gword} is not a isogram")