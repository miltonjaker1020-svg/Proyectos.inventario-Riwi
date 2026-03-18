inventario=[]
def colores():
    AZUL = "\033[94m"
    BLANCO = "\033[97m"
    VERDE = "\033[92m"
    RESET = "\033[0m"
    ROJO = "\033[91m"

def agregar_producto():
    #colores para el programa
    AZUL = "\033[94m"
    BLANCO = "\033[97m"
    VERDE = "\033[92m"
    RESET = "\033[0m"
    ROJO = "\033[91m"
    
   
    confirmar=True
    while confirmar==True:
        
    #mensaje de bienvenida
        print(AZUL + """
            ===================================================
            === BIENVENIDO AL APARTADO DE AGREGAR PRODUCTOS ===
            ===================================================
            
            """+ RESET)
    
    
    #ingreso del producto
        producto=input("ingrese el nombre del producto: ")
    
    #validacion de que el producto sea un string y tmabien que no este vacio
        while producto=="" or not producto.isalpha():
            print(ROJO + "ingrese un producto valido"+ RESET)
            producto=input("ingrese el nombre del producto: ")
        
        try: 
            cantidad=int(input("ingrese la cantidad del producto: "))
            while cantidad <= 0:
                print(ROJO + "ingrese una cantidad valida"+ RESET)
                cantidad=int(input("ingrese la cantidad de productos: "))
        
        
            precio=float(input("ingrese el precio  de los productos: "))
            while precio <= 0:
                print(ROJO + "ingrese un precio valido"+ RESET)
                precio=float(input("ingrese el precio  del producto: "))

           
            if producto in inventario:
                inventario[producto]["cantidad"]+=cantidad
                totalactualizado=inventario[producto]["precio"]/inventario[producto]["cantidad"]
                inventario[producto]["precio"]+=totalactualizado*cantidad
            else:
                diccionario={
                "producto":producto,    
                "cantidad":cantidad,
                "precio":precio
                
             }
                inventario.append(diccionario)
            
            if producto in inventario:
                inventario[producto]["cantidad"]+=cantidad
                
            print(VERDE + "✔ producto agregado con exito"+ RESET)
            confirmar=input("desea agregar otro producto? (si/no): ").lower()
            while confirmar not in ("si","no"):
                print(ROJO + "ingrese un valor valido"+ RESET)
                confirmar=input("desea agregar otro producto? (si/no): ").lower()
            
            if confirmar=="no":
                confirmar=False
                
            elif confirmar=="si":
                confirmar=True

        except ValueError:
            print(ROJO + "ingrese un valor valido"+ RESET)
            continue
