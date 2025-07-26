
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb
from config import Config


mysql = MySQL()

def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    
    from controllers.albumController import albumsBP
    app.register_blueprint(albumsBP)
    
    return app

app = Flask (__name__)


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


if __name__ == '__main__':
    app= createApp()
    app.run(port=3000, debug = True)