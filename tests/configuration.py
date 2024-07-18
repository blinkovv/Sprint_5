import string
import random


EMAIL = "GrantBlinkov11776@yandex.ru"
PASSWORD = "Qwe123Asd456!"
URL = "https://stellarburgers.nomoreparties.site/"
URL_REGISTRATION = "https://stellarburgers.nomoreparties.site/register"
URL_LOGIN = "https://stellarburgers.nomoreparties.site/login"
N = 13
res = ''.join(random.choices(string.ascii_letters, k=N))


def generate_email():
    email = ["@yandex.ru", "@mail.ru", "@gmail.com"]
    rand_idx = random.randrange(len(email))
    random_num = email[rand_idx]
    res = ''.join(random.choices(string.ascii_letters, k=13))
    return f'{res}{random_num}'


def generate_name():
    res = ''.join(random.choices(string.ascii_letters, k=13))
    return res


def generate_password():
    res = ''.join(random.choices(string.ascii_letters, k=13))
    return f'{res}{random.randint(0, 9)}'



