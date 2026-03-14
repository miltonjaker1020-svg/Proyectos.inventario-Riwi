


while True:
    Nombre=input("Introduzca el nombre del producto: ") #Introduzco el nombre del producto
    while not Nombre.isalpha(): # verifico que el nombre sea valido
        print("Introduzca un nombre valido")
        Nombre=input("Introduzca el nombre del producto: ")
    try: # Pruebo el codigo
        Precio=float(input("Introduzca el precio del producto: "))    
        while Precio<0 :# verifico que el precio no pueda ser un numero negativo
            print("Introduzca un precio valido")
            Precio=float(input("Introduzca el precio del producto: "))# le mando a poner denuevo el precio
    except ValueError:# Evito errores por valor invalido como string
        print("Introduzca un precio valido")
        Precio=float(input("Introduzca el precio del producto: "))

    try:# Pruebo el codigo
        cantidad=int(input("Introduzca la cantidad del producto: "))
        while cantidad<0: # verifico que la cantidad no pueda ser un numero negativo
            print("Introduzca una cantidad valida")
            cantidad=int(input("Introduzca la cantidad del producto: "))# le mando a poner denuevo la cantidad
    except ValueError:# Evito errores por valor invalido como string o float
        print("Introduzca una cantidad valida")
        cantidad=int(input("Introduzca la cantidad del producto: "))
    costo_total=Precio*cantidad # calculo el costo total

    print("""desea saber solo el costo total o todo el inventario?? 
    1.solo el costo total
    2.todo el inventario""") # Muestro las opciones

    respuesta=int(input("")) # Introduzco la respuesta
    while respuesta not in range(1,3): # verifico que la respuesta sea valida
        print("revise su respuesta e introduzca una respuesta valida")
        respuesta=input("")# le mando a poner denuevo la respuesta
    if respuesta==1: # si la respuesta es 1
        
        print(f"el costo total fue de {costo_total}") # muestro el costo total
        break

    elif respuesta==2: # si la respuesta es 2
        
        print(f"Producto: {Nombre}\nPrecio: {Precio}\nCantidad: {cantidad}\nCosto total: {costo_total}") # muestro todo el inventario


# este codigo se encarga de pedir al usuario el nombre, precio y cantidad de un producto y mostrar el costo total o todo el inventario