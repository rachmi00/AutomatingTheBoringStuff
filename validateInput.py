while True:
    print("Enter your age: ")
    age = input()
    if age.isdecimal():
       break
    print("Enter a number for you age")
while True:
    print("Select a new password (Numbers and letters only)")
    password = input()
    if password.isalnum():
        break
    print("Enter a valid password value")