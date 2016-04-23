def filtertext(x):
    with open(x, 'r') as f:
      text = f.read()
    userinput = input('myinput:')
    for i in text.split('\n'):
        if i in userinput:
            userinput = userinput.replace(str(i), '*'*len(i))
    print(userinput)

filtertext('word.txt')
