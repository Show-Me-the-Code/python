def filterwords(x):
    with open(x, 'r') as f:
      text = f.read()
    print (text.split('\n'))
    userinput = input('myinput:')
    for i in text.split('\n'):
        if i in userinput:
            return True

if filterwords('word.txt'):
    print ('freedom')
else:
    print ('human rights')
