from mostrar import *

def calular_estadisticas(inventario):
    print( "\033[94m" + """
                            ============================================
                            ===bienvenido al programa de estadisticas===                 
                            ============================================
                            
                            """+ "\033[0m" )
    if not inventario:
        print("\033[91m" + "no hay productos en el inventario"+ "\033[0m")
        
    total_cantidad=0
    total_precio=0
    
    for i in inventario:
        total_cantidad+=i['cantidad']
        total_precio+=i['precio']

    print("cantidad total de productos: ",total_cantidad)
    print("precio total de productos: ",total_precio*total_cantidad)