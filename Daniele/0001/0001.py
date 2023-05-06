import hashlib, os

def Hashing_Password(password_On_Clear):
    # Generate a random salt
    salt = os.urandom(16)

    # Add the salt to the clear password
    salted_password = password_On_Clear.encode('utf-8') + salt

    # Generate the hash using SHA-256
    hash_object = hashlib.sha256(salted_password)
    hash_value = hash_object.hexdigest()

    # Return the hash and the salt
    return hash_value, salt
