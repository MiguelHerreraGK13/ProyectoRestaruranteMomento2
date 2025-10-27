"""
Punto de entrada para la aplicación web
"""
from web.App import App

# Inicializar la aplicación
app = App()

# Punto de entrada
if __name__ == "__main__":
    # Ejecutar la aplicación
    app.run(debug=True)
