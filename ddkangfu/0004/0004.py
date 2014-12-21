#coding=utf-8

def count_word(file_name):
    f = open(file_name)
    line = f.readline()

    while line:
        print line
        line = f.readline()

    f.close()


if __name__ == '__main__':
    count_word('english.txt')