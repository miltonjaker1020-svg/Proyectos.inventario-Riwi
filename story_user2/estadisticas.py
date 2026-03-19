from mostrar import * # Inportamos las funciones del archivo mostrar

def calular_estadisticas(inventario):
    print( "\033[94m" + """                                                                 
                            ============================================
                            ===bienvenido al programa de estadisticas===                 
                            ============================================
                            
                            """+ "\033[0m" ) # Imprimimos una bienvenida
    print("""que desea hacer
          1. ver valor total del inventario
          2. ver la cantidad total de productos registrados
          """)
    try:
        eleccion=int(input("ingrese la opcion que desea escoger"))
        if not inventario: # Verificamos que hayan valores en el inventario
            print("\033[91m" + "no hay productos en el inventario"+ "\033[0m")
            
        total_cantidad=0 # Establecemos acumuladores 
        total_precio=0 
        
        for i in inventario:
            total_cantidad+=i['cantidad'] # acumulamos los valores
            total_precio+=i['precio']

        if eleccion==1:
        
            print("cantidad total de productos: ",total_cantidad) # Imprimimos los valores acumulados

        elif eleccion==2:
            print("precio total de productos: $",total_precio*total_cantidad) 
            
    except ValueError:
        print("\033[91m" + "error coloque una opcion valida" + "\033[0m")
        eleccion=int(input("ingrese la opcion que desea escoger"))
