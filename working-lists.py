from re import A


magicians = ['alice', 'david', 'carolina']

for magician in magicians: 
  print(magician)

# range starts at 0 and stops at 6, not showing 6
# range(1, 6)
for value in range(6):
  print(value)

print('list range', list(range(0, 11, 2)))
squares = []
for value in range(11):
  squares.append(value ** 2)
print(squares)


digits = list(range(1, 10)) 
digits.append(0)
# statistic 
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions

squares = [value ** 2 for value in range(1,11)]
print('squares', squares)

# slicing lists
players = ['charles', 'john', 'michael', 'florence', 'eli', 'juan', 'pedro', 'alana']
print('sliced', players[0:3])
print('sliced equivalent', players[:3])
print('include end of list', players[3:])
print('last three even if list grows', players[-3:])

print('Loop through slice')
for p in players[-4:]:
  print(p.title())

print('copy list')

print('copy first players')
new_players = players[:3]
new_players.append('gabriela')
print('old players', players)
print('new players', new_players)
