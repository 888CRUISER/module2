# Модуль 1. Часть 1.

# Уровень 1

# print((5 + ((7 * 5) / 8)) / 3**5)

# Уровень 2

# def main(v, t):
#     if v * t > 109:
#         print((v * t) % 109)
#     else:
#         print(v * t)

# main(30, 5)

# Уровень 3

# def main(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)

# Модуль 1. Часть 2.

# Уровень 1

# def main(a, b, c):
#     if a == b and a == c and b == c:
#         print(3)
#     elif a != b and a != c and b != c:
#         print(0)
#     else:
#         print(2)

# Уровень 2 
# def main(a,b,c,d):
#     if a == c or b == d:
#         print('YES')
#     else:
#         print("NO")

# main(input('Введите первое число'),input(Введите второе число),input(Введите третье число),input(Введите четвертое число))

# Уровень 3

# password = ''

# while True:
#     password = input('Введите свой пароль: ')
#     capitalize_count = 0
#     lower_count = 0

#     if len(password) <= 8:
#         print('Пароль слишком маленький')
#         continue
#     elif (len(password) > 8):
#         for p in password:
#             if p == p.capitalize():
#                 capitalize_count += 1
#             if p == p.lower():
#                 lower_count += 1
#         if capitalize_count > 0 and lower_count > 0:
#             print('Ваш пароль', password, 'кол-во символов', len(password), 'кол-во заглавных', capitalize_count, 'кол-во прописных', lower_count)
#             break
#         else:
#             print('Введите пароль с прописными и заглавными буквами')
#             continue

# Первый коммит
def main():
    return 'First commit'
# GIT