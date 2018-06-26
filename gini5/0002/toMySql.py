import pymysql, random, string
db = pymysql.connect(host="localhost",user="testuser",passwd="test123",db="mysql")
cursor = db.cursor()
# dic = {}
#
# def generate_string(size=8):
#     seed = string.ascii_letters+string.digits
#     res = ''.join(random.sample(seed,size))
#     return res
#
# for i in range(200):
#     new = generate_string()
#     while new in dic.values():
#         new = generate_string()
#     dic[i] = new
#     cursor.execute("INSERT INTO ACTIVATIONCODE VALUES(%d,%s)"%(i,new))
#
# try:
#     db.commit()
# except:
#         db.rollback()

cursor.close()
db.close()