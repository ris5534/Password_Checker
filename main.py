# Start of project
password = str(input())
special_characters = ["!", "@", "#", "$", "^", "&", "*", "(", ")", "_"]

if len(password) <= 6:
    print("ERROR: Password not long enough")
else:
    print("PASS: There is more than 6 characters")

for character in password:
    if character.isdigit():
        print("PASS: There is a digit")
        break
else:
    print("ERROR: No Digit")
for character in special_characters:
    if character in password:
        print("PASS: There is a special character")
        break
else:
    print("ERROR: No Special Character")
# Checking for Uppercase letters
for character in password:
    if character.isupper():
        print("PASS: There is an uppercase letter")
        break
else:
    print("ERROR: NO uppercase letter")
# Checking for lowercase letter
for character in password:
    if character.islower():
        print("PASS: There is lowercase letter")
        break
else:
    print("ERROR: No lowercase letter")
