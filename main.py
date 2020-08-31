import string
import random

def pass_gera(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

pass_gera()
print(pass_gera())