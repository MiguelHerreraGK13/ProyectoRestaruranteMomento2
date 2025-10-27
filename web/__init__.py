"""
Inicializador para la creación de la aplicación
"""
from web.App import App

# Crear la instancia de la aplicación
app_instance = App()

# Exponer la aplicación Flask para que pueda ser importada por WSGI
app = app_instance.app
