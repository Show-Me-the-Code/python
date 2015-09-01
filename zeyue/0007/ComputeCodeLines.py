#!/usr/bin/python

import os


file_suffix = "not defined"
inline_comment_syntax = "not defined"
multiline_comment_syntax = "not defined"
result = {"Code files": 0,
          "Total lines": 0,
          "Code lines": 0,
          "Comment lines": 0,
          "Blank lines": 0}


def getFilesList(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)

    return file_paths


def getSuffix(full_file_path):
    return os.path.splitext(full_file_path)[1][1:]


def identifyFileType(suffix):
    if suffix == "py":
        return "#", "\"\"\""
    elif suffix == "c" or suffix == "h" or suffix == "cpp" or suffix == "hpp":
        return "//", "/*"
    else:
        return "not defined"


def isInlineComment(string_line):
    """This function will check if input line is a comment or not.

    :string_line: input line
    :returns: true or false

    """
    commentLen = len(inline_comment_syntax)
    if string_line[0:commentLen] == inline_comment_syntax:
        return True
    else:
        return False


def isMultilineComment(string_line):
    commentLen = len(str(multiline_comment_syntax))
    if string_line[0:commentLen] == multiline_comment_syntax:
        return True
    else:
        return False


def countOneFile(full_file_path):
    global inline_comment_syntax, multiline_comment_syntax
    file_suffix = getSuffix(full_file_path)
    if(identifyFileType(file_suffix) != "not defined"):
        result["Code files"] += 1

        (inline_comment_syntax,
         multiline_comment_syntax) = identifyFileType(file_suffix)
        with open(full_file_path, "r") as lines:
            for line in lines:
                line = line.strip()
                if line.strip():
                    result["Total lines"] += 1
                    if isInlineComment(line):
                        result["Comment lines"] += 1
                    elif isMultilineComment(line):
                        result["Comment lines"] += 1
                    else:
                        result["Code lines"] += 1
                else:
                    result["Blank lines"] += 1


def countInDirectory(directory):
    full_file_paths = getFilesList(directory)
    for f in full_file_paths:
        countOneFile(f)

directory = input()
# countOneFile("d:/NOTBACKEDUP/python/zeyue/0007/ComputeCodeLines.py")
countInDirectory(directory)
# countInDirectory("D:/Documents/Zeyue/workspace/Gauge/v1.3.10\
# /Recorder/QuartzDyne/src")
# countOneFile("D:/Documents/Zeyue/workspace/Gauge/v1.3.10\
# /Recorder/QuartzDyne/src/CommandTable.c")

print(str(result))
