email = input("Enter your email: ")
k = 0
j = 0
d = 0

if len(email) >= 6:
    if email[0].isalpha():
        if '@' in email and email.count("@") == 1:
            if (email[-4] == "." and email[-3] != ".") or (email[-4] != "." and email[-3] == "."):
                # Rest of the code

                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Invalid email address")
                else:
                    print("Valid email address")
            else:
                print("Invalid email address")
        else:
            print("Invalid email address")
    else:
        print("Invalid email address")
else:
    print("Invalid email address")
