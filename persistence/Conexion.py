"""
Clase de conexión para la persistencia en archivos JSON
"""
import os
import json

class Conexion:
    """Maneja la conexión a los archivos JSON"""
    
    @staticmethod
    def get_data_dir():
        """Obtiene la ruta del directorio de datos"""
        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
        os.makedirs(data_dir, exist_ok=True)
        return data_dir
    
    @staticmethod
    def get_file_path(file_name):
        """Obtiene la ruta completa de un archivo en el directorio de datos"""
        return os.path.join(Conexion.get_data_dir(), file_name)
    
    @staticmethod
    def load_json(file_name):
        """Carga datos desde un archivo JSON"""
        file_path = Conexion.get_file_path(file_name)
        
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    return json.load(file)
            return []
        except Exception as e:
            print(f"Error al cargar datos desde {file_name}: {e}")
            return []
    
    @staticmethod
    def save_json(file_name, data):
        """Guarda datos en un archivo JSON"""
        file_path = Conexion.get_file_path(file_name)
        
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar datos en {file_name}: {e}")
            return False
