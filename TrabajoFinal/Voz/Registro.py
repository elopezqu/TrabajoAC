def registro(existe, nombre):
    if(existe):
        file = open("./Usuarios/"+nombre+".txt", "r")
        nivel =  (int(file.read()))
        file.close()
        return nivel    
    else:
        file = open("./Usuarios/"+nombre+".txt", "w")
        file.write("4")
        file.close()
        return 2

nombre = input("Ingrese nombre:\n")
nivel = registro(True, nombre)
print(nivel)

