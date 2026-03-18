from aggproduct import *

def mostrar_inventario(inventario): # Establecemos la funcion mostrar_inventario
    run=True # Establecemos el iniciador
    while run==True: 
        print("\033[94m" + """
              ===================================================
              === BIENVENIDO AL APARTADO DE AGREGAR PRODUCTOS ===
              ===================================================
    
              """+ "\033[0m" ) # Imprimimos la bienvenida
        if not inventario: # Si el inventario esta vacio imprime un mensaje que dice que esta vacio
            print("\033[91m" + "no hay productos en el inventario"+ "\033[0m")
            
        else:
            for i in inventario: # lee los valores que estan dentro de la lista
                print(f"producto: {i["producto"]}  |  cantidad: {i['cantidad']}  |  precio total : {i['precio']} ")
        run=False # Simula un break
        
        
