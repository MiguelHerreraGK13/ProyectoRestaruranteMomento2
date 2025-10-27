"""
Script de inicialización para el sistema
"""
import os
from persistence.Conexion import Conexion
from domain.model.Categoria import Categoria
from domain.model.Producto import Producto

# Nombres de archivos
CATEGORIAS_FILE = "categorias.json"
PRODUCTOS_FILE = "productos.json"

def inicializar_datos():
    """
    Crea los archivos JSON con datos iniciales si no existen
    """
    data_dir = Conexion.get_data_dir()
    categorias_path = os.path.join(data_dir, CATEGORIAS_FILE)
    productos_path = os.path.join(data_dir, PRODUCTOS_FILE)
    
    # Categorías por defecto
    if not os.path.exists(categorias_path):
        categorias = [
            Categoria(1, "Entradas", "Aperitivos y pequeños platos para comenzar"),
            Categoria(2, "Platos principales", "Platos fuertes y especialidades"),
            Categoria(3, "Postres", "Dulces y postres variados"),
            Categoria(4, "Bebidas", "Refrescos, jugos y bebidas")
        ]
        Conexion.save_json(CATEGORIAS_FILE, [cat.to_dict() for cat in categorias])
        print("Archivo de categorías creado con datos iniciales.")
    
    # Productos por defecto
    if not os.path.exists(productos_path):
        productos = [
            Producto(1, "Ensalada César", "Lechuga romana, crutones, parmesano y aderezo César", 34000, 1, "Entradas"),
            Producto(2, "Palitos de mozzarella", "Queso mozzarella empanizado con salsa marinara", 32000, 1, "Entradas"),
            Producto(3, "Hamburguesa clásica", "Carne de res, lechuga, tomate, cebolla y queso", 52000, 2, "Platos principales"),
            Producto(4, "Pizza Margherita", "Salsa de tomate, mozzarella y albahaca", 68000, 2, "Platos principales"),
            Producto(5, "Helado de vainilla", "Clásico helado de vainilla con toppings", 20000, 3, "Postres"),
            Producto(6, "Refresco", "Refresco de cola, lima-limón o naranja", 10000, 4, "Bebidas")
        ]
        Conexion.save_json(PRODUCTOS_FILE, [prod.to_dict() for prod in productos])
        print("Archivo de productos creado con datos iniciales.")

# Ejecutar inicialización
if __name__ == "__main__":
    inicializar_datos()
    print("Inicialización de datos completada.")
