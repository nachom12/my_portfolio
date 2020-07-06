import random

def run():
    print("Adivina el numero")
    numero_generado = random.randint(1,100)
    numero = 0
    intentos = 5
    while ((numero != numero_generado) and intentos > 0):
        intentos = intentos - 1
        numero = int(input("Ingrese un numero: "))
        if (numero > numero_generado):
            print("El numero es menor!")
        elif (numero < numero_generado):
            print("El numero es mayor!")
        else:
            print ("Ganaste!")
            break
    if (intentos == 0):
        print ("Te quedaste sin intentos")
        print ("El numero era " + str(numero_generado))

if __name__ == "__main__":
    run()