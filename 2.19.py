mList =[45, 765, 2, 56, 543, 8 , 5, 22, 444, 98]
for item in range(len(mList)):
    mList[item] = str(mList[item]).zfill(3)
print("The word is:", ''.join(map(str, mList)))