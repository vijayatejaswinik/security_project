# decrypt.py — decrypt report.txt.enc using key.key
from cryptography.fernet import Fernet

key = open("key.key", "rb").read()
f = Fernet(key)

encrypted = open("report.txt.enc", "rb").read()

decrypted = f.decrypt(encrypted)
open("decrypted_report.txt", "wb").write(decrypted)

print("Decrypted report saved as decrypted_report.txt")
