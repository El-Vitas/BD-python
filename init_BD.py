from decouple import config
import pyodbc

try:
    driver = config('DB_DRIVER')
    server = config('DB_SERVER')
    database = config('DB_DATABASE')

    connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    connection = pyodbc.connect(connection_string)
    query = connection.cursor()
    print("conexión exitosa")
except Exception as e:
    print(e)
    exit()


def execute_query(string_query, message):
    '''
    Funcion que sirve para evitar problemas con el manejo de querys en SQL SERVER. Finaliza el programa en caso de error

    Parametros:
        query (str): query que irá en el archivo.
        message (str): Mensaje que indica si el programa fue ejecutado correctamente.

    Retorno:
        No posee. Termina el programa en caso de error.
    '''
    try:
        query.execute(string_query)
        print(message)
    except Exception as e:
        print(e)
        exit()

