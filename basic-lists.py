'''
List is a collection items in particular order
[] indicates a list
'''

letters = ['a', 'b', 'c', 'd', 'e']

print(letters)

# last element
print(letters[-1])
print(letters[-2])
print(letters[-3])

# append items end of list
letters.append('f')
# insert any position 
letters.insert(0, '0')
print(letters)
# delete specific index
del letters[0]
print(letters)
# remove last item
popped_letter = letters.pop()
print(popped_letter)
print(letters)
# remove using pop any position
letters.pop(3)
print(letters)
letters.insert(3, 'd')
letters.append('f')
letters.append('c')
print(letters)

# search value and remove (returns removed item)
# only removes first ocurrence
letters.remove('c')
print(letters)