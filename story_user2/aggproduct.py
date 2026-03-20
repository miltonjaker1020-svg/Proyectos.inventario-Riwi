inventario=[] # Establecemos una lista llama inventario
def colores(): # proyeccion a futuro ya que no me salio Xc
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
    
   
    confirmar=True #Establesco la variable confirmar y que esta contenga un true para no usar el while true
    while confirmar==True:
        
    #Mensaje de bienvenida
        print(AZUL + """
            ===================================================
            === BIENVENIDO AL APARTADO DE AGREGAR PRODUCTOS ===
            ===================================================
            
            """+ RESET)
    
    
    #Ingreso del producto
        producto=input("ingrese el nombre del producto: ")
    
    #Validacion de que el producto sea un string y tmabien que no este vacio
        while producto=="" or not producto.isalpha():
            print(ROJO + "ingrese un producto valido"+ RESET)
            producto=input("ingrese el nombre del producto: ")
        
        try: 
            cantidad=int(input("ingrese la cantidad del producto: ")) # Pedimos la cantidad del producto
            while cantidad <= 0: # Validamos que no sea un numero negativo o 0
                print(ROJO + "ingrese una cantidad valida"+ RESET)
                cantidad=int(input("ingrese la cantidad de productos: "))
        
        
            precio=float(input("ingrese el precio  de los productos: ")) # Pedimos el precio del producto
            while precio <= 0: # Validamos que no sea un numero negativo o menor a 0
                print(ROJO + "ingrese un precio valido"+ RESET)
                precio=float(input("ingrese el precio  del producto: "))

           
            if producto in inventario:# Establecemos que si el producto ya existe este sobre escriba la lista
                inventario[producto]["cantidad"]+=cantidad
                totalactualizado=inventario[producto]["precio"]/inventario[producto]["cantidad"]
                inventario[producto]["precio"]+=totalactualizado*cantidad
            else: # Se establece el diccionario
                diccionario={
                "producto":producto,    
                "cantidad":cantidad,
                "precio":precio
                
             }
                inventario.append(diccionario) # Guarda el diccionario en la lista inventario
            
           
                
            print(VERDE + "✔ producto agregado con exito"+ RESET) # Le hacemos saber al cliente que se registro correctamente el producto
            opcion=input("desea agregar otro producto? (si/no): ").lower()  # Preguntamos si quiere agregar otro producto
            while confirmar not in ("si","no"): # Verificamos que no pongo palabras incorrectas
                print(ROJO + "ingrese un valor valido"+ RESET)
                confirmar=input("desea agregar otro producto? (si/no): ").lower()
            
            if opcion=="no":  # Si pone no cerramos el siclo con un confirmar false
                confirmar=False
                
            elif opcion=="si": # Si pone si inicia otra iteracion con un confirmar true
                confirmar=True

        except ValueError:  # Capturamos el error
            print(ROJO + "ingrese un valor valido"+ RESET)
            continue

