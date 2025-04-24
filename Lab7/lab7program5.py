pwd = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False

for c in pwd:
    if c.isupper():
        has_upper = True
    if c.islower():
        has_lower = True
    if c.isdigit():
        has_digit = True

if has_upper and has_lower and has_digit and len(pwd) >= 8:
    print("Strong password")
else:
    print("Weak Password")
