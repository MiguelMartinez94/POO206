
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask (__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Kesadilla94"
app.config['MYSQL_DB'] = "dbflask"
#app.config['MYSQL_PORT'] = 3306

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
        
#ruta con parámetros
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return '¡Hola, '+nombre+'!'

        
#ruta try-catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8! :c', 404
    
#ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleRoute():
    return 'Hola soy el mismo recurso del servidor'

#ruta POST
@app.route('/usuario', methods = ['POST'])
def formulario():
    return 'Soy un formulario'

@app.errorhandler(405)
def metodoNoPermitido(e):
    return 'Revisa el meotodo de envio de tu ruta (GET o POST)', 405

    
if __name__ == '__main__':
    
    app.run(port=3000, debug = True)