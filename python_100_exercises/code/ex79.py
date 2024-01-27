def check_reqs(userpass):
    if len(userpass) < 5:
        return 0
    elif not any(i.isdigit() for i in userpass):
        return 0
    elif not any(i.isupper() for i in userpass):
        return 0
    else:
        return 1


while (True):
    userpass = input("Enter new password: ")
    if check_reqs(userpass):
        print("Password is fine")
        break
    else:
        print("Password is not fine")
