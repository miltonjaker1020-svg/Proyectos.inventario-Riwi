# Sistema de Inventario (Versión con  CSV)

## Buenas tardes o buenos días (depende de cuándo veas esto). Aquí voy a explicar cómo funciona mi programa en Python

---

## Diagrama de flujo



---

## Este programa es un sistema de inventario que permite al usuario gestionar productos y almacenar la información en archivos CSV.

El sistema cuenta con las siguientes opciones:

1. Agregar productos
2. Mostrar inventario
3. Buscar productos
4. Actualizar productos
5. Eliminar productos
6. Ver estadísticas
7. Guardar CSV
8. Cargar CSV
9. Sobrescribir o fusionar inventario
10. Salir

---

## ¿Cómo funciona?

### Primero, el programa inicia con un bucle `while`, lo que permite que el sistema se ejecute continuamente hasta que el usuario decida salir.

```python
runner="0"
while runner=="0":
```

---

### Luego, se muestra un menú con las opciones disponibles y el usuario selecciona una opción:

```python
pregunta=int(input("¿que opcion desea ejecutar?"))
```

---

## Opción 1: Agregar producto

Cuando el usuario selecciona esta opción, el sistema solicita el nombre, precio y cantidad del producto:

```python
nombre=input("Ingrese el nombre del producto: ").lower()
precio=float(input("Ingrese el precio: "))
cantidad=int(input("Ingrese la cantidad: "))
```

Luego, se llama a la función que agrega el producto al inventario:

```python
agregar_producto(inventario, nombre ,precio,cantidad,diccionario)
```

Dentro de esta función se valida que el nombre sea correcto:

```python
while producto=="" or not producto.isalpha():
    print("ingrese un producto valido")
    producto=input("ingrese el nombre del producto: ")
```

También se validan cantidad y precio:

```python
while cantidad <= 0:
    cantidad=int(input("ingrese la cantidad de productos: "))

while precio <= 0:
    precio=float(input("ingrese el precio  del producto: "))
```

Finalmente, el producto se guarda como un diccionario dentro de la lista:

```python
diccionario={
    "producto":producto,    
    "cantidad":cantidad,
    "precio":precio
}
inventario.append(diccionario)
```

---

## Opción 2: Mostrar inventario

El sistema recorre la lista y muestra los productos:

```python
for i in inventario:
    print(f"producto: {i['producto']}  |  cantidad: {i['cantidad']}  |  precio total : {i['precio']} ")
```

Si no hay productos:

```python
if not inventario:
    print("no hay productos en el inventario")
```

---

## Opción 3: Buscar producto

El usuario ingresa un nombre y el sistema lo busca:

```python
for producto in inventario:
    if producto["producto"]==nombre:
        return producto
```

---

## Opción 4: Actualizar producto

Se permite modificar precio o cantidad:

```python
if nuevo_precio is not None:
    producto["precio"] = nuevo_precio

if nueva_cantidad is not None:
    producto["cantidad"] = nueva_cantidad
```

---

## Opción 5: Eliminar producto

El sistema elimina el producto si lo encuentra:

```python
for producto in inventario:
    if producto["producto"]==nombre:
        inventario.remove(producto)
```

---

## Opción 6: Estadísticas

Se calculan valores recorriendo el inventario:

```python
total_unidades += producto["cantidad"]
valor_total += producto["precio"]
```

También se identifica el producto más caro y el de mayor stock:

```python
if producto["precio"] > producto_mas_caro["precio"]:
    producto_mas_caro = producto
```

---

## Opción 7: Guardar CSV

El sistema guarda el inventario en un archivo CSV.

Primero valida que no esté vacío:

```python
if not inventario:
    print("Inventario vacio.")
    return
```

Luego abre el archivo:

```python
with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as file:
```

Obtiene los encabezados:

```python
encabezados = inventario[0].keys()
```

Y escribe los datos:

```python
writer = csv.DictWriter(file, fieldnames=encabezados)
writer.writeheader()
writer.writerows(inventario)
```

Si ocurre un error:

```python
except PermissionError:
    print("Error: No tienes permisos")
```

---

## Opción 8: Cargar CSV

El sistema lee el archivo CSV:

```python
with open(ARCHIVO_CSV, "r", newline="", encoding="utf-8") as archivo:
```

Valida el encabezado:

```python
if encabezado != ["nombre", "precio", "cantidad"]:
    print("Encabezado inválido.")
```

Recorre cada fila:

```python
for fila in lector:
```

Valida estructura:

```python
if len(fila) != 3:
    errores += 1
```

Convierte tipos:

```python
precio = float(precio)
cantidad = int(cantidad)
```

Y guarda los datos válidos:

```python
inventario_cargado.append({
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad
})
```

---

## Opción 9: Sobrescribir o fusionar inventario

El sistema pregunta al usuario:

```python
opcion = input("¿Sobrescribir inventario actual? (S/N): ").upper()
```

### Si elige sobrescribir:

```python
inventario = nuevo
```

### Si elige fusionar:

```python
if prod_actual["nombre"] == prod_nuevo["nombre"]:
    prod_actual["cantidad"] += prod_nuevo["cantidad"]
```

Y si el precio cambia:

```python
prod_actual["precio"] = prod_nuevo["precio"]
```

---

## Manejo de errores

El sistema utiliza `try-except` para evitar fallos:

```python
except ValueError:
    print("ingrese un valor valido")
```

También maneja errores de archivos:

```python
except FileNotFoundError:
    print("El archivo no existe.")
```

---

## Cómo ejecutar el programa

Ejecutar en terminal:

```bash
python principal_app.py
```

---

