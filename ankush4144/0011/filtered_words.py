file_name = "filtered_words.txt"

with open(file_name, 'r') as a:
    sensitive_words = a.read().split('\n')

sensitive_words = [i.lower().strip() for i in sensitive_words]

user_input = input("Enter your word: ").strip().lower()

if user_input in sensitive_words:
    print("Freedom")
else:
    print("Human Rights")
