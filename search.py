from init_BD import *
import datetime


def search_reproduccion():
    '''
    Funcion que busca la reproduccion de una cancion en la tabla "reproduccion" en la base de datos.
    En caso de encontrar mas de una reproduccion para la cancion, se solicita al usuario que seleccione una.
    Finalmente, retorna un string con informacion de la cancion seleccionada.

    Parametros:
        No posee.

    Retorno:
        Un string con informacion de la cancion seleccionada. 
        En caso de no encontrar la cancion, retorna "cancion no encontrada."
    '''
    results = []
    option = 0
    while len(results) == 0:
        name = input(
            "Ingresa el nombre de la canción. Presiona enter para cancelar la operacion: ")
        if(name == ""):
            return 

        string_query = r'''
            SELECT * FROM reproduccion
            WHERE song_name LIKE '%{0}%'
            '''

        execute_query(string_query.format(name.replace("'", "''")),
                      "-----busqueda finalizada-----")
        results = query.fetchall()

        if len(results) == 0:
            return "cancion no encontrada."

    if len(results) > 1:
        for i, row in enumerate(results):
            print(f"{i+1}. {row[1]} de {row[2]}")

        option = int(input("Selecciona el numero de la canción correcta: "))-1

    fav = "Si" if results[option][5] else "No"
    song = f"\nCancion: {results[option][1]},\nArtista: {results[option][2]},\nFecha de reproduccion: {results[option][3]},\nCantidad de reproduccion: {results[option][4]},\nFavorito: {fav}"
    print(song)


def songs_to_date():
    '''
    Funcion que busca en la tabla "reproduccion" todas las canciones reproducidas desde 
    una fecha dada hasta "last_days" dias atras.
    Luego, imprime en pantalla la informacion de cada cancion obtenida.

    Parametros:
        No posee.

    Retorno:
        No posee.
    '''
    date = input("\nIngresa la fecha actual en el formato (YYYY-MM-DD): ")
    while True:
        try:
            datetime.date.fromisoformat(date)
            break
        except:
            print("formato invalido")
            date = input("\nIngresa la fecha actual en el formato (YYYY-MM-DD): ")
            continue
    last_days = int(
        input("Ingresa hasta cuantos dias atras deseas buscar: "))

    # Se hace de esta manera debido a que la fecha se pide. Se podría hacer con la fecha actúal, pero el resultado seria muy limitado.
    string_query = r'''
            SELECT * FROM reproduccion
            WHERE fecha_reproduccion >= DATEADD(day,-{0}, CONVERT(date, '{1}', 23))
            AND fecha_reproduccion <= CONVERT(date, '{1}', 23)
    '''
    execute_query(string_query.format(last_days, date),
                  "-----busqueda finalizada-----")
    results = query.fetchall()
    for song in results:
        fav = "Si" if song[5] else "No"
        string_song = f"\nCancion: {song[1]},\nArtista: {song[2]},\nFecha de reproduccion: {song[3]},\nCantidad de reproduccion: {song[4]},\nFavorito: {fav}"
        print(f"{string_song}\n")


def search_name_artist():
    '''
    Función que busca un nombre de canción o artista en la base de datos 
    y devuelve los resultados correspondientes de la cancion.

    Parametros:
        No posee.

    Retorno:
        Si encuentra una única canción o artista, devuelve una cadena con el nombre de la canción y el artista.
        Si encuentra múltiples resultados, imprime en consola los nombres de las canciones y artistas encontrados.
        Si no encuentra ningún resultado, devuelve una cadena indicando que la búsqueda no arrojó resultados.
    '''
    results = []
    while len(results) == 0:
        name = input(
            "Ingresa el nombre de la canción o artista. Presiona enter para cancelar la operacion: ")
        if (name == ""):
            return

        string_query = r'''
            SELECT * FROM repositorio_musica
            WHERE song_name LIKE '%{0}%' OR artist_name = '{0}'
            '''

        execute_query(string_query.format(name.replace("'", "''")),
                      "-----busqueda finalizada-----")
        results = query.fetchall()

        if len(results) == 0:
            return "cancion o artista no encontrados."

    if len(results) > 1:
        for i, row in enumerate(results):
            print(f"{i+1}. {row[3]} de {row[2]}")

def search_song():
    '''
    Funcion que busca una canción en la tabla repositorio_musica.

    Parametros:
        No posee.

    Retorno:
        results (list): Lista que contiene la información de la canción encontrada.
    '''
    results = []

    while len(results) == 0:
        name = input(
            "Ingresa el nombre de la canción o presiona enter para cancelar la operacion: ")
        if (name == ""):
            return []

        string_query = r'''
            SELECT * FROM repositorio_musica
            WHERE song_name LIKE '%{0}%'
            '''

        execute_query(string_query.format(name.replace("'", "''")),
                      "-----busqueda finalizada-----")
        results = query.fetchall()

        if len(results) == 0:
            print("cancion no encontrada")

    for i, row in enumerate(results):
        print(f"{i+1}. {row[3]} de {row[2]}")

    if len(results) > 1:
        option = int(input("Selecciona el numero de la canción correcta: "))-1
        results = [results[option]]

    return results[0]
