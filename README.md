# Sistema de Restaurante - Versión Refactorizada

Este es un sistema para la administración de un restaurante que permite gestionar categorías y productos del menú. Está organizado siguiendo el patrón de arquitectura en capas con una estructura más avanzada que mejora la mantenibilidad del código.

## Características

- **Arquitectura en capas bien definida**:
  - Dominio: Modelos y servicios
  - Persistencia: Acceso a datos
  - Web: Interfaz de usuario
- Gestión de categorías de menú (crear, ver, modificar, eliminar)
- Gestión de productos (crear, ver, modificar, eliminar)
- Visualización del menú completo
- Persistencia de datos en archivos JSON
- Interfaz web usando Flask y Bootstrap

## Estructura del Proyecto

```
sistema_restaurante_refactorizado/
│
├── domain/                  # Capa de dominio
│   ├── model/               # Modelos de dominio
│   │   ├── Categoria.py     # Clase Categoria
│   │   └── Producto.py      # Clase Producto
│   │
│   └── service/             # Servicios de negocio
│       ├── Categoria_Service.py   # Servicio para gestión de categorías
│       └── Producto_Service.py    # Servicio para gestión de productos
│
├── persistence/             # Capa de persistencia
│   ├── Conexion.py          # Gestión de conexión a datos
│   ├── Categoria_Repositorio.py  # Repositorio de categorías
│   └── Producto_Repositorio.py   # Repositorio de productos
│
├── web/                     # Capa de presentación
│   ├── App.py               # Clase principal de la aplicación web
│   ├── Menu_App.py          # Punto de entrada para la aplicación web
│   └── templates/           # Plantillas HTML
│       ├── base.html        # Plantilla base
│       ├── index.html       # Página principal
│       ├── menu.html        # Visualización del menú
│       ├── categorias/      # Plantillas para categorías
│       └── productos/       # Plantillas para productos
│
├── data/                    # Directorio de datos
│   ├── categorias.json      # Datos de categorías
│   └── productos.json       # Datos de productos
│
├── Init_Data.py             # Script para inicializar datos
└── Main.py                  # Punto de entrada principal
```

## Requisitos

- Python 3.6 o superior
- Flask 2.0.0 o superior

## Instalación

1. Clona o descarga este repositorio
2. Instala las dependencias:

```bash
pip install flask
```

## Ejecución

1. Inicializa los datos (opcional si es la primera vez):

```bash
python Init_Data.py
```

2. Ejecuta la aplicación:

```bash
python Main.py
```

3. Accede a la aplicación en tu navegador: `http://localhost:5000`

## Características del código

- **Patrón Repositorio**: Separa la lógica de acceso a datos
- **Servicios**: Encapsula la lógica de negocio
- **Modelos de dominio**: Define entidades claras
- **Controladores web**: Gestiona la interacción con el usuario
- **Plantillas HTML**: Separación clara de la vista

## Uso de la Aplicación

### Gestión de Categorías
- Lista todas las categorías disponibles
- Crea nuevas categorías con nombre y descripción
- Edita categorías existentes
- Elimina categorías (si no tienen productos asociados)

### Gestión de Productos
- Lista todos los productos disponibles
- Visualiza productos por categoría
- Crea nuevos productos con nombre, descripción, precio y categoría
- Edita productos existentes
- Elimina productos

### Visualización del Menú
- Muestra una vista organizada del menú por categorías
- Muestra detalles de cada producto, incluyendo precio

## Notas adicionales

Esta es una versión refactorizada que sigue un diseño orientado a objetos más estricto y una estructura de proyecto más profesional. La aplicación implementa los principios de Responsabilidad Única y Separación de Preocupaciones para mejorar la mantenibilidad y extensibilidad.

---

© 2025 Sistema de Restaurante
