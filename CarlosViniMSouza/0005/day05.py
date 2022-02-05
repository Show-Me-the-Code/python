import json

my_map = {
    'a': 23,
    'b': 42,
    'c': 0xc0ffee
}

print(my_map)

print(json.dumps(my_map, indent=4, sort_keys=True))
