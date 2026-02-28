import string
import secrets

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print(f"Password: {generate_password(10)}")