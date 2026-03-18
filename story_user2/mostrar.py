from aggproduct import *

def mostrar_inventario(inventario):
    run=True
    while run==True:
        print("\033[94m" + """
              ===================================================
              === BIENVENIDO AL APARTADO DE AGREGAR PRODUCTOS ===
              ===================================================
    
              """+ "\033[0m" )
        if not inventario:
            print("\033[91m" + "no hay productos en el inventario"+ "\033[0m")
            
        else:
            for i in inventario:
                print(f"producto: {i["producto"]}  |  cantidad: {i['cantidad']}  |  precio total : {i['precio']} ")
        run=False
        
        
