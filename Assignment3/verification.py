import random

userid = input("Enter UserID: ")
password = input("Enter Password: ")

if userid == "Tiru" and password == "1234":
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_input = int(input("Enter the above number: "))
    if user_input == captcha:
        print("Login successful")
    else:
        print("Captcha verification failed")
else:
    print("Invalid credentials")
