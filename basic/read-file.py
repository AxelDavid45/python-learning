from pathlib import Path

file = Path('./pi_million_digits.txt')

lines = file.read_text().strip()


birthday = input('enter your birthday, in the form mmddyy: ')
if birthday in lines:
  print('yoir birthday appears in the first million digits of pi')
else:
  print('your birthday does not appear in the first million digits ')
