# Function to check if a password is correct
def check_password(password):
    # Read the hash and salt of the password from the database
    with open('KEY_HASH.txt'), 'r') as f:
        saved_hash, salt = f.read().strip().split(',')

    # Add the salt to the entered password
    salted_password = password.encode('utf-8') + salt.encode('utf-8')

    # Generate the hash of the entered password using SHA-256
    hash_object = hashlib.sha256(salted_password)
    entered_hash = hash_object.hexdigest()

    # Compare the two hashes
    if entered_hash == saved_hash:
        print('Password Correct')
        return True
    else:
        return False
