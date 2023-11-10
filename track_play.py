from init_BD import *
import datetime
from querys import INSERT_AND_UPDATE
def show_playback():
    '''
    Funcion que muestra las reproducciones ordenadas por fecha o por cantidad de veces reproducida.

    Parametros:
        No posee.

    Retorno:
        No posee.
    '''
    string_query = r'''
        IF EXISTS (SELECT 1 FROM reproduccion)
            SELECT * FROM reproduccion;
    '''

    while True:
        string_query = menu_show_playback(string_query)
        if (string_query == 'e'): return
        
        try:
            execute_query(string_query,"");
            results = query.fetchall()
            for i in results:
                print(
                    f"{i[1]} de {i[2]}\nPrimera reproduccion:{i[3]}\nCantidad de reproducciones {i[4]}\n")
        except pyodbc.Error as e:
            print("\nNo posees canciones en la lista de reproducción.")
        

def menu_show_playback(string_query: str):
    print("Elija la forma en la que desea ordenar el registro de reproducciones:")
    print("1.fecha de reproduccion\n2.cantidad de veces reproducida\n3.cancelar operación")
    opcionParametro = input("opcion: ")

    if(opcionParametro == '3'):
        return 'e'

    print("\nelija una opcion")
    print("1.Ascendente\n2.Descentente")
    opcionOrden = input("opcion: ")

    match opcionOrden:
        case "1":
            opcionOrden = "ASC"
        case "2":
            opcionOrden = "DESC"
        case _:
            print("operacion invalida")
            return 'e'

    match opcionParametro:
        case "1":
            string_query.format("fecha_reproduccion", opcionOrden)
        case "2":
            string_query.format("cant_reproducciones", opcionOrden)
        case _:
            print("operacion invalida")
            return 'e'

    return string_query

def add_and_update_song(song: tuple):
    '''
    Funcion que agrega una cancion a la tabla 'reproduccion' o actualiza la cantidad
     de veces que ha sido reproducidaen caso de que no exista.

    Parametros:
        song (tuple): Tupla con la informacion de la cancion (id, nombre, artista, duracion)

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
    string_query = INSERT_AND_UPDATE.format(song[0], song[3], song[2], date, 1, 0)
    execute_query(string_query, f"\nsonando {song[3]} de {song[2]}")
    connection.commit()
