__author__ = 'PyBeaner'

words = open("filtered_words.txt").read().split()

word = input("Please Input an word:")
if word in words:
    print("Freedom")
else:
    print("Human Rights")
