from app import mysql

#Método para obtener albums activos
def getAll():
    cursor = mysql.connection.cursor()
    cursor.execute('select * from albums where state = 1')
    consultaTodo = cursor.fetchall()
    cursor.close()
    return consultaTodo


#Obtener album por id

def getById(id):
    cursor = mysql.connection.cursor()
    cursor.execute('select * from albums where id = %s', (id,))
    consultaId = cursor.fetchone()
    cursor.close()
    return consultaId

#Método para insertar un álbum

def insertAlbum(titulo, artista, anio):
    cursor = mysql.connection.cursor()
    cursor.execute('insert into albums(album, artista, anio) values(%s, %s, %s)', (titulo, artista, anio))
    mysql.connection.commit()
    cursor.close()
    
#Método para actualizar un album

def updateAlbum(idUpdate, nTitulo, nArtista, nAnio):
    cursor = mysql.connection.cursor()
    cursor.execute('update albums set album = %s, artista = %s, anio = %s where id = %s', (nTitulo, nArtista, nAnio, idUpdate))
    mysql.connection.commit()
    cursor.close()
    
#método para eliminar un album
def softDeleteAlbum(id):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE albums SET state = 0 WHERE id = %s', (id,))
    mysql.connection.commit()
    