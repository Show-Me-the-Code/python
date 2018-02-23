import os
import string

#config
CODEPATH = '/home/william/pythonPractice/Sources/code/'

if __name__ == '__main__':

    line_num = 0;
    comment_num = 0;
    blank_num = 0;

    for f in os.walk(CODEPATH).next()[2]:
        with open(CODEPATH + f, 'r') as code:
            for line in code.readlines():
                line_num += 1;
                if line.strip() == '':
                    blank_num += 1;
                if line.strip()[:1] == '#':
                    comment_num += 1;

    print 'You have wrote %s lines of code, includes %s blank line and %s comment line' % (line_num, blank_num, comment_num);
