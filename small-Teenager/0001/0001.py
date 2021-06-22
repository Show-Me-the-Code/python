'''
 做为 Apple Store App 独立开发者，你要搞限时促销，
 为你的应用生成激活码（或者优惠券），
 使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import uuid


def get_activity_code(num):
    file = open('txt/activate_code.txt', 'w')
    for i in range(0, num):
        # print(uuid.uuid1().hex,file=file)
        file.write(uuid.uuid4().hex + '\n')
    file.close()


get_activity_code(200)
