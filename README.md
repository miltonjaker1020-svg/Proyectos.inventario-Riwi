# Sistema de Inventario
## Buenas tardes o buenos días (depende de cuándo veas esto). Aquí voy a explicar cómo funciona mi programa en Python
### Diagrama de flujo
![image alt](https://github.com/miltonjaker1020-svg/English-explanation/blob/main/Diagrama%20sin%20t%C3%ADtulo.drawio(2).png)
### Este programa es un script simple de inventario que le pide al usuario algunos datos sobre el producto:
1. ¿Cuál es su nombre?
2. ¿Cuál es su precio?
3. ¿Cuál es su cantidad?

### Luego le pregunta al usuario si quiere ver solo el precio final o los detalles completos de la compra. Si el usuario elige "solo el precio final", el sistema imprime "tienes que pagar...". Pero si elige la otra opción, imprime toda la información completa.

#### ejemplo:
```
¿cuál es el nombre del producto que quieres comprar?
Manzanas
```
```
¿cuál es su precio?
$5.40
```
```
¿cuál es su cantidad?
3
```
```
¿qué quieres ver?

1.el precio final
2.el detalle completo de la compra

2
```
```
Producto: Manzanas
Precio: $5.40
Cantidad: 3
costo total: 16.2
```


### ¿Cómo funciona?
#### Primero, el programa comienza con un bucle ```while true```, lo que significa que el programa seguirá ejecutándose hasta que una condición específica lo detenga.

#### Lo primero que el programa pregunta es cuál es el _nombre del producto_. El usuario introduce el nombre del producto y el programa verifica si el nombre es válido usando la función ```isalpha()```. Esta función revisa la entrada y verifica que solo contenga letras. Si el nombre no es válido, el programa vuelve a pedir el nombre del producto.

#### Luego, el programa pide el _precio del producto_ (el producto seleccionado). Este proceso está dentro de un bloque ```try-except```. El bloque try intenta convertir la entrada en un número tipo float, por lo que si el usuario introduce un valor inválido como un string (texto), el programa captura el error y vuelve a pedir el precio del producto. También verifica que el precio no sea un valor negativo.

#### Después de eso, el programa pide _la cantidad del producto_ (usando un proceso de validación similar), convierte la entrada en un número entero y verifica que no sea un número negativo.



#### Una vez que el programa tiene el precio y la cantidad, calcula el costo final multiplicando el precio por la cantidad.

#### Finalmente, el programa le pregunta al usuario qué información quiere ver. Puede elegir entre ver solo el costo final o el detalle completo de la compra. Dependiendo de la elección del usuario, el programa muestra el resultado correspondiente.

### Cómo usar el archivo 

#### Forma 1: Para personas que no saben usar Git ni herramientas de desarrollo

##### Si nunca has usado Git, repositorios o programas de programación avanzados, puedes usar el archivo de una forma muy sencilla.

##### Paso 1: entrar al repositorio
######  Primero debes abrir el enlace del repositorio público en tu navegador.

##### Paso 2: descargar el archivo
###### Tienes dos formas simples de hacerlo:

**Opción A (descargar todo el repositorio):**
###### 1. Busca el botón verde que dice **Code**.
###### 2. Haz clic en **Download ZIP**.
###### 3. Se descargará una carpeta comprimida en tu computadora.
###### 4. Descomprímela.

**Opción B (descargar solo el archivo):**
###### 1. Haz clic sobre el archivo que quieres usar.
###### 2. Busca el botón **Download** o **Raw**.
###### 3. Guárdalo en tu computadora.

#### Paso 3: ejecutar el programa
###### Si el archivo es un programa de Python:

1. Asegúrate de tener **Python instalado**. si no lo tiene instalado [click aqui para descargarlo](https://www.python.org/ftp/python/pymanager/python-manager-26.0.msix)
2. Abre la carpeta donde descargaste el archivo.
3. Haz doble clic o ejecútalo con Python.

#### Otra forma es abrir una terminal en esa carpeta y escribir:
```python inventario.py```
##### El programa se ejecutará y podrás usarlo.
------
#### Forma 2: Para personas que saben usar Git

##### Si ya conoces Git, la forma más común es **clonar el repositorio**.

##### Paso 1: copiar la URL del repositorio
###### En la página del repositorio, presiona **Code** y copia la URL.

##### Url:
```https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi.git```
> Esto descargará todo el repositorio en tu computadora.

#### Paso 3: entrar a la carpeta
```Proyectos.inventario-Riwi.git```
#### Paso 4: ejecutar el programa

**Opción 1 (botón de ejecutar):**
Presiona el botón **Run Python File**.

**Opción 2 (terminal integrada):**

Abre la terminal en VS Code y escribe:
```python inventario.py```



