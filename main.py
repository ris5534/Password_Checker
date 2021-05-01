# Start of project
password = str(input())
special_characters = ["!", "@", "#", "$", "^", "&", "*", "(", ")", "_"]
save_to_file = 0

if len(password) <= 6:
    print("ERROR: Password not long enough")
else:
    save_to_file += 1
    print("PASS: There is more than 6 characters")

for character in password:
    if character.isdigit():
        save_to_file += 1
        print("PASS: There is a digit")
        break
else:
    print("ERROR: No Digit")
for character in special_characters:
    if character in password:
        save_to_file += 1
        print("PASS: There is a special character")
        break
else:
    print("ERROR: No Special Character")
# Checking for Uppercase letters
for character in password:
    if character.isupper():
        save_to_file += 1
        print("PASS: There is an uppercase letter")
        break
else:
    print("ERROR: NO uppercase letter")
# Checking for lowercase letter
for character in password:
    if character.islower():
        save_to_file += 1
        print("PASS: There is lowercase letter")
        break
else:
    print("ERROR: No lowercase letter")
# creates a .txt file under the project if all tests check out and saves the password
if save_to_file == 5:
    f = open("PassWords.txt", "w")
    f.write(password)
