def replace_char(word):
    return str(word).replace('.', '').replace(',', '')

line = "Originally bred to herd cattle, sheep, and horses, the Pembroke Welsh Corgi is an active and intelligent dog breed. Easy to train and eager to learn, Pembrokes are great with children and other pets, and you can find them in four different coat colors and markings."
words = line.split()
result = list(map(replace_char, words))
for item in range(len(result)):
    result[item] = result[item].lower()
print("Sorted by alphabet:", sorted(result))
print("Sorted by length:", sorted(result, key = len))