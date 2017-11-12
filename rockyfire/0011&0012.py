0011 & 0012
with open("filtered_words.txt","r") as f:
    fs=f.readlines()
    while True:
        word = input("input your word")
        Freedom_list=[x.strip() for x in fs]
        # 0011
        if word  in Freedom_list:
            print ("Freedom")
        else:
            print ("Human Rights")
        # 0012
        for x in Freedom_list:
            if word.find(x) != -1:
                print (len(x))
                print(word.replace(x,"*"*len(x)))

