import string

def anlsText(text):
    dic = {};
    cursor_1 = 0;
    haveWord = False;
    for cursor_2 in range(0,len(text)):
        if(text[cursor_2] not in string.letters):
            if(haveWord):
                if((string.lower(text[cursor_1:cursor_2]) == 'll') or (string.lower(text[cursor_1:cursor_2]) == 'won' and text[cursor_2] == '\'')):
                    word = 'will';
                elif(string.lower(text[cursor_1:cursor_2]) == 're'):
                    word = 'are';
                elif(string.lower(text[cursor_1:cursor_2]) == 't'):
                    word = 'not';
                elif(string.lower(text[cursor_1:cursor_2]) == 'don'):
                    word = 'do';
                elif(string.lower(text[cursor_1:cursor_2]) == 'didn'):
                    word = 'did';
                elif(string.lower(text[cursor_1:cursor_2]) == 'doesn'):
                    word = 'does';
                else:
                    word = string.lower(text[cursor_1:cursor_2]);

                if(word in dic):
                    dic[word] = dic[word] + 1;
                else:
                    dic[word] = 1;
                haveWord = False;
        else:
            haveWord = True;
        if(haveWord == False):
            cursor_1 = cursor_2 + 1;

    return dic;

if __name__ == '__main__':

    with open("./Sources/english_text", "r") as f:

        print anlsText(f.read());

    f.close();
