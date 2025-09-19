from re import M


dog = { 'color': 'black', 'name': 'kira', 'age': 1 }

print(dog)
dog['age'] += 30
dog['x_position'] = 19
dog['y_position'] = 3
print('modify', dog)

while not dog['age']:
  print('decrement', dog['age'])
  dog['age'] -= 1

print('finish age')

for k in dog: 
  print(f'{k}: {dog[k]}')

print('Delete age')
del dog['age']
print(dog)
print(dog.get('age', 'age deleted'))

for k,v in dog.items():
  print(f'{k}: {v}')

if 'name' in sorted(dog.keys()):
  print('key name exists')

people_programming = {
  'erin': 'c++',
  'pedro': 'java',
  'alan': 'golang',
  'juan': 'java',
  'amazon': 'java',
  'google': 'c++',
  'monte': 'javascript',
  }

print('create a list of unique items')
for lang in set(people_programming.values()):
  print(lang)

print('how many languages people use?', set(people_programming.values()))
print('how many people were interviewed?', len(people_programming.keys()))

dog_1 = { 'name': 'kira', 'age': '1'}
dog_2 = { 'name': 'gorda', 'age': '4'}
dog_3 = { 'name': 'balto', 'age': 4 }

print('nesting elements')
dogs = [dog_1, dog_2, dog_3]

for d in dogs:
  print(d)

print('generate enemies')
enemies = []

for enemy_number in range(30):
  enemies.append({ 'color': 'green', 'points': 10 * enemy_number })

for alien in enemies[:4]:
  print('enemy', alien)

init_game = {
  'screen': (600, 600),
  'enemies': enemies,
  'levels': 8,
  'current_level': 1
  }