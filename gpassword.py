import random
import string


def randompassword():
    password = [""]
    password_length = random.randrange(8, 17)
    #print(password_length)

    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.punctuation))
    password.append(random.choice(string.digits))
    for i in range(password_length-4):
        char = ("qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM")
        password.append(random.choice(char))
    random.shuffle(password)
    #print("".join(password))
    word = "".join(password)
    return word


#randompassword()
