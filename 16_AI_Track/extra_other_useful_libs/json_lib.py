# https://docs.python.org/3/library/json.html
import json

# Encoding basic Python object hierarchies
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

# Compact encoding
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))

# Decoding JSON
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))