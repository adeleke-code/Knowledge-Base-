import string
import random

def generate_password():
    a = []
    for _ in range(4):
        a.append(random.choice(string.ascii_lowercase))
        a.append(random.choice(string.ascii_uppercase))
        a.append(random.choice(string.digits))
        a.append(random.choice(["@","!","$","#","="]))
    random.shuffle(a)
    return "".join(a)