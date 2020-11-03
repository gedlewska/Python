def replaceChar(word):
    return str(word).replace('.', '').replace(',', '')
    
def theLongest(words):
    return max(words,key=len)

line = "Originally bred to herd cattle, sheep, and horses, the Pembroke Welsh Corgi is an active and intelligent dog breed.Easy to train and eager to learn, Pembrokes are great with children and other pets, and you can find them in four different coat colors and markings."
words = line.split()
result = list(map(replaceChar, words))
long = theLongest(result)
print("The longest string is:", long, "and its length equals:" ,len(long))