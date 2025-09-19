name = "axel david"

print(name.title())
print(name.upper())
print(name.lower())

# String variables
first_name = 'axel'
last_name = 'espinosa'
name = f'{first_name} {last_name}'
print(name)

# Whitespace stripping

with_space = 'test '
no_space = 'test'
left_space = ' test'
print(with_space == no_space)
print(with_space.rstrip() == no_space)
print(left_space.lstrip() == no_space)
spaces = ' test '

print(spaces.strip() == no_space)
# prefixes
google = 'https://google.com'
print(google.removeprefix('https://'))
print(google.removesuffix('.com'))
file_ext = 'mytest.txt'
print(file_ext.removesuffix('.'))
