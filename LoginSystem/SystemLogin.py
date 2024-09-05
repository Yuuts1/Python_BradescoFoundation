print("1: Login")
print("2: Sign Up")
print("0: Exit")

users = []

def login_system():
    user_name = input("Digite seu usuario: ")
    user_password = input("Digite sua senha: ")

    for user in users:
        if user['name'] == user_name and user['password'] == user_password:
            print("Bem vindo!")
    else:
        print("Usuario não encontrado")


def sign_up_system():
    name = input("Digite seu nome de usuario: ")
    password = input("Digite sua senha: ")

    users.append({"name": name, "password": password})
    print("Usuario cadastrado com sucesso")

while True:
    choice = int ( input("Digite sua escolha:"))

    if choice == 1:
        login_system()
    elif choice == 2:
        sign_up_system()
    elif choice == 0:
        print("Saindo...")
        break  
    else:
        print("Digite algo valido!")