from init_BD import *

def top_15():
    '''
    Funcion que utiliza una query y una view para buscar los 15 artistas con mas reproducciones en la view ArtistStats.

    Parametros:
        No recibe parametros.
    
    Retorno:
        No posee.
    '''
    string_query = r'''
        SELECT TOP (15) [artist_name], [Total_top_15]
        FROM [ArtistStats] ORDER BY [Total_top_15] DESC
        '''

    execute_query(string_query, "busqueda finalizada\n")
    results = query.fetchall()
    for num, result in enumerate(results):
        print(f"{num+1}. {result[0]} con {result[1]} veces en top 10")

def peak_position():
    '''
    Funcion que utiliza una query y una view para buscar la posicion mas alta alcanzada por un artista en la view ArtistStats.

    Parametros:
        No recibe parametros.

    Retorno:
        No posee.
    '''
    string_query = r'''
        SELECT artist_name, peak_position FROM [ArtistStats] WHERE [artist_name] = '{0}'
        '''
    artist = input("ingresa el nombre del artista o presiona enter para cancelar la operacion: ")
    if(artist == ""):
        return
    
    execute_query(string_query.format(artist), "")
    results = query.fetchall()
    if(len(results) == 0):
       print("artista no encontrado")
       return
    
    name_artist = results[0][0]
    pos_artist = results[0][1]
    print(f"la posicion mas alta alcanzada por {name_artist} es {pos_artist}")

def avg_streams():
    '''
    Funcion que utiliza una query y una view para buscar el promedio de reproducciones de un artista en la view ArtistStats.

    Parametros:
        No recibe parametros.

    Retorno:
        No posee.
    '''
    string_query = r'''
        SELECT artist_name, dbo.Promedio(num_songs, sum_streams) FROM [ArtistStats] WHERE [artist_name] = '{0}'
        '''
    artist = input("ingresa el nombre del artista o presiona enter para cancelar la operacion: ")
    if(artist == ""):
        return
    
    execute_query(string_query.format(artist), "")
    results = query.fetchall()
    if(len(results) == 0):
        print("artista no encontrado")
        return

    name_artist = results[0][0]
    avg_rep = results[0][1]
    print(f"promedio de reproducciones de {name_artist} es {avg_rep}")
