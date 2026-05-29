# Aplicación Web

¡Hola! Este proyecto es una aplicación web súper sencilla e interactiva para gestionar info. Te permite agregar, editar, eliminar y guardar tus notas de forma segura para que no pierdas tu información al recargar la página.

## ¿Qué hace este programa?

Básicamente, es una lista inteligente de tareas. Sus funciones principales son:

* **Agrega notas:** Escribes tu texto, le das al botón "Agregar" y aparece inmediatamente en tu lista.
* **Edita notas:** ¿Te equivocaste al escribir? Cada nota tiene un botón de "Editar" que abre una ventanita rápida para corregir el texto.
* **Elimina notas:** Con un solo clic puedes borrar los apuntes que ya no necesites.
* **Doble guardado de seguridad:** Tus datos nunca se pierden porque se guardan en la memoria de tu navegador (Local Storage) y en una base de datos local (API).

---

## ¿Qué hay dentro del proyecto?

El proyecto consta de dos partes principales:

1. **`index.html`**: Es la "cara" de la aplicación. Aquí está el diseño visual, la caja para escribir y el espacio donde irán apareciendo la informacion

2. **`app.js`**: Aquí viven las instrucciones que le dicen a la página qué hacer cuando interactúas con ella.

---

## Exp´licacion del codigo (Partes Esenciales)

A continuación, te explico las funciones clave que hacen que esta aplicación funcione. Se comunican con el servidor usando **Fetch API**:

### 1. Obtener las notas al iniciar (GET)
Cuando abres la página, la aplicación va a la base de datos y trae todas la informacion guardada para mostrarla en pantalla.

```javascript
async function obtenerNotasDeAPI() {
    // Pedimos los datos al servidor local
    const respuesta = await fetch("http://localhost:3000/notas");
    
    if (respuesta.ok) {
        // Si responde bien, convertimos los datos a JSON
        const datosAPI = await respuesta.json();
        // Guardamos los datos en nuestro arreglo y los mostramos en pantalla
        notas = datosAPI; 
        renderizarLista();
    }
}
```

### 2. Guardar una nota nueva (POST)
Al escribir un texto y darle a "Agregar", el programa crea un objeto con un ID único y lo envía a la base de datos.

```javascript
// Creamos la nota con el texto del usuario
const nuevaNota = {
    id: Date.now().toString(), // Creamos un ID único usando la fecha
    texto: textoNota // El texto que ingresó el usuario
};

// La enviamos al servidor usando el método POST
const respuesta = await fetch("http://localhost:3000/notas", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(nuevaNota) // Convertimos la nota a texto para enviarla
});
```

### 3. Editar una nota existente (PUT)
Si el usuario hace clic en editar, le preguntamos el nuevo texto mediante una ventana emergente (`prompt`) y actualizamos exactamente esa nota en el servidor usando su ID.

```javascript
// Preguntamos el nuevo texto
const nuevoTexto = prompt("Edita tu nota:", nota.texto);

// Preparamos la nota actualizada
const notaActualizada = { ...nota, texto: nuevoTexto };

// Actualizamos en el servidor usando PUT y el ID de la nota
const respuesta = await fetch(`http://localhost:3000/notas/${nota.id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(notaActualizada)
});
```

### 4. Eliminar una nota (DELETE)
Cuando se hace clic en "Eliminar", le decimos a la base de datos que borre el registro que coincide con el ID de esa nota específica.

```javascript
// Enviamos la orden de eliminar usando el método DELETE y el ID
const respuesta = await fetch(`http://localhost:3000/notas/${nota.id}`, {
    method: 'DELETE'
});

if (respuesta.ok) {
    // Si se borró de la base de datos, la quitamos también de la pantalla
    ul.removeChild(li); 
}
```

---

## 🏃‍♂️ ¿Cómo usar y probar este proyecto en tu computadora?

Para que la aplicación funcione al 100% y pueda guardar datos de verdad, sigue estos pasos:

1. **Enciende el servidor de datos:** Asegúrate de tener Node.js instalado. Abre la terminal en la carpeta de este proyecto y ejecuta:
   ```bash
   npx json-server --watch db.json
   ```
   *(Deja esta terminal abierta mientras uses la app).*

2. **Abre la página:**
   Simplemente haz doble clic en el archivo `index.html` para abrirlo en tu navegador.

3. **¡A probar!**
   Agrega, edita y elimina notas. Puedes recargar la página y verás que todo tu progreso sigue intacto.

---

## ✅ Funciones técnicas implementadas

* **Manipulación del DOM:** Se usan métodos como `createElement` y `removeChild`.
* **Validaciones:** Control estricto de inputs para evitar datos vacíos.
* **Local Storage:** `localStorage.setItem` y `getItem` como respaldo de sesión.
* **Fetch API (Promesas):** Conexión asíncrona real (`async/await`) manejando métodos `GET`, `POST`, `PUT` y `DELETE`.
