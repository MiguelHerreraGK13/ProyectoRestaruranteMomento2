"""
Aplicación web para el sistema de restaurante
"""
import secrets
from flask import Flask, render_template, request, redirect, url_for, flash
from domain.service.Categoria_Service import Categoria_Service
from domain.service.Producto_Service import Producto_Service

class App:
    """Clase principal de la aplicación web"""
    
    def __init__(self):
        """Inicializa la aplicación Flask"""
        self.app = Flask(__name__)
        self.app.secret_key = secrets.token_hex(16)
        self.app.config['SESSION_TYPE'] = 'filesystem'
        self._configurar_rutas()
    
    def _configurar_rutas(self):
        """Configura las rutas de la aplicación"""
        # Página principal
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/menu', 'menu', self.menu)
        
        # Rutas para categorías
        self.app.add_url_rule('/categorias', 'listar_categorias', self.listar_categorias)
        self.app.add_url_rule('/categorias/nueva', 'nueva_categoria', self.nueva_categoria, methods=['GET', 'POST'])
        self.app.add_url_rule('/categorias/editar/<int:id>', 'editar_categoria', self.editar_categoria, methods=['GET', 'POST'])
        self.app.add_url_rule('/categorias/eliminar/<int:id>', 'eliminar_categoria', self.eliminar_categoria, methods=['POST'])
        
        # Rutas para productos
        self.app.add_url_rule('/productos', 'listar_productos', self.listar_productos)
        self.app.add_url_rule('/productos/categoria/<int:categoria_id>', 'productos_por_categoria', self.productos_por_categoria)
        self.app.add_url_rule('/productos/nuevo', 'nuevo_producto', self.nuevo_producto, methods=['GET', 'POST'])
        self.app.add_url_rule('/productos/editar/<int:id>', 'editar_producto', self.editar_producto, methods=['GET', 'POST'])
        self.app.add_url_rule('/productos/eliminar/<int:id>', 'eliminar_producto', self.eliminar_producto, methods=['POST'])
    
    def run(self, debug=True):
        """Ejecuta la aplicación Flask"""
        self.app.run(debug=debug)
    
    # Controladores de rutas
    
    def index(self):
        """Página principal"""
        categorias = Categoria_Service.listar_categorias()
        productos = Producto_Service.listar_productos()
        return render_template('index.html', categorias=categorias, productos=productos)
    
    def menu(self):
        """Ver menú completo"""
        categorias = Categoria_Service.listar_categorias()
        menu_por_categoria = {}
        
        for categoria in categorias:
            productos = Producto_Service.listar_productos_por_categoria(categoria.id)
            menu_por_categoria[categoria] = productos
        
        return render_template('menu.html', menu_por_categoria=menu_por_categoria)
    
    def listar_categorias(self):
        """Lista todas las categorías"""
        categorias = Categoria_Service.listar_categorias()
        return render_template('categorias/listar.html', categorias=categorias)
    
    def nueva_categoria(self):
        """Formulario para crear una nueva categoría"""
        if request.method == 'POST':
            nombre = request.form.get('nombre', '')
            descripcion = request.form.get('descripcion', '')
            
            if not nombre:
                flash('El nombre de la categoría es obligatorio', 'danger')
                return render_template('categorias/form.html')
            
            id_categoria = Categoria_Service.crear_categoria(nombre, descripcion)
            
            if id_categoria > 0:
                flash('Categoría creada con éxito', 'success')
                return redirect(url_for('listar_categorias'))
            else:
                flash('Error al crear la categoría', 'danger')
                return render_template('categorias/form.html')
        
        return render_template('categorias/form.html')
    
    def editar_categoria(self, id):
        """Formulario para editar una categoría existente"""
        categoria = Categoria_Service.obtener_categoria(id)
        
        if not categoria:
            flash('Categoría no encontrada', 'danger')
            return redirect(url_for('listar_categorias'))
        
        if request.method == 'POST':
            nombre = request.form.get('nombre', '')
            descripcion = request.form.get('descripcion', '')
            
            if not nombre:
                flash('El nombre de la categoría es obligatorio', 'danger')
                return render_template('categorias/form.html', categoria=categoria)
            
            if Categoria_Service.actualizar_categoria(id, nombre, descripcion):
                flash('Categoría actualizada con éxito', 'success')
                return redirect(url_for('listar_categorias'))
            else:
                flash('Error al actualizar la categoría', 'danger')
                return render_template('categorias/form.html', categoria=categoria)
        
        return render_template('categorias/form.html', categoria=categoria)
    
    def eliminar_categoria(self, id):
        """Elimina una categoría"""
        if Categoria_Service.eliminar_categoria(id):
            flash('Categoría eliminada con éxito', 'success')
        else:
            flash('No se puede eliminar la categoría porque tiene productos asociados', 'danger')
        
        return redirect(url_for('listar_categorias'))
    
    def listar_productos(self):
        """Lista todos los productos"""
        productos = Producto_Service.listar_productos()
        return render_template('productos/listar.html', productos=productos)
    
    def productos_por_categoria(self, categoria_id):
        """Lista productos por categoría"""
        categoria = Categoria_Service.obtener_categoria(categoria_id)
        if not categoria:
            flash('Categoría no encontrada', 'danger')
            return redirect(url_for('listar_categorias'))
        
        productos = Producto_Service.listar_productos_por_categoria(categoria_id)
        return render_template('productos/por_categoria.html', productos=productos, categoria=categoria)
    
    def nuevo_producto(self):
        """Formulario para crear un nuevo producto"""
        categorias = Categoria_Service.listar_categorias()
        
        if not categorias:
            flash('Debe crear al menos una categoría primero', 'warning')
            return redirect(url_for('nueva_categoria'))
        
        if request.method == 'POST':
            nombre = request.form.get('nombre', '')
            descripcion = request.form.get('descripcion', '')
            precio_str = request.form.get('precio', '')
            categoria_id_str = request.form.get('categoria_id', '')
            
            if not nombre or not precio_str or not categoria_id_str:
                flash('Todos los campos obligatorios deben estar completos', 'danger')
                return render_template('productos/form.html', categorias=categorias)
            
            try:
                precio = float(precio_str)
                categoria_id = int(categoria_id_str)
            except ValueError:
                flash('El precio debe ser un número válido', 'danger')
                return render_template('productos/form.html', categorias=categorias)
            
            if precio <= 0:
                flash('El precio debe ser mayor que cero', 'danger')
                return render_template('productos/form.html', categorias=categorias)
            
            id_producto = Producto_Service.crear_producto(nombre, descripcion, precio, categoria_id)
            
            if id_producto > 0:
                flash('Producto creado con éxito', 'success')
                return redirect(url_for('listar_productos'))
            else:
                flash('Error al crear el producto', 'danger')
                return render_template('productos/form.html', categorias=categorias)
        
        return render_template('productos/form.html', categorias=categorias)
    
    def editar_producto(self, id):
        """Formulario para editar un producto existente"""
        producto = Producto_Service.obtener_producto(id)
        categorias = Categoria_Service.listar_categorias()
        
        if not producto:
            flash('Producto no encontrado', 'danger')
            return redirect(url_for('listar_productos'))
        
        if request.method == 'POST':
            nombre = request.form.get('nombre', '')
            descripcion = request.form.get('descripcion', '')
            precio_str = request.form.get('precio', '')
            categoria_id_str = request.form.get('categoria_id', '')
            
            if not nombre or not precio_str or not categoria_id_str:
                flash('Todos los campos obligatorios deben estar completos', 'danger')
                return render_template('productos/form.html', producto=producto, categorias=categorias)
            
            try:
                precio = float(precio_str)
                categoria_id = int(categoria_id_str)
            except ValueError:
                flash('El precio debe ser un número válido', 'danger')
                return render_template('productos/form.html', producto=producto, categorias=categorias)
            
            if precio <= 0:
                flash('El precio debe ser mayor que cero', 'danger')
                return render_template('productos/form.html', producto=producto, categorias=categorias)
            
            if Producto_Service.actualizar_producto(id, nombre, descripcion, precio, categoria_id):
                flash('Producto actualizado con éxito', 'success')
                return redirect(url_for('listar_productos'))
            else:
                flash('Error al actualizar el producto', 'danger')
                return render_template('productos/form.html', producto=producto, categorias=categorias)
        
        return render_template('productos/form.html', producto=producto, categorias=categorias)
    
    def eliminar_producto(self, id):
        """Elimina un producto"""
        if Producto_Service.eliminar_producto(id):
            flash('Producto eliminado con éxito', 'success')
        else:
            flash('Error al eliminar el producto', 'danger')
        
        return redirect(url_for('listar_productos'))
