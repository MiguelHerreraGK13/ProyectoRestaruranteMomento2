"""
Servicio para la gestión de productos
"""
from persistence.Producto_Repositorio import Producto_Repositorio
from domain.service.Categoria_Service import Categoria_Service

class Producto_Service:
    """Servicio para la gestión de productos"""
    
    @staticmethod
    def listar_productos():
        """
        Lista todos los productos disponibles
        
        Returns:
            list: Lista de objetos Producto
        """
        return Producto_Repositorio.listar_productos()
    
    @staticmethod
    def obtener_producto(id):
        """
        Obtiene un producto por su ID
        
        Args:
            id: ID del producto
            
        Returns:
            Producto: Objeto Producto o None si no existe
        """
        return Producto_Repositorio.buscar_por_id(id)
    
    @staticmethod
    def listar_productos_por_categoria(categoria_id):
        """
        Lista los productos de una categoría específica
        
        Args:
            categoria_id: ID de la categoría
            
        Returns:
            list: Lista de objetos Producto de esa categoría
        """
        return Producto_Repositorio.listar_por_categoria(categoria_id)
    
    @staticmethod
    def crear_producto(nombre, descripcion, precio, categoria_id):
        """
        Crea un nuevo producto
        
        Args:
            nombre: Nombre del producto
            descripcion: Descripción del producto
            precio: Precio del producto
            categoria_id: ID de la categoría
            
        Returns:
            int: ID del producto creado, o -1 si falló
        """
        if not nombre or precio <= 0:
            return -1
        
        # Verificar que la categoría existe
        categoria = Categoria_Service.obtener_categoria(categoria_id)
        if not categoria:
            return -1
        
        return Producto_Repositorio.crear(
            nombre, 
            descripcion, 
            precio, 
            categoria_id,
            categoria.nombre
        )
    
    @staticmethod
    def actualizar_producto(id, nombre, descripcion, precio, categoria_id):
        """
        Actualiza un producto existente
        
        Args:
            id: ID del producto
            nombre: Nuevo nombre
            descripcion: Nueva descripción
            precio: Nuevo precio
            categoria_id: ID de la categoría
            
        Returns:
            bool: True si se actualizó correctamente
        """
        if not nombre or precio <= 0:
            return False
        
        # Verificar que la categoría existe
        categoria = Categoria_Service.obtener_categoria(categoria_id)
        if not categoria:
            return False
        
        return Producto_Repositorio.actualizar(
            id,
            nombre, 
            descripcion, 
            precio, 
            categoria_id,
            categoria.nombre
        )
    
    @staticmethod
    def eliminar_producto(id):
        """
        Elimina un producto
        
        Args:
            id: ID del producto
            
        Returns:
            bool: True si se eliminó correctamente
        """
        return Producto_Repositorio.eliminar(id)
