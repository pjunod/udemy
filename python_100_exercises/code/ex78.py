import random
import string

total = string.digits + string.ascii_letters + string.punctuation

passlist = random.sample(total, k=6)
print(''.join(passlist))
