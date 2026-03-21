from estadisticas import *


arranque=True  # Establecemos la variable junto con el valor true para iniciar el ciclo
while arranque==True:
    print( "\033[94m" + """
                    ==========================================
                    ===bienvenido al programa de inventario===
                    ==========================================
                    
                    """+ "\033[0m") # Imprimimos el mensaje de bienvenida
    
    print("""
             1. para agregar productos al inventario
             2. para mostrar inventario
             3. para ver las estadisticas del inventario
             4. salir
             
             """) # Mostramos las opciones
    try:
        opcion=int(input("ingrese una opcion: "))   # Guardamos la opcion escogida
    
        while opcion<1 or opcion>4: 
            # Si la opcion es menor a 1 o mayor a 4 esto imprimira un mensaje
            print("\033[91m" + "ingrese una opcion valida"+ "\033[0m")
            opcion=int(input("ingrese una opcion: "))
    
        if opcion==1: # Si la opcion es 1 esto iniciara la funcion agregar_producto
            agregar_producto()
        elif opcion==2: # Si la opcion es 2 esto iniciara la funcion mostrar_inventario
            mostrar_inventario(inventario)
        elif opcion==3: # Si la opcion es 3 esto iniciara la funcion calcular_estadisticas
            calular_estadisticas(inventario)
        elif opcion==4: # Si la opcion es 4 esto ara que arranque sea false y asi cerrar el programa
            arranque=False

    except ValueError:
        print("\033[91m" + "ingrese una opcion valida"+ "\033[0m")

# El objetivo de esta semana fue aprender a usar las diversas estructuras de datos y manipularlas dependiendo de sus funcionalidades,tambien poner en practica el gran poder que tienen los condicionales sobre los menus interactivos y por ultimo las maneras mas optimas para manejar errores 
