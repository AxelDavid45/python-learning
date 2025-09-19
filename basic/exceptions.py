l = [3,4]
try:
  v = l[1]
except IndexError:
  print('No existe')
else:
  print(v)


from pathlib import Path

# Files does not exist
f = Path("./portfolio.jpg")

try:
  data = f.read_bytes()
except FileNotFoundError:
  print('File is not in your system')
else:
  print(data[:8])
