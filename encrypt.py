# encrypt.py — generate key and encrypt report.txt with Fernet
from cryptography.fernet import Fernet

# generate a key and save
key = Fernet.generate_key()
open("key.key", "wb").write(key)

# create Fernet object
f = Fernet(key)

# read report (binary)
report = open("report.txt", "rb").read()

# encrypt and save
encrypted = f.encrypt(report)
open("report.txt.enc", "wb").write(encrypted)

print("Encrypted report saved as report.txt.enc and key.key created.")
