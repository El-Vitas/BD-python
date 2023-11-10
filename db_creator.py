from init_BD import query, connection, execute_query
import csv
import querys

def create_tables():
    '''
    Funcion encargada de crear distintos tipos de tablas.

    Parametros:
        No posee.

    Retorno:
        No posee. Inserta los datos en la base de datos y realiza un commit a la base de datos.
    '''
    execute_query(querys.CREATE_REPOSITORIO_MUSICA_TABLE, "tabla 'repositorio_musica' creada")

    execute_query(querys.CREATE_REPRODUCCION_TABLE, "tabla 'reproduccion' creada")

    execute_query(querys.CREATE_LISTA_FAVORITOS_TABLE, "tabla 'lista_favoritos' creada")

    connection.commit()

def create_views():
    '''
    Funcion encargada de crear vistas.

    Parametros:
        No posee.

    Retorno:
        No posee. Inserta los datos en la base de datos y realiza un commit a la base de datos.
    '''
    execute_query(querys.CREATE_ARTIST_STATS_VIEW.format(), "View 'ArtistStats' Creada")

def create_functions():
    '''
    Funcion encargada de crear functions de la base de dato.

    Parametros:
        No posee.

    Retorno:
        No posee. Inserta los datos en la base de datos y realiza un commit a la base de datos.
    '''
    execute_query(querys.CREATE_PROMEDIO_FUNCTION.format(), "Funcion 'Promedio' Creada")
    
def insert_data():
    '''
    Funcion que lee un archivo CSV llamado 'song.csv', que contiene canciones y datos relacionados con ellas, e inserta los datos en la tabla 'repositorio_musica'.

    Parametros:
        No posee.

    Retorno:
        No posee. Inserta los datos en la base de datos y realiza un commit a la base de datos.
    '''
    with open('song.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            string_query = r'''
                IF NOT EXISTS(SELECT * FROM repositorio_musica WHERE artist_name = '{1}' AND song_name = '{2}')
                INSERT INTO
                    repositorio_musica(position, artist_name, song_name, days, top_10, peak_position, peak_position_time, peak_streams, total_streams)
                VALUES
                    ({0}, '{1}', '{2}', {3}, {4}, {5}, '{6}', {7}, {8});
                '''
            # Se eliminan los "'" de las canciones y de los artistas evitando problemas al insertar
            array_query = row[0].split(";")
            array_query[1] = array_query[1].replace("'", "''").strip()
            array_query[2] = array_query[2].replace("'", "''").strip()
            # Se establece el formato al stringQuery y luego se ejecuta el query
            query.execute(string_query.format(*array_query))
    connection.commit()
    print("Base de datos poblada correctamente.")
