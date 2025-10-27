"""
Servicio para la gestión de categorías
"""
from persistence.Categoria_Repositorio import Categoria_Repositorio
from persistence.Producto_Repositorio import Producto_Repositorio

class Categoria_Service:
    """Servicio para la gestión de categorías"""
    
    @staticmethod
    def listar_categorias():
        """
        Lista todas las categorías disponibles
        
        Returns:
            list: Lista de objetos Categoria
        """
        return Categoria_Repositorio.listar_categorias()
    
    @staticmethod
    def obtener_categoria(id):
        """
        Obtiene una categoría por su ID
        
        Args:
            id: ID de la categoría
            
        Returns:
            Categoria: Objeto Categoria o None si no existe
        """
        return Categoria_Repositorio.buscar_por_id(id)
    
    @staticmethod
    def crear_categoria(nombre, descripcion):
        """
        Crea una nueva categoría
        
        Args:
            nombre: Nombre de la categoría
            descripcion: Descripción de la categoría
            
        Returns:
            int: ID de la categoría creada, o -1 si falló
        """
        if not nombre:
            return -1
        
        return Categoria_Repositorio.crear(nombre, descripcion)
    
    @staticmethod
    def actualizar_categoria(id, nombre, descripcion):
        """
        Actualiza una categoría existente
        
        Args:
            id: ID de la categoría
            nombre: Nuevo nombre
            descripcion: Nueva descripción
            
        Returns:
            bool: True si se actualizó correctamente
        """
        if not nombre:
            return False
        
        resultado = Categoria_Repositorio.actualizar(id, nombre, descripcion)
        
        if resultado:
            # Actualizar nombre de categoría en productos
            Producto_Repositorio.actualizar_nombre_categoria(id, nombre)
            return True
        
        return False
    
    @staticmethod
    def eliminar_categoria(id):
        """
        Elimina una categoría
        
        Args:
            id: ID de la categoría
            
        Returns:
            bool: True si se eliminó correctamente
        """
        # Verificar que no tenga productos asociados
        productos_categoria = Producto_Repositorio.listar_por_categoria(id)
        if productos_categoria:
            return False  # No se puede eliminar si tiene productos
        
        return Categoria_Repositorio.eliminar(id)
