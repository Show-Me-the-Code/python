f = open('artical.txt','r')
artical = f.read()
f.close()

punctuation = ",.\"\'?!\n"

for p in punctuation:
    artical = artical.replace(p," ")

words = {}

for word in artical.split(" "):
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for key in words:
    if key == " ":
        continue
    print key,words[key]
