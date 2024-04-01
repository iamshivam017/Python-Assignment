def validate_password(password, username, last_passwords):
    # Check password length
    if len(password) < 10:
        return "Password must be at least 10 characters long."
    
    # Check for character variety
    uppercase, lowercase, digit, special = 0, 0, 0, 0
    for char in password:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digit += 1
        elif char in '@#$%&*!':
            special += 1

    if uppercase < 2 or lowercase < 2 or digits < 2 or special < 2:
        return "Password must contain at least two uppercase letters, two lowercase letters, two digits, and two special characters."
    
    # Check for sequence and repetition restrictions
    for i in range(len(username) - 2):
        if username[i:i+3] in password:
            return "Password should not contain any sequence of three or more consecutive characters from the username."
    for i in range(len(password) - 3):
        if password[i] == password[i+1] == password[i+2] == password[i+3]:
            return "No character should repeat more than three times in a row."
    
    # Check for historical password match
    if password in last_passwords:
        return "The new password must not be the same as the last three passwords used by the user."
    
    return "Password is valid."


username = "user123"
last_passwords = ["password1", "password2", "password3"]
while True:
    password = input("Enter a new password: ")
    validation_message = validate_password(password, username, last_passwords)
    if validation_message == "Password is valid.":
        print(validation_message)
        break
    else:
        print(validation_message)