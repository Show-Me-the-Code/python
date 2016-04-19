__author__ = 'Tracy'

import os, io, re

commentLines = 0
whiteLines = 0
comment = False

path = 'F:\AllKindsOfWorkplace\PyCharmWorkplace\PythonLearning'

count = 0
def tree(path):
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.isdir(os.path.join(path, file)):
            tree(os.path.join(path, file))
        else:
            filename = os.path.basename(os.path.join(path, file))
            if filename.endswith(".py"):
                # print(filename)
                file = io.open(os.path.join(path, file))
                parse(file)
                file.close()

def parse(file):
    global commentLines
    global whiteLines
    global comment
    for line in file.readlines():
        # line = line.strip("\n")
        if line.startswith("#"):
            commentLines += 1
        elif re.match("^[\\s&&[^\\n]]*$", line):
            whiteLines += 1

tree(path)

print(commentLines)
print(whiteLines)
