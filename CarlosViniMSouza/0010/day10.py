# Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def sub(a, b):
    return a - b


func = [sub]

print(func[0])
# Output: <function sub at 0x000001F907895900>

print(func[0](5, 7))
# Output: -2
