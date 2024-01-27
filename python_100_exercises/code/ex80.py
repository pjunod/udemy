def check_reqs(userpass):
    bad = []
    if len(userpass) < 5:
        bad.append("Password minimum 5 characters")
    if not any(i.isdigit() for i in userpass):
        bad.append("Password must contain a number")
    if not any(i.isupper() for i in userpass):
        bad.append("Password must contain an uppercase letter")
    return bad


while (True):
    userpass = input("Enter new password: ")
    passcheck = check_reqs(userpass)
    if len(passcheck) > 0:
        print("Please check the following:")
        for i in passcheck:
            print(i)
    else:
        print("Password is fine")
        break
