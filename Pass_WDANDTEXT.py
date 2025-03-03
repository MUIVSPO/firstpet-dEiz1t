import random
import re

def passwd(numbers, word):
    chars = list(word)
    while True:
        psw = ""
        for i in range(numbers):
            char = random.choice(chars)
            if char.isalpha():
                char = random.choice([char.upper(), char.lower()])
            psw += char
        if (re.search(r'[A-Z]', psw) and
            re.search(r'[a-z]', psw) and
            re.search(r'[0-9]', psw) and
            re.search(r'[!@#$%^&*(),.?":{}|<>]', psw)):
            return psw

numbers = int(input("Какая должна быть длина пороля?: "))
word = input("Введите символы которые будут использоваться в пароле(включая буквы, цифры и специальные символы): ")
print("Ваш пароль:", passwd(numbers, word))
