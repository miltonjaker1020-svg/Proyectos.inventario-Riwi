import os
import csv


ARCHIVO_CSV = os.path.join("data.csv")


def guardar_csv(inventario, ruta="data.csv", incluir_header=True):
    
    if not inventario:
        print("Inventario vacio.")
        return
    
    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as file:
            
            campos = ["producto", "precio", "cantidad"]
            writer = csv.DictWriter(file, fieldnames=campos)
            
            if incluir_header:
                writer.writeheader()
                
            writer.writerows(inventario)

        print(f"Inventario guardado en: {ruta}")
        
    except Exception as e:
        print(f"Error al guardar: {e}")





def cargar_csv(ruta="data.csv"):
    inventario_cargado = []
    errores = 0
    
    try:    
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector, None)
            
            if encabezado != ["producto", "precio", "cantidad"]:
                print("Encabezado inválido.")
                return []
            
            for fila in lector:
                
                if len(fila) != 3:
                    errores += 1
                    continue
                
                nombre, precio, cantidad = fila
                
                try:
                    precio = float(precio)
                    cantidad = int(cantidad)
                    
                    if precio < 0 or cantidad < 0:
                        raise ValueError
                    
                    inventario_cargado.append({
                        "producto": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                
                except ValueError:
                    errores += 1
                    
        print(f"{errores} filas inválidas omitidas")
        return inventario_cargado
    
    except Exception as e:
        print(f"Error: {e}")
    
    return []
           