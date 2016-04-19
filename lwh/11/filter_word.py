# coding = utf-8
"""
def filter_word():

    # init
    filter_words_list = []
    with open("filtered_words.txt", "r") as f:
        string_read = f.readline()
        while string_read != "":
            filter_words_list.append(string_read)
            string_read = f.readline()

        print("Enter \\q to exit.")
        string_input = input(
            "Input your word to check whether it was filtered ->")
        while string_input != "\\q":
            if string_input in filter_words_list:
                print("Freedom")
            else:
                print("Human Rights")
            string_input = input(
                "Input your word to check whether it was filtered ->")

if __name__ == "__main__":
    filter_word()

"""
# coding = utf-8
__author__ = 'Forec'
word_filter = set()
with open('filtered_words.txt',"r") as f:
    for x in f.readlines():
        word_filter |= {x.rstrip('\n')}
while True:
    s = input()
    if s == 'exit':
        break
    elif s in word_filter:
        print('Freedom')
    else:
        print('Human Rights')
        