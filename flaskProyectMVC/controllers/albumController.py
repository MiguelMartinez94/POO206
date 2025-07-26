from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.albumModel import *

albumsBP = Blueprint('albums', __name__)

#ruta de inicio

@albumsBP.route('/')
def home():
    try:
        
        consultaTodo = getAll()        
        return render_template('formulario.html', errores={}, albums = consultaTodo)
        
    except Exception as e:
        print('Error al consultar todo: ' + e)
        return render_template('formulario.html', errores={}, albums = [])
    
    
    
#Ruta de detalles
#Ruta para cargar datos de detalle        
@albumsBP.route('/detalle/<int:id>')
def detalle(id):
    try:
        consultaId = getById(id)
        return render_template('consulta.html', album = consultaId)
        
    except Exception as e:
        print('Error al consultar todo: ' + e)
        return render_template('consulta.html', errores={}, albums = {})
    
    

#Ruta para guardar los albums
@albumsBP.route('/guardarAlbum', methods = ['POST'])
def guardar():
    
    #lista de errores
    errores = {}
    
    #Obtener los datos a insertar
    titulo = request.form.get('txtTitulo', '').strip()
    artista = request.form.get('txtArtista', '').strip()
    anio = request.form.get('txtAnio', '').strip()
    
    if not titulo:
        errores['txtTitulo'] = 'Nombre del álbum obligatorio'
        
    if not artista:
        errores['txtArtista'] = 'Nombre del artista obligatorio'
        
    if not anio:
        errores['txtAnio'] = 'Año del álbum obligatorio'
        
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2050:
        errores['txtAnio'] = 'Ingresa un año válido'
        
    if not errores:
    #Intentamos ejecutar el INSERT
    
        try:
            
            insertAlbum(titulo, artista, anio)
            flash('Album se guardó en BD')
            return redirect(url_for('home'))
            
        except Exception as e:
            mysql.connection.rollback()
            flash( f'Algo falló: {str(e)}')
            return redirect(url_for('albums.home'))
            
        
    
    return render_template('formulario.html', errores = errores)        
        

#Ruta para cargar datos a actualizar        
@albumsBP.route('/actualizar/<int:id>')
def consulta_actualizar(id):
    try:
        consultaId = getById(id)
        return render_template('update.html', album = consultaId)
        
    except Exception as e:
        print('Error al consultar todo: ' + e)
        return render_template('update.html', errores={}, albums = {})
        

#Ruta para actualizar los datos cargados
@albumsBP.route('/modificarAlbum', methods= ['POST'])
def guardar_actualizaciones():
        
    #lista de errores
    errores = {}
    
    #Obtener los datos a modificar
    idUpdate = request.form.get('id', '').strip()
    nTitulo = request.form.get('ntxtTitulo', '').strip()
    nArtista = request.form.get('ntxtArtista', '').strip()
    nAnio = request.form.get('ntxtAnio', '').strip()
    
    if not nTitulo:
        errores['ntxtTitulo'] = 'Nombre del álbum obligatorio'
        
    if not nArtista:
        errores['ntxtArtista'] = 'Nombre del artista obligatorio'
        
    if not nAnio:
        errores['ntxtAnio'] = 'Año del álbum obligatorio'
        
    elif not nAnio.isdigit() or int(nAnio) < 1800 or int(nAnio) > 2050:
        errores['ntxtAnio'] = 'Ingresa un año válido'
        
    if not errores:
    
    #Intentamos ejecutar el UPDATE
    
        try:
            updateAlbum(idUpdate, nTitulo, nArtista, nAnio)
            flash('Album se actualizó correctamente')
            return redirect(url_for('albums.home'))
            
        except Exception as e:
            mysql.connection.rollback()
            flash( f'Algo falló: {str(e)}')
            return redirect(url_for('albums.home'))
            
        
        
    return render_template('update.html',album=(idUpdate, nTitulo, nArtista, nAnio), errores = errores, )

#Cargar datos para eliminar

@albumsBP.route('/eliminacion/<int:id>')
def eliminar(id):
    
    flash('¿Deseas Eliminar este album?')
    
    try:
        consultaId = getById(id)
        return render_template('confirmDel.html', album = consultaId)
        
    except Exception as e:
        print('Error al consultar todo: ' + e)
        return render_template('confirmDel.html', albums = {})
        


#Confirmación de la eliminación
@albumsBP.route('/confirmar_eliminacion/<int:id>', methods=['POST'])
def confirmarEliminacion(id):
    
    try:
        
        softDeleteAlbum(id)
        flash('Álbum eliminado correctamente')
        return redirect(url_for('albums.home'))
        
    except Exception as e:
        mysql.connection.rollback()
        flash(f'Error al eliminar: {str(e)}')
    
