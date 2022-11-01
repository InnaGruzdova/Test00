import random

valid_email = 'andrej169@yandex.ru'
valid_password = 'K42mbNVrZBgCsyA'
valid_pone = '+79522840568'
url_tmall_login = 'https://b2c.passport.rt.ru/'
url_cod = 'https://my.rt.ru/'
url_email = "https://www.1secmail.com/api/v1/"

import random
engl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
domens = ['com', 'ua', 'ru', 'net']


def pass_gener():
    passw_random = ''
    for x in range(6):
        passw_random  = ''.join([passw_random, random.choice(list(engl))])

    return passw_random.lower()
print(pass_gener())
def email_gener():
    name_email = ''
    name_server = ''
    for x in range(6):
        name_email = ''.join([name_email, random.choice(engl)])
    for y in range(4):
        name_server = ''.join([name_server, random.choice(engl)])
    def domen():
        dom = random.choice(domens)
        return dom
    email = ''.join([name_email,'@',name_server,'.',domen()])
    return email.lower()
print(email_gener())



fcv = ''
for x in range(6):
    fcv = fcv + random.choice(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
print(f'вставить\n{fcv}')
login_no_valid = fcv
ls_no_valid = fcv


def generate_string(n):
   return "x" * n

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}*****'


class AuthUser:
   @staticmethod
   def random():  # Функция генерирует случайные валидные данные
      password = fake.password()
      return password


def generate_string(num):
   return "x" * num
