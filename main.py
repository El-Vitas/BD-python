from init_BD import connection
from db_creator import *
from track_play import *
from favorites import *
from search import *
from stats import *
from delete import delete_data


def menu():
    '''
    Función que muestra el menú principal y ejecuta la opción elegida por el usuario.

    Parametros:
        No posee.

    Retorno:
        No posee.
    '''
    flag_continue = True
    while (flag_continue):
        print("\n0. Terminar el programa.\n1. Crear tablas, funciones y vistas.\n2. Poblar 'repositorio_musica'\n3. Eliminar datos.\n4. Mostrar canciones en reproducción.\n5. Añadir canción a favoritos.\n6. Eliminar canción de favoritos.\n7. Mostrar canciones favoritas.\n8. Reproducir una canción.\n9. Buscar una canción en la tabla Reproduccion.\n10. Mostrar todas las canciones escuchadas en los últimos X días.\n11. Buscar por nombre de canción y por artista.\n12. Top 15 artistas con la mayor cantidad total de veces en que sus canciones han estado en el top 10.\n13. Peak position de un artista.\n14. Promedio de streams totales.")
        option = input("\nIngresa la opcion que desees: ")
        match option:
            case "0":
                flag_continue = False
            case "1":
                create_tables()
                create_functions()
                create_views()
            case "2":
                insert_data()
            case "3":
                delete_data()
            case "4":
                show_playback()

            case "5":
                add_favorites()

            case "6":
                delete_favorites()

            case "7":
                show_favorites()

            case "8":
                results = search_song()
                add_and_update_song(results)

            case "9":
                search_reproduccion()

            case "10":
                songs_to_date()

            case "11":
                search_name_artist()

            case "12":
                top_15()

            case "13":
                peak_position()

            case "14":
                avg_streams()

            case _:
                print("Valor incorrecto. Intenta nuevamente.")


def main():
    '''
    Función principal que llama a la función menu()

    Parametros:
        No posee.

    Retorno:
        No posee.
    '''
    menu()
    connection.close()


if __name__ == "__main__":
    main()
