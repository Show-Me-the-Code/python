**Description:** This program is a simple program in python to count code lines in one or several directories. It will distinguish:

  1. code lines
  2. blank lines
  3. comment lines
  4. total non-blank lines
  
      > for now, I suppose to count inline comment and multiple lines comment as well. 
      
      > `#` and `'''` in python; `//` and `/**/` in C/C++ 

**Supported file types:** 
    
    .py, .c, .cpp, .h, .hpp. 
  > These 4 types have been tested, should be supposed to work well. Otherwise, `.java` maybe work as well, but not yet tested.

**Usage:** This program should be launched through console, indicating directories that you want to count within. The command line is like this:

    python -3 ComputeCodeLines.py [Full path of first directory] [Full path of second directory] [...]
**Example:**I have a directory in `d:/PythonProjects/python/zeyue/0007`. So my command line will be:

    python -3 ComputeCodeLines.py d:/PythonProjects/python/zeyue/0007
> **ATTENTION:** In the directory path, the slash `/` or `\\` is necessary. **DO NOT** use `\`

And I get a response like this:

    this is the directory: d:\PythonProjects\python\zeyue\0007
    d:\PythonProjects\python\zeyue\0007\ComputeCodeLines.py
    Blank lines: 41
    Code lines: 117
    Comment lines: 63
    No blank lines: 180
    ()
    Final result in the directory
    d:\PythonProjects\python\zeyue\0007
    Code files: 1
    Code lines: 117
    Comment lines: 63
    No blank lines: 180
    Blank lines: 41
    
That's it! Hope you enjoyful!
