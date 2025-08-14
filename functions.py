from typing import List


def basic_function():
  print('hereeee')

print('passing lists')

def passing_list(ages_list): 
  for i in ages_list:
    print(i)


def side_effect(list: List):
  while list:
    list.pop()

to_remove = [9,3,4,4,5,6,3,3434,34343]

side_effect(to_remove)

print(to_remove)

to_remove = [9,3,4,4,5,6,3,3434,34343]

## pass a copy
side_effect(to_remove[:])

print(to_remove)

## arbitrary parameters
def many_args(*args): 
  print(args) # tuple
  for i in args:
    print(i)

many_args('prueba', '2', 3,4,5,6,5,4,4,5,6)

def many_dictionary(**args):
  print(args)

many_dictionary(name='ss', last_name='eee', age=30)