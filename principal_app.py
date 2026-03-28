from modulo_servicios import *
from archivos import *
color=colores()


runner="0"
while runner=="0":

    

    print(color['AZUL'] + """
            ===========================================
            === BIENVENIDO AL SISTEMA DE INVENTARIO ===
            ===========================================

                            Opciones
            1. Agregar
            2. Mostrar
            3. Buscar
            4. Actualizar
            5. Eliminar
            6. Estadísticas
            7. Guardar CSV
            8. Cargar CSV
            9. Sobreescribir CSV
            10. Salir
            
            """+ color['RESET']) 

   
    try:
        pregunta=int(input("¿que opcion desea ejecutar?"))

        if pregunta==1:
            while True:

                nombre=input(f"{color['AZUL']} Ingrese el nombre del producto que desea agregar, {color['RESET']}").lower()
                precio=float(input(f"{color['AZUL']} Ingrese el nuevo precio del producto que desea agregar, {color['RESET']}"))
                cantidad=int(input(f"{color['AZUL']} Ingrese la nuevo cantidad del producto que desea agregar, {color['RESET']}"))
                agregar_producto(inventario, nombre ,precio,cantidad,diccionario)
                break

        elif pregunta==2:
            mostrar_inventario(inventario)

        elif pregunta==3:
            producto=input(f"{color['AZUL']} Ingrese el nombre del producto que desea agregar,  {color['RESET']} ").lower()
            mostrar=buscar_producto(inventario, producto)
            print(mostrar)

        elif pregunta==4:
            nombre=input(f"{color['AZUL']} Ingrese el nombre del produto que desa actualizar,  {color['RESET']} ")
            
            cantidad_input = input("Nueva cantidad (Enter para no cambiar): ")
            precio_input = input("Nuevo precio (Enter para no cambiar): ")
            
            nuevo_precio = float(precio_input) if precio_input != "" else None
            nueva_cantidad = int(cantidad_input) if cantidad_input != "" else None

            print(actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad))

        elif pregunta==5:

            nombre=input(f"{color['AZUL']} Ingrese el nombre del producto que desea eliminar, {color['RESET']}")
            resultado=eliminar_producto(inventario, nombre)
            if resultado == "no se encontro la referencia":
                print(f" {color['ROJO']}no existe, {color['RESET']}")
    


        elif pregunta==6:
            calcular_estadisticas(inventario)


        elif pregunta==7:
            guardar_csv(inventario,"data.csv")

        elif pregunta==8:
            inventario = cargar_csv("data.csv")
            
        elif pregunta==9:
           nuevo = cargar_csv(ARCHIVO_CSV)

           if nuevo:
            opcion = input("¿Sobrescribir inventario actual? (S/N): ").upper()
            
            if opcion == "S":
                inventario = nuevo
                print("Inventario reemplazado.")
            
            elif opcion == "N":
                # FUSIÓN
                for prod_nuevo in nuevo:
                    encontrado = False
                    
                    for prod_actual in inventario:
                        if prod_actual["producto"] == prod_nuevo["producto"]:
                            
                            # sumar cantidad
                            prod_actual["cantidad"] += prod_nuevo["cantidad"]
                            
                            # actualizar precio si es distinto
                            if prod_actual["precio"] != prod_nuevo["precio"]:
                                prod_actual["precio"] = prod_nuevo["precio"]
                            
                            encontrado = True
                            break
                    
                    if not encontrado:
                        inventario.append(prod_nuevo)
                
                print("Inventario fusionado.")

        elif pregunta==10:
         print("saliendo....")
         break

    except Exception as e:
        print(f"error,{e}")


