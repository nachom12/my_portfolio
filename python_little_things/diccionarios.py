def run():
    #key, value#
    mi_diccionaro = {
        "Nacho": 49218878,
        "Ana": 123456789,
        "Elbio": 29690004,
    }
    print("Personas en el diccionario")
    for nombres, cedulas in mi_diccionaro.items(): #esta keys y esta values
        print(nombres + " tiene la cedula: " + str(cedulas))

if __name__ == "__main__":
    run()