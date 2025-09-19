from pathlib import Path

file = Path('./generated.txt')

contents = 'Hello\n'
contents += 'Generated another line'

file.write_text(contents)