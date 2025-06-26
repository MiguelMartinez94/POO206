
from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL
import MySQLdb

app = Flask (__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Kesadilla94"
app.config['MYSQL_DB'] = "db_albums"
#app.config['MYSQL_PORT'] = 3306
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

#ruta básica
@app.route('/DBCheck')
def DB_check():
    try:
        
        cursor = mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify({'status':'ok', 'message':'Conectado con exito'}), 200        
        
        
    except MySQLdb.MySQLError as e:
        return jsonify({'status':'error', 'message':str(e)}), 500  
        

        
#ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8! :c', 404
    

@app.errorhandler(405)
def metodoNoPermitido(e):
    return 'Revisa el meotodo de envio de tu ruta (GET o POST)', 405

#Ruta de inicio
@app.route('/')
def home():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from albums')
        consultaTodo = cursor.fetchall()
        return render_template('formulario.html', errores={}, albums = consultaTodo)
        
    except Exception as e:
        print('Error al consultar todo: ' + e)
        return render_template('formulario.html', errores={}, albums = {})
        
    finally:
        cursor.close()
        
@app.route('/detalle/<int:id>')
def detalle(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from albums where id = %s', (id,))
        consultaId = cursor.fetchone()
        return render_template('consulta.html', album = consultaId)
        
    except Exception as e:
        print('Error al consultar todo: ' + e)
        return render_template('consulta.html', errores={}, albums = {})
        
    finally:
        cursor.close()



#Ruta de consulta
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Ruta para el insert
@app.route('/guardarAlbum', methods = ['POST'])
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
            cursor = mysql.connection.cursor()
            cursor.execute('insert into albums(album, artista, anio) values(%s, %s, %s)', (titulo, artista, anio))
            mysql.connection.commit()
            flash('Album se guardó en BD')
            return redirect(url_for('home'))
            
        except Exception as e:
            mysql.connection.rollback()
            flash( f'Algo falló: {str(e)}')
            return redirect(url_for('home'))
            
        finally:
            
            cursor.close()
    
    return render_template('formulario.html', errores = errores)
    
if __name__ == '__main__':
    
    app.run(port=3000, debug = True)