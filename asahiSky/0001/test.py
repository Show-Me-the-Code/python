import uuid


def create_Num():
    number = 200
    result = []
    sum = 0
    while True:
        i = str(uuid.uuid1())
        if not i in result:
            result.append(i)
            sum += 1
        if sum == number:
            break
    return result

if __name__ == '__main__':
    result = create_Num()
    print(result)
