import json
from pathlib import Path
numbers = [1,3,4,5,4,3,2]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)