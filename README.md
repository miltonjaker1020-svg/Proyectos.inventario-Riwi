
#  - Guia Completa del Proyecto: Inventario de Productos

Este proyecto es una aplicacion web muy sencilla para controlar el inventario de una tienda. Sirve para agregar productos, verlos en una lista, editarlos y borrarlos.

Lo importante de este proyecto es que los datos no se pierden. Se guardan tanto en la memoria de tu propio navegador (para que sigan ahi si recargas la pagina) como en un servidor local (para simular una base de datos real en internet).

---

## Estructura General

El proyecto esta formado por 4 archivos que trabajan en equipo:
1. **index.html**: Es la estructura basica, las cajas donde escribes y los botones.
2. **styles.css**: Es la pintura y el acomodo de las cosas para que no se vea feo.
3. **db.json**: Es el archivador (base de datos) que simula estar en internet.
4. **app.js**: Es el cerebro que hace que todo funcione y cobren vida los botones.

---

## Explicacion de cada archivo y sus partes 

### 1. index.html 
Este archivo solo crea los elementos que el usuario puede ver y tocar.

* **El formulario para escribir datos:**
```html
<form id="formularioProducto">
    <input type="text" id="nombreProducto" placeholder="Nombre del producto" required>
    <input type="number" id="precioProducto" placeholder="Precio ($)" step="0.01" required>
    <button type="submit">Agregar Producto</button>
</form>
```

* **El boton para traer los datos del servidor:**
```html
<button id="btnSincronizar" class="boton">Sincronizar con API </button>
```

* **La lista vacia que luego se llena con Javascript:**
```html
<ul id="listaProductos"></ul>
```

---

### 2. styles.css (El diseno y los colores)
Se encarga de que la aplicacion sea comoda de usar y se vea ordenada.

* **Acomodar el formulario en fila hacia abajo:**
```css
form { 
    display: flex; 
    flex-direction: column; 
    gap: 10px; 
    margin-bottom: 20px; 
}
```

* **Ocultar los carteles de aviso por defecto:**
```css
.mensaje { padding: 10px; margin-bottom: 10px; border-radius: 4px; display: none; }
.exito { background-color: #d4edda; color: #155724; }
.error { background-color: #f8d7da; color: #721c24; }
```

* **Darle forma de barra a cada producto de la lista:**
```css
li { 
    background: #f4f4f9; 
    margin: 5px 0; 
    padding: 10px; 
    display: flex; 
    justify-content: space-between; 
    align-items: center; 
    border: 1px solid #ddd; 
}
```

---

### 3. db.json (La base de datos de mentira)
Es un archivo de texto simple que simula un servidor externo en internet. guarda los productos de esta forma:

```json
{
  "productos": [
    {
      "id": "1",
      "nombre": "Teclado Mecanico RGB",
      "precio": 85.50
    },
    {
      "id": "2",
      "nombre": "Raton Inalambrico",
      "precio": 45.00
    }
  ]
}
```

---

### 4. app.js (El cerebro del proyecto)
Aqui esta toda la logica. Es el archivo mas importante.

* **Revisar la memoria del navegador al abrir la pagina (Local Storage):**
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const datosLocales = localStorage.getItem('productos');
    if (datosLocales) {
        productos = JSON.parse(datosLocales);
        renderizarProductos();
    }
});
```

* **El truco de ponerle un ID unico a cada fila de la lista:**
```javascript
const li = document.createElement('li');
li.id = `prod-${producto.id}`; // Le pega una etiqueta como prod-12345
```

* **Borrar el producto de la pantalla usando ese ID:**
```javascript
const nodoAEliminar = document.getElementById(`prod-${id}`);
if (nodoAEliminar) {
    listaProductos.removeChild(nodoAEliminar); // Lo quita del mapa visual
}
```

* **La funcion para prender y apagar los carteles de aviso por 3 segundos:**
```javascript
const mostrarMensaje = (texto, tipo) => {
    contenedorMensaje.textContent = texto;
    contenedorMensaje.className = `mensaje ${tipo}`;
    contenedorMensaje.style.display = 'block';
    
    setTimeout(() => {
        contenedorMensaje.style.display = 'none';
    }, 3000);
};
```

* **Pedir los datos al servidor (Metodo GET):**
```javascript
const respuesta = await fetch(API_URL);
const datosAPI = await respuesta.json();
productos = datosAPI; // Guarda lo que trajo del servidor
```

* **Mandar un nuevo producto al servidor (Metodo POST):**
```javascript
const respuesta = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(nuevoProducto)
});
```

* **Modificar un producto existente (Metodo PUT):**
```javascript
const respuesta = await fetch(`${API_URL}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(productoActualizado)
});
```

* **Borrar un producto del servidor (Metodo DELETE):**
```javascript
const respuesta = await fetch(`${API_URL}/${id}`, {
    method: 'DELETE'
});
```

---

## Como utilizar la aplicacion paso a paso

Sigue estos pasos para probar todas las funciones y ver como trabaja el codigo en tiempo real:

### Paso 1: Encender el servidor de mentira
1. Abre tu terminal o consola de comandos.
2. Ve hasta la carpeta donde tienes guardados tus 4 archivos.
3. Ejecuta el siguiente comando para activar `json-server`:
   ```bash
   json-server --watch db.json
   ```
   *Veras un mensaje en la consola que dice que el servidor esta corriendo en una direccion como `http://localhost:3000/productos`.*

### Paso 2: Abrir la aplicacion en el navegador
1. Busca tu archivo `index.html` en la carpeta y dale doble click para abrirlo en tu navegador web.
2. Abre las herramientas de desarrollador presionando la tecla **F12** y ve a la pestana llamada **Consola**. Esto sirve para ver los mensajes internos del codigo.

### Paso 3: Probar la sincronizacion (Metodo GET)
1. Haz click en el boton azul que dice **Sincronizar con API**.
2. Veras que en la pantalla aparecen magicamente los elementos que estaban guardados dentro de tu archivo `db.json`.
3. En la consola de F12 aparecera un mensaje confirmando que se descargaron los datos correctamente.

### Paso 4: Agregar un nuevo producto (Metodo POST)
1. En la caja de texto escribe el nombre de un producto (por ejemplo: `Monitor Gamer`).
2. En la caja de abajo escribe un precio (por ejemplo: `250`).
3. Haz click en el boton **Agregar Producto**.
4. El producto aparecera abajo en la lista al instante. Javascript uso `appendChild` para meterlo en el HTML, lo guardo en el `Local Storage` del navegador y ademas lo mando al archivo `db.json` de tu computadora. Si abres tu archivo `db.json`, veras el nuevo producto anotado al final.

### Paso 5: Editar un producto existente (Metodo PUT)
1. Ve a cualquier producto de la lista y haz click en su boton amarillo que dice **Editar**.
2. Te aparecera una ventana flotante preguntando el nuevo nombre. Modificalo y dale aceptar.
3. Luego te saldra otra ventana preguntando el nuevo precio. Cambialo y dale aceptar.
4. El texto en la pantalla cambiara de inmediato y el archivo `db.json` se actualizara con los nuevos valores.

### Paso 6: Borrar un producto (Metodo DELETE)
1. Haz click en el boton rojo que dice **Eliminar** en cualquiera de tus productos.
2. El producto desaparecera de la pantalla inmediatamente de forma limpia (Javascript uso `removeChild`).
3. Tambien se borrara de la memoria de tu navegador y del archivo `db.json`.

### Paso 7: Comprobar que no se pierden los datos (Local Storage)
1. Cierra la pestana de tu navegador o refresca la pagina presionando **F5**.
2. Veras que la lista no se borra, los productos siguen ahi. Esto pasa porque la aplicacion fue a buscar los datos guardados en el `Local Storage` antes de pintar la pantalla.
