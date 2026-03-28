


inventario=[]   
diccionario= {}
def colores():
    return { # proyeccion a futuro ya que no me salio Xc
        "AZUL" : "\033[94m",
        "BLANCO" : "\033[97m",
        "VERDE" : "\033[92m",
        "RESET" : "\033[0m",
        "ROJO ": "\033[91m",
        }

color=colores()

def agregar_producto(inventario,producto,precio,cantidad,diccionario):
    #colores para el programa
    AZUL = "\033[94m"
    BLANCO = "\033[97m"
    VERDE = "\033[92m"
    RESET = "\033[0m"
    ROJO = "\033[91m"
    
   
    #Establesco la variable confirmar y que esta contenga un true para no usar el while true
    
        
    #Mensaje de bienvenida
    print(AZUL + """
            ===================================================
            === BIENVENIDO AL APARTADO DE AGREGAR PRODUCTOS ===
            ===================================================
            
            """+ RESET)
    
    
    #Ingreso del producto
    
    for p in inventario:
        if p["producto"].lower() == producto.lower():
            print(ROJO + "ese producto ya se encuentra en el inventario"+ RESET)
            return
        
    #Validacion de que el producto sea un string y tmabien que no este vacio
    while producto=="" or not producto.isalpha():
            print(ROJO + "ingrese un producto valido"+ RESET)
            producto=input("ingrese el nombre del producto: ")
        
    try: 
        # Pedimos la cantidad del producto
            while cantidad <= 0: # Validamos que no sea un numero negativo o 0
                print(ROJO + "ingrese una cantidad valida"+ RESET)
                cantidad=int(input("ingrese la cantidad de productos: "))
        
        
            # Pedimos el precio del producto
            while precio <= 0: # Validamos que no sea un numero negativo o menor a 0
                print(ROJO + "ingrese un precio valido"+ RESET)
                precio=float(input("ingrese el precio  del producto: "))

           
            # Establecemos que si el producto ya existe este sobre escriba la lista
            diccionario={
            "producto":producto,    
            "cantidad":cantidad,
            "precio":precio
             }
            inventario.append(diccionario) # Guarda el diccionario en la lista inventario
            
           
            
            print(VERDE + "✔ producto agregado con exito"+ RESET) # Le hacemos saber al cliente que se registro correctamente el producto
            # Preguntamos si quiere agregar otro producto
            
            
            
            return diccionario, inventario

    except ValueError:  # Capturamos el error
            print(ROJO + "ingrese un valor valido"+ RESET)
            

def actualizar_producto(inventario, nombre , nuevo_precio=None, nueva_cantidad=None):

    for producto in inventario:
        if producto["producto"].lower() == nombre.lower():
            
            if nuevo_precio is not None:
                producto["precio"] = nuevo_precio

            if nueva_cantidad is not None:
                producto["cantidad"] = nueva_cantidad
                
            return "producto actualizado"
        
    return  color['ROJO'] + "no se encontro la referencia"+  color['RESET']
            
def eliminar_producto(inventario, nombre):

    


    for producto in inventario:
        if producto["producto"]==nombre:
            inventario.remove(producto)
            return "producto eliminado"
        
    return "no se encontro la referencia" # simpre pone esto

    
def calcular_estadisticas(inventario):
    if not inventario:
        print("El inventario esta vacio")
        return
    
    
    else:
        total_unidades = 0
        valor_total = 0

        producto_mas_caro = inventario[0]
        producto_mayor_stock = inventario[0]
        
        for producto in inventario:
            
            total_unidades += producto["cantidad"]
            valor_total += producto["precio"]

            if producto["precio"] > producto_mas_caro["precio"]:
                producto_mas_caro = producto

            if producto["cantidad"] > producto_mayor_stock["cantidad"]:
                producto_mayor_stock = producto
                
                
        print(f"Unidades totales: {total_unidades}")
        print(f"Valor total: {valor_total}")
        print(f"Producto más caro: {producto_mas_caro['producto']} y su precio es: {producto_mas_caro['precio']}")
        print(f"Mayor stock: {producto_mayor_stock['producto']} y su stock es: {producto_mayor_stock['cantidad']}")
    


def buscar_producto(inventario, nombre):
    
    
    for producto in inventario:
        if producto["producto"]==nombre:
            return producto

    if nombre not in diccionario:
        return  color['ROJO'] + "ese producto no se encuentra en el inventario" +    color['RESET']

    
    return None


def mostrar_inventario(inventario): # Establecemos la funcion mostrar_inventario
    run=True # Establecemos el iniciador
    while run==True: 
        print("\033[94m" + """
              ========================================================
              === BIENVENIDO AL APARTADO QUE MUESTRA,EL INVENTARIO ===
              ========================================================
    
              """+ "\033[0m" ) # Imprimimos la bienvenida
        if not inventario: # Si el inventario esta vacio imprime un mensaje que dice que esta vacio
            print("\033[91m" + "no hay productos en el inventario"+ "\033[0m")
            
        else:
            for i in inventario: # lee los valores que estan dentro de la lista
                print(f"producto: {i['producto']}  |  cantidad: {i['cantidad']}  |  precio total : {i['precio']} ")
        run=False # Simula un break




