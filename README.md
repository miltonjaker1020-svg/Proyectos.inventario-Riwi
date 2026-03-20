## H2 feature
### buenos dias, el dia de hoy subi un proyecto el cual es un inventario digitalizado que tiene funciones como:
1. #### Agregar productos
2. #### Mostrar el inventario
3. #### Ver las estadisticas del inventario
---
### Diagrama de flujo
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/fc0fed329fb5534054acac49511fbbc59b586769/Diagrama%20sin%20t%C3%ADtulo.png)
#
### Explicacion de cada funcion
#### Agregar producto
##### Primero que nada se establecen los colores que se van a usar en el programa al momento de mostrar algo en la consola
```
    AZUL = "\033[94m"
    BLANCO = "\033[97m"
    VERDE = "\033[92m"
    RESET = "\033[0m"
    ROJO = "\033[91m"

```
> Intente hacer una funcion llamada ```def colores()``` para asi utilisarlos mas adelante pero lo deje como proyeccion a futuro
#
##### Ahora se establece una variable llamada confirmar junto con su valor true. Ademas de iniciar un bucle claro esta
```
   confirmar=True #Establesco la variable confirmar y que esta contenga un true para no usar el while true
    while confirmar==True:
```
>cabe recalcar que se uso este metodo para aprender a evitar usar ```while true``` ya que esto es una mala practica. Lo que quiere decir este bloque de codigo es que siempre que ```confirmar``` sea verdadero(true) se repetira lo que esta debajo ```while```
#

##### Se Muestra un mensaje de bienvenida
```

   print(AZUL + """
            ===================================================
            === BIENVENIDO AL APARTADO DE AGREGAR PRODUCTOS ===
            ===================================================
            
            """+ RESET)
```
>Aqui se usan los colores establecidos anterior mente
#
##### Se le pide al usuario que ingrese el nombre del producto, ademas valida que este no este vacio y no contenga numero
```
 
    #Ingreso del producto

        producto=input("ingrese el nombre del producto: ")
    



    #Validacion de que el producto sea un string y tmabien que no este vacio

        while producto=="" or not producto.isalpha():
            print(ROJO + "ingrese un producto valido"+ RESET)
            producto=input("ingrese el nombre del producto: ")
```
> Uso ```while``` para que ocurra esto repetidamente y que no lo devuelva a al mensaje de bienvenida 
#
##### Se le pide al usuario la cantidad del producto y el precio total a pagar por esos productos y valida que esta informacion no contenga numeros negativos
```
 try: 
            cantidad=int(input("ingrese la cantidad del producto: "))  # Pedimos la cantidad del producto

             

            while cantidad <= 0:           # Validamos que no sea un numero negativo o 0

                print(ROJO + "ingrese una cantidad valida"+ RESET)
                cantidad=int(input("ingrese la cantidad de productos: "))
        
        
            precio=float(input("ingrese el precio  de los productos: "))   # Pedimos el precio del producto

            while precio <= 0:     # Validamos que no sea un numero negativo o menor a 0

                print(ROJO + "ingrese un precio valido"+ RESET)
                precio=float(input("ingrese el precio  del producto: "))
```
> Aqui comensamos un un try ya que desde aqui el sistema comiensa a pedir tipos de datos los cuales pueden causar un error de valor, y como dije antes uso  ```while``` para no volver a cargar una nueva iteraccion
#
##### Dependiendo de si el producto existe este se actualiza o agrega
```
            if producto in inventario:    # Establecemos que si el producto ya existe este sobre escriba la lista

                inventario[producto]["cantidad"]+=cantidad
                totalactualizado=inventario[producto]["precio"]/inventario[producto]["cantidad"]
                inventario[producto]["precio"]+=totalactualizado*cantidad

            else:   # Se establece el diccionario

                diccionario={
                "producto":producto,    
                "cantidad":cantidad,
                "precio":precio }
                inventario.append(diccionario)
```     
> Aqui uso condicionales(if y else) para dependiendo de si el producto ingresado exista, este agrege la cantidad nueva, luego establecemos la variable ```totalactualizado``` la cual saca el valor unitario del producto por si el cliente desea usarlo mas adelante,y  le actualisamos el valor de la compra. Ahora si el  producto no existe este se guarda en un diccionario y este diccionario se guarda en una lista llamada ``` inventario``` 
#
##### Se le pregunta  al usuario si desea ingresar otro producto

```       
          opcion=input("desea agregar otro producto? (si/no): ").lower()
          while confirmar not in ("si","no"):  # Verificamos que no pongo palabras incorrectas

                print(ROJO + "ingrese un valor valido"+ RESET)
                opcion=input("desea agregar otro producto? (si/no): ").lower()
            
            if opcion=="no":   # Si pone no cerramos el siclo con un confirmar false
                confirmar=False
                
          

        except ValueError:  # Capturamos el error
            print(ROJO + "ingrese un valor valido"+ RESET)
            continue
```    
> Se usa un while para validar que el usuario si ingreso las palabras clave. si la entrada ``` opcion ``` es no, esto cambiara el valor de ```confirmar``` por false cerrando asi el programa
---
#### Mostrar inventario

##### Establecemos un inicador mas el bucle asociado a su condicion
 ```
  run=True # Establecemos el iniciador
    while run==True: 
 ```
 > Como se menciono anterior mente esto se hace par aevitar la mala practica que conlleva usar  ```while true```
#
##### Se valida que el inventario no este vacio y si este no lo esta se muestra en consola todo el inventario registrado
```
        if not inventario: # Si el inventario esta vacio imprime un mensaje que dice que esta vacio

            print("\033[91m" + "no hay productos en el inventario"+ "\033[0m")
            
        else:
            for i in inventario: # lee los valores que estan dentro de la lista
                print(f"producto: {i['producto']}  |  cantidad: {i['cantidad']}  |  precio total : {i['precio']} ")

        run=False # Simula un break
```        
>Se usa ```for``` ya que este es muy bueno para recorrer listas de manera rapida y simple
---
### Ver estadisticas
#### Se le muestra al usuario un menu el cual muestra a que operacion esta asociado cada numero
```
   print( "\033[94m" + """                                                                 
                            ============================================
                            ===bienvenido al programa de estadisticas===                 
                            ============================================
                            
                            """+ "\033[0m" ) # Imprimimos una bienvenida
    print("""que desea hacer
          1. ver valor total del inventario
          2. ver la cantidad total de productos registrados
          """)
```
#
#### Se le pregunta al usuario que desea hacer y se muestra solo lo que selecciono
```
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
```
> Aqui se establecieron variables(```total_cantidad```,```total_precio```) antes del ```for``` para almacenar en estas los valores totales de cantidad y precio

### Como se ve en consola:
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/6ed20a4c54cd6ffe75d92ea6dc32c787e84952f3/1.png)
#
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/6ed20a4c54cd6ffe75d92ea6dc32c787e84952f3/2.png)
#
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/6ed20a4c54cd6ffe75d92ea6dc32c787e84952f3/3.png)
#
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/6ed20a4c54cd6ffe75d92ea6dc32c787e84952f3/4.png)
-----
#### Con multiples productos
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/6ed20a4c54cd6ffe75d92ea6dc32c787e84952f3/5.png)
#
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/6ed20a4c54cd6ffe75d92ea6dc32c787e84952f3/6.png)
#
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/6ed20a4c54cd6ffe75d92ea6dc32c787e84952f3/7.png)
#
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/6ed20a4c54cd6ffe75d92ea6dc32c787e84952f3/8.png)
#
![image alt](https://github.com/miltonjaker1020-svg/Proyectos.inventario-Riwi/blob/6ed20a4c54cd6ffe75d92ea6dc32c787e84952f3/9.png)


