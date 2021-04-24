# Start of project
password = str(input())
#contains_digit = False

if len(password) <= 6:
    print("Password not long enough")

for character in password:
    if character.isdigit():
        print("There is a number in the password")
        break
else:
    print("No Digit in password")
