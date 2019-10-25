import os

code_lines = list()
notation_lines = list()
blank_lines = list()


def process_file(filename):
    global code_lines
    global notation_lines
    global blank_lines
    with open(filename, 'r') as file:
        for line in file.readlines():
            _line = line.strip()
            if not _line:
                blank_lines.append(_line)
            elif _line.startswith('#'):
                notation_lines.append(_line)
            else:
                code_lines.append(_line)


def show_result():
    global code_lines
    global notation_lines
    global blank_lines
    print('-'*20)
    print('code:', len(code_lines))
    for line in code_lines:
        print(line)
    print('-' * 20)
    print('notation:', len(notation_lines))
    for line in notation_lines:
        print(line)
    print('-' * 20)
    print('blank:', len(blank_lines))
    code_lines.clear()
    notation_lines.clear()
    blank_lines.clear()


def process_files(path='../6'):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.py'):
            print('='*30)
            print('current file:', os.path.join(path, file))
            process_file(os.path.join(path, file))
            show_result()

process_files()