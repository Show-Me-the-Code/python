# Compute the line number of codes in one directory

import os


def getFilesList(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)

    return file_paths

full_file_paths = getFilesList("D:/PythonProjects/python")
# print("\n".join(full_file_paths))

file_type = "python"
inline_comment_syntax = "#"


def isInlineComment(string_line):
    """This function will check if input line is a comment or not.

    :string_line: input line
    :returns: true or false

    """
    if string_line[0] == inline_comment_syntax:
        return True
    else:
        return False

# print(isInlineComment("# this is a test"))
