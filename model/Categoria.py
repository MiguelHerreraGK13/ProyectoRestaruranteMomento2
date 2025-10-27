"""
Modelo para las categorías del menú
"""

class Categoria:
    """Modelo para las categorías del menú"""
    
    def __init__(self, id=None, nombre="", descripcion=""):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
    
    
    @classmethod
    def from_dict(cls, data):
        """Crea una instancia desde un diccionario"""
        return cls(
            id=data.get('id'),
            nombre=data.get('nombre', ''),
            descripcion=data.get('descripcion', '')
        )
    
    def to_dict(self):
        """Convierte la instancia a un diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }
    
    def __str__(self):
        return f"Categoria(id={self.id}, nombre={self.nombre})"
