# Portafolio Personal

Proyecto web personal desarrollado con **HTML**, **CSS** y **JavaScript**. Incluye una página de presentación (portafolio) y una página secundaria dedicada a mis mascotas .

---

## Estructura del Proyecto

```
/
├── index.html           # Página principal del portafolio
├── mascotas.html        # Página de mascotas
├── styles.css           # Estilos globales (con variables CSS y responsive)
├── script.js            # Lógica e interactividad en JavaScript
├── settings.json        # Configuración de Live Server (VS Code)
└── imagenes/
    ├── 55da3dc31084cb6308df607b686613fdf23dd459.jpeg  # Foto de perfil
    ├── Rottweiler-Temperament.jpg                      # Black (perro)
    ├── tortuga-rusa.jpg                                # Jose (tortuga)
    ├── default.jpg                                     # Samuel (loro)
    └── Guacamano-azul-de-pecho-amarilo-Zoo-Madrid-3 (1).jpg  # Gabriel (guacamayo)
```

---

## Páginas

### `index.html` — Portafolio
Página principal con tres secciones:
- **Sobre Mí** — Presentación personal.
- **Proyectos** — Menú con enlaces a proyectos.
- **Contacto** — Formulario con campos de nombre y email.

### `mascotas.html` — Mis Mascotas
Galería en grid con 6 mascotas 

| Nombre | Tipo |
|---|---|
| Black | Rottweiler |
| Jose | Tortuga rusa (60+ años) |
| Samuel | Loro |
| Gabriel | Guacamayo azul |
| Chiquilina | Gata |
| Julian | Mapache |

---

##Funcionalidades JavaScript (`script.js`)

1. **Mensaje de bienvenida** — Aparece al cargar la página y desaparece automáticamente tras 4 segundos con animación.
2. **Texto rotativo** — Botón "Saber más sobre mí" que alterna entre 3 textos distintos con transición.
3. **Toggle de proyectos** — Botón para mostrar u ocultar la lista de proyectos.

---

## Estilos CSS (`styles.css`)

- Variables CSS en `:root` para colores, tipografía, espaciados y sombras.
- Animaciones: `bajarFoto`, `rebote`.
- Diseño **responsive** con 3 breakpoints:
  - Móvil: `max-width: 599px`
  - Tablet: `600px – 1023px`
  - Escritorio: `min-width: 1024px`

---

## Cómo ejecutar

1. Clona o descarga el repositorio.
2. Abre el proyecto en **VS Code**.
3. Instala la extensión **Live Server**.
4. Haz clic derecho en `index.html` → **Open with Live Server**.
5. El servidor correrá en el puerto `5501` (según `settings.json`).

> También puedes abrir `index.html` directamente en el navegador, aunque algunas rutas de imágenes locales podrían requerir un servidor.

---

## Tecnologías

- HTML5
- CSS3 (Grid, Flexbox, Variables, Animaciones)
- JavaScript (Vanilla)
- VS Code + Live Server


