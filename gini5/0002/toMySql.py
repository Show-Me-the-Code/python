import MySQLdb, random, string
db = MySQLdb.connect(host="localhost", port = 3306, user="root",passwd="test123",db="mysql")
cursor = db.cursor()


dic = {}

def generate_string(size=8):
    seed = string.ascii_letters+string.digits
    res = ''.join(random.sample(seed,size))
    return res

for i in range(200):
    new = generate_string()
    while new in dic.values():
        new = generate_string()
    dic[i] = new
    query = "INSERT INTO ACTIVATION_CODE VALUES(%d,%r)"%(i,new)
    cursor.execute(query)

try:
    db.commit()
except:
        db.rollback()

# select #
cursor.execute('SELECT * FROM ACTIVATION_CODE')
data = cursor.fetchall()
print(data)
cursor.close()
db.close()