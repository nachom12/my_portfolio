import random

def build_password():
    mayus = ['A', 'B', 'C', 'D']
    minus = ['a', 'b', 'c', 'd']
    simb = ['@', '$', '%', '?']
    num = ['1','2','3','4', '5']
    caracteres = mayus + minus + simb + num
    contra = []
    for i in range (0,15):
        caracter_random = random.choice(caracteres)
        contra.append(caracter_random)
    contra = "".join(contra) # transforma la lista en un string
    return contra

def run():
    password = build_password()
    print("Your new password is: " + str(password))


if __name__ == "__main__":
    run()