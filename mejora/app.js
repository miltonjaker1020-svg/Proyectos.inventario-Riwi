
const API_URL = 'http://localhost:3000/productos';
let productos = []; 

// elementos del DOM
const formularioProducto = document.getElementById('formularioProducto');
const nombreInput = document.getElementById('nombreProducto');
const precioInput = document.getElementById('precioProducto');
const listaProductos = document.getElementById('listaProductos');
const btnSincronizar = document.getElementById('btnSincronizar');
const contenedorMensaje = document.getElementById('contenedorMensaje');

document.addEventListener('DOMContentLoaded', () => {
    // Cargar datos iniciales desde Local Storage al recargar la página 
    const datosLocales = localStorage.getItem('productos');
    if (datosLocales) {
        productos = JSON.parse(datosLocales);
        console.log('Datos recuperados de Local Storage:', productos);
        renderizarProductos();
    }
});


const mostrarMensaje = (texto, tipo) => {
    contenedorMensaje.textContent = texto;
    contenedorMensaje.className = `mensaje ${tipo}`;
    contenedorMensaje.style.display = 'block';
    
    // Ocultar el mensaje automáticamente después de 3 segundos
    setTimeout(() => {
        contenedorMensaje.style.display = 'none';
    }, 3000);
};

// Valida que los campos no esten vacíos
const validarDatos = (nombre, precio) => {
    if (nombre.trim() === '' || isNaN(precio) || precio <= 0) {
        mostrarMensaje('Por favor, ingresa un nombre válido y un precio mayor a 0.', 'error');
        return false;
    }
    return true;
};


const renderizarProductos = () => {
    // Limpiar la lista 
    listaProductos.innerHTML = '';

    productos.forEach(producto => {
        // Crear elemento li del producto
        const li = document.createElement('li');
        li.id = `prod-${producto.id}`; //Li identificada con un id//

        // Contenedor de texto del producto
        const infoProducto = document.createElement('span');
        infoProducto.textContent = `${producto.nombre} - $${Number(producto.precio).toFixed(2)}`;
        li.appendChild(infoProducto);

        // Contenedor para los botones 
        const contenedorBotones = document.createElement('div');

        // Botón Editar 
        const btnEditar = document.createElement('button');
        btnEditar.textContent = 'Editar';
        btnEditar.style.backgroundColor = '#ffc107';
        btnEditar.onclick = () => solicitarEdicionProducto(producto.id);
        contenedorBotones.appendChild(btnEditar);

        // Botón Eliminar (TASK 3)
        const btnEliminar = document.createElement('button');
        btnEliminar.textContent = 'Eliminar';
        btnEliminar.style.backgroundColor = '#dc3545';
        btnEliminar.style.color = 'white';
        // Implementación de remoción del DOM y lógica asociada al hacer clic
        btnEliminar.onclick = () => eliminarProducto(producto.id);
        contenedorBotones.appendChild(btnEliminar);

        li.appendChild(contenedorBotones);
        
        
        listaProductos.appendChild(li);
    });
};

// Guardar el estado actual del arreglo en Local Storage
const guardarEnLocalStorage = () => {
    localStorage.setItem('productos', JSON.stringify(productos));
    console.log('Local Storage actualizado de manera exitosa.');
};


//  GET: Obtener lista de elementos del servidor
const obtenerProductosAPI = async () => {
    try {
        const respuesta = await fetch(API_URL);
        if (!respuesta.ok) throw new Error('Error al conectar con el servidor.');
        
        const datosAPI = await respuesta.json();
        console.log('Respuesta GET Servidor:', datosAPI);
        
        // Sincroniza
        productos = datosAPI;
        guardarEnLocalStorage();
        renderizarProductos();
        mostrarMensaje('Productos sincronizados desde la API con éxito.', 'exito');
    } catch (error) {
        console.error('Error en GET:', error);
        mostrarMensaje('No se pudo conectar con la API. Mostrando datos locales.', 'error');
    }
};


btnSincronizar.addEventListener('click', obtenerProductosAPI);


formularioProducto.addEventListener('submit', async (e) => {
    e.preventDefault(); // Evitar recarga de página 

    const nombre = nombreInput.value;
    const precio = parseFloat(precioInput.value);

    // Validación previa 
    if (!validarDatos(nombre, precio)) return;

    // Crear el objeto del nuevo producto utilizando un ID único basado en tiempo
    const nuevoProducto = {
        id: String(Date.now()),
        nombre: nombre,
        precio: precio
    };

    try {
        const respuesta = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(nuevoProducto)
        });

        if (!respuesta.ok) throw new Error('No se pudo guardar el producto en el servidor.');

        const productoGuardado = await respuesta.json();
        console.log('Respuesta POST Servidor:', productoGuardado);

        // Actualiza el local estorage
        productos.push(productoGuardado);
        guardarEnLocalStorage();
        renderizarProductos();
        
        // Limpia el  formulario 
        formularioProducto.reset();
        mostrarMensaje('¡Producto agregado con éxito a la lista y al servidor!', 'exito');

    } catch (error) {
        console.error('Error en POST:', error);
        // Si la API falla, de todas formas lo guardamos localmente por resiliencia
        productos.push(nuevoProducto);
        guardarEnLocalStorage();
        renderizarProductos();
        formularioProducto.reset();
        mostrarMensaje('Guardado localmente. Error al sincronizar con el servidor.', 'error');
    }
});

// PUT: Actualiza un elemento existente 
const solicitarEdicionProducto = async (id) => {
    const productoAEditar = productos.find(p => p.id === id);
    if (!productoAEditar) return;

    // Solicita nueva información al usuario mediante prompt()
    const nuevoNombre = prompt('Modifica el nombre del producto:', productoAEditar.nombre);
    const nuevoPrecioInput = prompt('Modifica el precio del producto:', productoAEditar.precio);
    const nuevoPrecio = parseFloat(nuevoPrecioInput);

    if (nuevoNombre === null || nuevoPrecioInput === null) return; // Si cancela el prompt
    if (!validarDatos(nuevoNombre, nuevoPrecio)) return;

    const productoActualizado = { ...productoAEditar, nombre: nuevoNombre, precio: nuevoPrecio };

    try {
        const respuesta = await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(productoActualizado)
        });

        if (!respuesta.ok) throw new Error('Error al actualizar en el servidor.');

        const datosEditados = await respuesta.json();
        console.log('Respuesta PUT Servidor:', datosEditados);

        // Modifica mediante indice
        const indice = productos.findIndex(p => p.id === id);
        productos[indice] = datosEditados;

        guardarEnLocalStorage();
        renderizarProductos();
        mostrarMensaje('Producto actualizado correctamente.', 'exito');

    } catch (error) {
        console.error('Error en PUT:', error);
        mostrarMensaje('No se pudo actualizar en el servidor remoto.', 'error');
    }
};

//  DELETE: Elimina un elemento
const eliminarProducto = async (id) => {
    try {
        const respuesta = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });

        if (!respuesta.ok) throw new Error('No se pudo eliminar el producto del servidor.');
        
        console.log(`Respuesta DELETE Servidor: Producto con ID ${id} eliminado.`);

        
        productos = productos.filter(producto => producto.id !== id);

        // Remueve del DOM usando removeChild 
        const nodoAEliminar = document.getElementById(`prod-${id}`);
        if (nodoAEliminar) {
            listaProductos.removeChild(nodoAEliminar);
        }

        // Sincroniza al Local Storage de inmediato
        guardarEnLocalStorage();
        mostrarMensaje('Producto eliminado con éxito.', 'exito');

    } catch (error) {
        console.error('Error en DELETE:', error);
        mostrarMensaje('Error al intentar borrar el producto del servidor.', 'error');
    }
};