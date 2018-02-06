#0021
import uuid
import hashlib

def enpass(password,salt=None):
    if salt is None:
        salt = str(uuid.uuid4())[:4]        
    assert 4==len(salt)
    return salt+':'+hashlib.sha256(password.encode()+salt.encode()).hexdigest()

def ckpass(password,enedpass):
    return enpass(password,enedpass[:4]) == enedpass

if __name__ =='__main__':
    passfile = 'password.txt'
    enedpass = enpass('12345')
    with open(passfile,'w')as f:
        f.write(enedpass)
    f.close()

    with open(passfile,'r')as f:
        print(ckpass('12345',f.read()))
    f.close()
