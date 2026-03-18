from estadisticas import *


arranque=True
while arranque==True:
    print( "\033[94m" + """
                    ==========================================
                    ===bienvenido al programa de inventario===
                    ==========================================
                    
                    """+ "\033[0m")
    
    print("""
             1. para agregar productos al inventario
             2. para mostrar inventario
             3. para ver las estadisticas del inventario
             4. salir
             
             """)
    
    opcion=int(input("ingrese una opcion: "))
    if opcion==1:
        agregar_producto()
    elif opcion==2:
        mostrar_inventario(inventario)
    elif opcion==3:
        calular_estadisticas(inventario)
    elif opcion==4:
        arranque=False