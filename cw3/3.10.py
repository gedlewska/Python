def roman2int(string):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                     'XC': 90, 'CD': 400, 'CM': 900}
    item = 0
    num = 0
    while item < len(string):
        if item + 1 < len(string) and string[item:item + 2] in roman_numbers:
            num += roman_numbers[string[item:item + 2]]
            item += 2
        else:
            num += roman_numbers[string[item]]
            item += 1
    return num


text = input("Write number in roman: ")
print(roman2int(text))
