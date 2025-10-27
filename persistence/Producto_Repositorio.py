"""
Repositorio para la persistencia de productos en JSON
"""
from persistence.Conexion import Conexion
from domain.model.Producto import Producto

class Producto_Repositorio:
    """Repositorio para acceder a datos de productos en archivos JSON"""
    
    # Nombre del archivo JSON
    PRODUCTOS_FILE = "productos.json"
    
    @staticmethod
    def listar_productos():
        """
        Carga los productos desde el archivo JSON
        
        Returns:
            list: Lista de objetos Producto
        """
        data = Conexion.load_json(Producto_Repositorio.PRODUCTOS_FILE)
        return [Producto.from_dict(prod_data) for prod_data in data]
    
    @staticmethod
    def guardar_productos(productos):
        """
        Guarda los productos en el archivo JSON
        
        Args:
            productos (list): Lista de objetos Producto
            
        Returns:
            bool: True si se guardó correctamente
        """
        data = [prod.to_dict() for prod in productos]
        return Conexion.save_json(Producto_Repositorio.PRODUCTOS_FILE, data)
    
    @staticmethod
    def obtener_siguiente_id():
        """
        Obtiene el siguiente ID disponible para productos
        
        Returns:
            int: Siguiente ID
        """
        productos = Producto_Repositorio.listar_productos()
        if not productos:
            return 1
        return max(prod.id for prod in productos) + 1
    
    @staticmethod
    def buscar_por_id(id):
        """
        Busca un producto por su ID
        
        Args:
            id: ID del producto
            
        Returns:
            Producto: Objeto Producto o None
        """
        productos = Producto_Repositorio.listar_productos()
        for producto in productos:
            if producto.id == id:
                return producto
        return None
    
    @staticmethod
    def crear(nombre, descripcion, precio, categoria_id, nombre_categoria):
        """
        Crea un nuevo producto
        
        Args:
            nombre: Nombre del producto
            descripcion: Descripción del producto
            precio: Precio del producto
            categoria_id: ID de la categoría
            nombre_categoria: Nombre de la categoría
            
        Returns:
            int: ID del producto creado
        """
        productos = Producto_Repositorio.listar_productos()
        
        # Generar nuevo ID
        nuevo_id = Producto_Repositorio.obtener_siguiente_id()
        
        # Crear nuevo producto
        nuevo_producto = Producto(
            nuevo_id, 
            nombre, 
            descripcion, 
            precio, 
            categoria_id, 
            nombre_categoria
        )
        productos.append(nuevo_producto)
        
        # Guardar cambios
        Producto_Repositorio.guardar_productos(productos)
        
        return nuevo_id
    
    @staticmethod
    def actualizar(id, nombre, descripcion, precio, categoria_id, nombre_categoria):
        """
        Actualiza un producto
        
        Args:
            id: ID del producto
            nombre: Nuevo nombre
            descripcion: Nueva descripción
            precio: Nuevo precio
            categoria_id: ID de la categoría
            nombre_categoria: Nombre de la categoría
            
        Returns:
            bool: True si se actualizó correctamente
        """
        productos = Producto_Repositorio.listar_productos()
        
        for i, producto in enumerate(productos):
            if producto.id == id:
                productos[i].nombre = nombre
                productos[i].descripcion = descripcion
                productos[i].precio = precio
                productos[i].categoria_id = categoria_id
                productos[i].nombre_categoria = nombre_categoria
                return Producto_Repositorio.guardar_productos(productos)
        
        return False
    
    @staticmethod
    def eliminar(id):
        """
        Elimina un producto
        
        Args:
            id: ID del producto
            
        Returns:
            bool: True si se eliminó correctamente
        """
        productos = Producto_Repositorio.listar_productos()
        productos_filtrados = [p for p in productos if p.id != id]
        
        if len(productos_filtrados) < len(productos):
            return Producto_Repositorio.guardar_productos(productos_filtrados)
        
        return False
    
    @staticmethod
    def listar_por_categoria(categoria_id):
        """
        Lista productos de una categoría específica
        
        Args:
            categoria_id: ID de la categoría
            
        Returns:
            list: Lista de productos de esa categoría
        """
        productos = Producto_Repositorio.listar_productos()
        return [p for p in productos if p.categoria_id == categoria_id]
    
    @staticmethod
    def actualizar_nombre_categoria(categoria_id, nuevo_nombre):
        """
        Actualiza el nombre de la categoría en todos los productos que pertenecen a ella
        
        Args:
            categoria_id: ID de la categoría
            nuevo_nombre: Nuevo nombre de la categoría
            
        Returns:
            bool: True si se actualizó correctamente
        """
        productos = Producto_Repositorio.listar_productos()
        modificado = False
        
        for producto in productos:
            if producto.categoria_id == categoria_id:
                producto.nombre_categoria = nuevo_nombre
                modificado = True
        
        if modificado:
            return Producto_Repositorio.guardar_productos(productos)
        
        return True  # No había productos que actualizar
