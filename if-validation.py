ages = [18, 40, 57, 80]


if 18 in ages:
  print('is in list')

if 30 not in ages:
  print('not in ages')

age = 0
if age == 30:
  print('age is 30')
elif age >= 20 and age < 30:
  print('lower than 30')
elif age >= 15 or age == 14:
  print('condition doesnt make sense')
else:
  print('Not case')

ages_empty = []

if not ages_empty:
  print('list empty evaluates to False')
