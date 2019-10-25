import random, string


def gen_charint(filename, width = 4, num = 200):
    #Open/Close times is far more expensive than R/W times
    f = open(filename, 'wb')
    charint = string.digits + string.letters
    for i in range(num):
        verify = [random.choice(charint) for j in range(width)]
        verify = ''.join(verify) + '\n' 
        f.write(verify)
    f.close()

if __name__ == '__main__':
    
    filename = 'result.txt'
    width = 4
    num = 200
    gen_charint(filename, width, num)

    
