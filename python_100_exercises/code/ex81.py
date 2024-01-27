def check_reqs(userpass):
    bad = []
    if len(userpass) < 5:
        bad.append("Password minimum 5 characters")
    if not any(i.isdigit() for i in userpass):
        bad.append("Password must contain a number")
    if not any(i.isupper() for i in userpass):
        bad.append("Password must contain an uppercase letter")
    return bad


with open("users.txt") as file:
    users = file.readlines()

users = [x.strip() for x in users]

while True:
    username = input("Enter username: ")
    if username in users:
        print("Username exists")
    else:
        print("Username is fine")
        break

while True:
    userpass = input("Enter new password: ")
    passcheck = check_reqs(userpass)
    if len(passcheck) > 0:
        print("Please check the following:")
        for i in passcheck:
            print(i)
    else:
        print("Password is fine")
        break
