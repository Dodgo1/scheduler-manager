import random
import string
from hashlib import md5


def hash_string(password: str):
    return md5(bytes(password, "utf-8")).hexdigest()

def get_random_string(length:int):
    return "".join(random.choices(string.ascii_letters, k=length))