import sys

email = input("Enter email: ").strip()
password = input("Enter password: ")

if password == "":
    print("Invalid password")
    sys.exit()

if len(password) < 8:
    print("Invalid password")
    sys.exit()

if password == email:
    print("Invalid password")
    sys.exit()

if " " in password:
    print("Invalid password")
    sys.exit()

if not password[0].isalnum() or not password[-1].isalnum():
    print("Invalid password")
    sys.exit()

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)

if not (has_upper and has_lower):
    print("Invalid password")
    sys.exit()

print("Valid password")
