word = "word"
result = ""
for letter in word:
    result += letter + '_'
print(result[:len(result) - 1])