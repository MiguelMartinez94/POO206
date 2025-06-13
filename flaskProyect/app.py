
from flask import Flask

app = Flask (__name__)


#ruta básica
@app.route('/')
def home():
    return 'Hola mundo FLASK'
        
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