let boton = document.querySelector(".btnAgregar")
let input = document.querySelector(".inpute")
let ul = document.getElementById("listaNotas")
const mensajeError = document.getElementById("mensajeError");
const btnSync = document.getElementById("btnSync")

//CAmbiar en Riwi//
const api = "https://jsonplaceholder.typicode.com/posts"



// ARRAY DONDE SE GUARDAN LAS NOTAS
let notas = JSON.parse(localStorage.getItem("notas")) || [];


// MOSTRAR LAS NOTAS GUARDADAS
notas.forEach((nota) => {
    crearNota(nota);
});


// BOTON AGREGAR
boton.addEventListener("click", () => {

    if(input.value.trim() === ""){
        mensajeError.textContent = "Completa el campo";
        mensajeError.classList.add("visible");
        return;
    }

    mensajeError.classList.remove("visible");
    const nuevaNota = {
        id: Date.now(),
        texto: textoNota
    };

    crearNotaEnDOM(nuevaNota);
    notas.push(nuevaNota);
    actualizarLocalStorage();
    console.log("✅ Éxito: Nota agregada correctamente.", nuevaNota)
    input.value = "";
});

    function actualizarLocalStorage() {
    // Usa localStorage.setItem() para guardar información.
    localStorage.setItem("notas", JSON.stringify(notas));
  }




// FUNCION PARA CREAR NOTAS
function crearNotaEnDOM(nota){

    let li = document.createElement("li");

    li.textContent = texto;

    ul.appendChild(li);

    const diseño = document.createElement("div");
    diseño.className = "nota-bullet";

    const spanTexto = document.createElement("span");
    spanTexto.className = "nota-texto";
    spanTexto.textContent = nota.texto;

    const btnEliminar = document.createElement("button");
    btnEliminar.className = "btn-eliminar";
    btnEliminar.textContent = "Eliminar";

    li.appendChild(design);
    li.appendChild(spanTexto);
    li.appendChild(btnEliminar);

    // ELIMINAR AL HACER CLICK
    li.addEventListener("click", () => {

        li.remove();



        setTimeout(() => {
            
            ul.removeChild(li);

            // Eliminar del arreglo usando filter
            notas = notas.filter((n) => n.id !== nota.id);
            
            // Actualizar Local Storage tras borrar
            actualizarLocalStorage();
            console.log(`🗑️ Nota eliminada (ID: ${nota.id})`);}, 200);
            
            });
}
    btnSync.addEventListener("click", sincronizarConAPI);

    async function sincronizarConAPI(){    

    console.log("🔄 Iniciando sincronización con la API...");
    try {
    const response = await fetch(api);
    const data = await response.json();
    console.log("📥 GET (Elementos obtenidos de la API):", data );

    if (data.length > 0) {
        const ultima = notas[notas.length - 1];

        const post = await fetch(api, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                userId: 1,
                title: ultima.texto,
                
            }),
        });

        const datapost = await post.json();
        console.log("📤 POST (Elemento enviado a la API):", datapost);

        const put = await fetch(api, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                id: 1,
                userId: 1,
                title: ultima.texto,
                
            }),
        });
        const dataput = await put.json();
        console.log("📤 PUT (Elemento actualizado en la API):", dataput);

        const deleate = await fetch(api, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                id: 1,
                userId: 1,
                title: ultima.texto,
                
            }),
        });
        const resDelete = await fetch(`${API_URL}/1`, {
                method: 'DELETE',
            });
            console.log("❌ DELETE (Status code de eliminación):", resDelete.status);
            
            alert("Sincronización exitosa. Por favor, abre la consola para ver los resultados.");
        } else {
            console.warn("⚠️ No hay notas locales para enviar mediante POST, PUT y DELETE.");
            alert("Agrega al menos una nota antes de sincronizar para probar todas las rutas (POST, PUT, DELETE).");
        }

        } catch (error) {
        // Muestra en consola o DOM los resultados de cada solicitud o errores.
        console.error("🚨 Error al intentar sincronizar con la API:", error);
        alert("Ocurrió un error en la sincronización de la API.");
        }



   }
