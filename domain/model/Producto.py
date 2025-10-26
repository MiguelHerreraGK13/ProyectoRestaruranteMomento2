"""
Modelo para los productos del menú
"""

class Producto:
    """Modelo para los productos del menú"""
    
    def __init__(self, id=None, nombre="", descripcion="", precio=0.0, categoria_id=None, nombre_categoria=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria_id = categoria_id
        self.nombre_categoria = nombre_categoria
    
    @classmethod
    def from_dict(cls, data):
        """Crea una instancia desde un diccionario"""
        return cls(
            id=data.get('id'),
            nombre=data.get('nombre', ''),
            descripcion=data.get('descripcion', ''),
            precio=data.get('precio', 0.0),
            categoria_id=data.get('categoria_id'),
            nombre_categoria=data.get('nombre_categoria')
        )
    
    def to_dict(self):
        """Convierte la instancia a un diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'categoria_id': self.categoria_id,
            'nombre_categoria': self.nombre_categoria
        }
    
    def __str__(self):
        return f"Producto(id={self.id}, nombre={self.nombre}, precio={self.precio})"
