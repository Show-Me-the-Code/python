__author__ = 'PyBeaner'
words = open("filtered_words.txt").read().split()

user_input = input("Please Input an word:")

for word in words:
    user_input = user_input.replace(word, "*" * len(word))

print(user_input)
