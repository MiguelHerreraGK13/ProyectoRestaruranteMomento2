"""
Punto de entrada principal para el sistema de restaurante

"""
from web.Menu_App import app

# Punto de entrada principal
if __name__ == "__main__":
    # Ejecutar la aplicación
    app.run(debug=True)
