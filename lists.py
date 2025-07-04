letters = ['a', 'b', 'c', 'd']

#Add
letters.append('d') #add element at the end of the list
letters.insert(0,'_')
print(letters)

# Remove
letters.pop(0)
for letter in letters:
    if letter == 'b':
        letters.remove('b')
print(letters)


if "e" in letters:
    print(letters.index("e"))
print(letters.count('e'))