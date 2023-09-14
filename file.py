usernames = []
passwords = []
names = []


def register():
    usernames.append(input("Создайте ваш юзернейм: "))
    passwords.append(input("Создайте ваш пароль: "))
# with open('username.txt','w') as my_file:
#     my_file.write((register) + '\n')



def login():
    username = input("Введите ваш юзернейм: ")
    password = input("Введите ваш пароль: ")
    if username in usernames and password in passwords:
        print("Добро пожаловать!")
    else:
        print("Неверный логин или пароль!")


while True:
    account_ans = input("Выберите:  a)Регистрация     b)Логин     c)Выход ")
    if account_ans == "a":
        register()
    if account_ans == "b":
        login()
    if account_ans == "c":
        break



