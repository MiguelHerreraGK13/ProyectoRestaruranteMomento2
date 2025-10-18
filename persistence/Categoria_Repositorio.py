"""
Repositorio para la persistencia de categorías en JSON
"""
from persistence.Conexion import Conexion
from domain.model.Categoria import Categoria

class Categoria_Repositorio:
    """Repositorio para acceder a datos de categorías en archivos JSON"""
    
    # Nombre del archivo JSON
    CATEGORIAS_FILE = "categorias.json"
    
    @staticmethod
    def listar_categorias():
        """
        Carga las categorías desde el archivo JSON
        
        Returns:
            list: Lista de objetos Categoria
        """
        data = Conexion.load_json(Categoria_Repositorio.CATEGORIAS_FILE)
        return [Categoria.from_dict(cat_data) for cat_data in data]
    
    @staticmethod
    def guardar_categorias(categorias):
        """
        Guarda las categorías en el archivo JSON
        
        Args:
            categorias (list): Lista de objetos Categoria
            
        Returns:
            bool: True si se guardó correctamente
        """
        data = [cat.to_dict() for cat in categorias]
        return Conexion.save_json(Categoria_Repositorio.CATEGORIAS_FILE, data)
    
    @staticmethod
    def obtener_siguiente_id():
        """
        Obtiene el siguiente ID disponible para categorías
        
        Returns:
            int: Siguiente ID
        """
        categorias = Categoria_Repositorio.listar_categorias()
        if not categorias:
            return 1
        return max(cat.id for cat in categorias) + 1
    
    @staticmethod
    def buscar_por_id(id):
        """
        Busca una categoría por su ID
        
        Args:
            id: ID de la categoría
            
        Returns:
            Categoria: Objeto Categoria o None
        """
        categorias = Categoria_Repositorio.listar_categorias()
        for categoria in categorias:
            if categoria.id == id:
                return categoria
        return None
    
    @staticmethod
    def crear(nombre, descripcion):
        """
        Crea una nueva categoría
        
        Args:
            nombre: Nombre de la categoría
            descripcion: Descripción de la categoría
            
        Returns:
            int: ID de la categoría creada
        """
        categorias = Categoria_Repositorio.listar_categorias()
        
        # Generar nuevo ID
        nuevo_id = Categoria_Repositorio.obtener_siguiente_id()
        
        # Crear nueva categoría
        nueva_categoria = Categoria(nuevo_id, nombre, descripcion)
        categorias.append(nueva_categoria)
        
        # Guardar cambios
        Categoria_Repositorio.guardar_categorias(categorias)
        
        return nuevo_id
    
    @staticmethod
    def actualizar(id, nombre, descripcion):
        """
        Actualiza una categoría
        
        Args:
            id: ID de la categoría
            nombre: Nuevo nombre
            descripcion: Nueva descripción
            
        Returns:
            bool: True si se actualizó correctamente
        """
        categorias = Categoria_Repositorio.listar_categorias()
        
        for i, categoria in enumerate(categorias):
            if categoria.id == id:
                categorias[i].nombre = nombre
                categorias[i].descripcion = descripcion
                return Categoria_Repositorio.guardar_categorias(categorias)
        
        return False
    
    @staticmethod
    def eliminar(id):
        """
        Elimina una categoría
        
        Args:
            id: ID de la categoría
            
        Returns:
            bool: True si se eliminó correctamente
        """
        categorias = Categoria_Repositorio.listar_categorias()
        categorias_filtradas = [c for c in categorias if c.id != id]
        
        if len(categorias_filtradas) < len(categorias):
            return Categoria_Repositorio.guardar_categorias(categorias_filtradas)
        
        return False
