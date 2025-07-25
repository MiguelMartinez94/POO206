from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL
import MySQLdb

app = Flask (__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Kesadilla94"
app.config['MYSQL_DB'] = "restaurante"
#app.config['MYSQL_PORT'] = 3306
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def home():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from restaurantes where state = 1')
        consultaRestaurantes = cursor.fetchall()
        return render_template('registro_restaurante.html', errores={}, restaurantes = consultaRestaurantes)
        
    except Exception as e:
        print('Error al consultar todo: ' + e)
        return render_template('registro_restaurante.html', errores={}, restaurantes = {})
        
    finally:
        cursor.close()
        
#Ruta para cargar datos de detalle        
@app.route('/detalle_restaurante/<int:id>')
def detalleRestaurante(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from restaurantes where id = %s', (id,))
        consultaNombre = cursor.fetchone()
        return render_template('detalle_restaurante.html', restaurante = consultaNombre)
        
    except Exception as e:
        print('Error al consultar todo: ' + e)
        return render_template('detalle_restaurante.html', errores={}, restaurantes = {})
        
    finally:
        cursor.close()
        


        

        
        
#Ruta para el insert
@app.route('/guardarRestaurante', methods = ['POST'])
def guardarRestaurante():
    
    #lista de errores
    errores = {}
    
    #Obtener los datos a insertar
    restaurante = request.form.get('restaurante', '').strip()
    tipo = request.form.get('tipo', '').strip()
    comentario = request.form.get('comentario', '').strip()
    calificacion= request.form.get('calificacion', '').strip()
    
    
    if not restaurante:
        errores['restaurante'] = 'Nombre del restaurante obligatorio'
        
    if not tipo:
        errores['tipo'] = 'Mencionar tipo de comida'
        
    if not comentario:
        errores['comentario'] = 'Si no tiene ningún comentario escribir "ninguno"'
        
    elif not calificacion.isdigit() or int(calificacion) < 1 or int(calificacion) > 5:
        errores['califiacion'] = 'La calficación es un valor entre 1 y 5'
        
    if not errores:
    #Intentamos ejecutar el INSERT
    
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('insert into restaurantes(nombre, tipo, comentario, calificacion) values(%s, %s, %s, %s)', (restaurante, tipo, comentario, calificacion))
            mysql.connection.commit()
            flash('Restaurante guardado exitosamente')
            return redirect(url_for('home'))
            
        except Exception as e:
            mysql.connection.rollback()
            flash( f'Algo falló: {str(e)}')
            return redirect(url_for('home'))
            
        finally:
            
            cursor.close()
    
    return render_template('resgitro_restaurante.html', errores = errores)   


#Ruta para cargar datos a actualizar        
@app.route('/actualizar_restaurante/<int:id>')
def actualizarRestaurante(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from restaurantes where id = %s', (id,))
        restaurante = cursor.fetchone()
        return render_template('update_restaurante.html', restaurante = restaurante)
        
    except Exception as e:
        print('Error al consultar datos a actualizar: ' + e)
        return render_template('update_restaurante.html', errores={}, restaurantes = {})
        
    finally:
        cursor.close()


@app.route('/modificarRestaurante', methods = ['POST'])
def modificarRestaurante():
    
    #lista de errores
    errores = {}
    
    #Obtener los datos a insertar
    
    idUpdate = request.form.get('idUpdate', '').strip()
    nrestaurante = request.form.get('nrestaurante', '').strip()
    ntipo = request.form.get('ntipo', '').strip()
    ncomentario = request.form.get('ncomentario', '').strip()
    ncalificacion= request.form.get('ncalificacion', '').strip()
    
    
    if not nrestaurante:
        errores['nrestaurante'] = 'Nombre del restaurante obligatorio'
        
    if not ntipo:
        errores['ntipo'] = 'Mencionar tipo de comida'
        
    if not ncomentario:
        errores['ncomentario'] = 'Si no tiene ningún comentario escribir "ninguno"'
        
    elif not ncalificacion.isdigit() or int(ncalificacion) < 1 or int(ncalificacion) > 5:
        errores['ncalifiacion'] = 'La calficación es un valor entre 1 y 5'
        
    if not errores:
    #Intentamos ejecutar el INSERT
    
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('update restaurantes set nombre = %s, tipo = %s, comentario = %s, calificacion = %s where id = %s', (nrestaurante, ntipo, ncomentario, ncalificacion, idUpdate))
            mysql.connection.commit()
            flash('Restaurante actualizado exitosamente')
            return redirect(url_for('home'))
            
        except Exception as e:
            mysql.connection.rollback()
            flash( f'Algo falló: {str(e)}')
            return redirect(url_for('home'))
            
        finally:
            
            cursor.close()
    
    return render_template('update_restaurante.html', restaurante=(idUpdate, nrestaurante, ntipo, ncomentario, ncalificacion), errores = errores,)   

#ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8! :c', 404
    

@app.errorhandler(405)
def metodoNoPermitido(e):
    return 'Revisa el meotodo de envio de tu ruta (GET o POST)', 405


#Ruta para cargar datos a eliminar



if __name__ == '__main__':
    
    app.run(port=3000, debug = True)