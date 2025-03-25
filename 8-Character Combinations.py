import itertools 
import string
#it used to generate the combinations
# contain pre defined character set(letter,digits,punctuations)


charset = string.ascii_letters + string.digits + string.punctuation
# This creates a set of all possible characters


def generate_combinations():
    for combo in itertools.product(charset, repeat=8):
        yield ''.join(combo)
#Generates all possible 8-character sequences using charset.


if __name__ == "__main__":
    count = 0
    for combination in generate_combinations():
        print(combination)
        count += 1
        if count >= 10:
            break
