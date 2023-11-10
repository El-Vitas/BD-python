# BD-python

Codigo para el ramo base de datos en el cual se usa SQL-Server con python para realizar el manejo de datos desde un .csv

Sobre el codigo:
	El codigo fue realizado mediante distintas querys las cuales luego pueden ser formateadas para realizar el execute del query, se incluye una funcion de sql y una view las cuales fueron solicitadas. Se realiza verificación de los datos ingresados por parte del usuario. El codigo consta de un menu en el cual se pueden realizar todas las operaciones solicitadas, además de la operacion de salir y de crear tablas.

En la busqueda de canciones o de artistas, si el nombre de la canción u artista coincide con otro, entonces se le solicita al usuario que escoja el correspondiente. En la opcion buscar por nombre o por artistas muestra todas las canciones con ese nombre o del artista.

En la operacion de busqueda por x dias anteriores, reproduccion y añadir a favoritos, se le solicita al usuario una fecha actual, ya que si se considera la fecha actual al momento de mostrar el ejemplo del codigo estarían todas las canciones con la misma fecha y no se vería la utilidad de estas operaciones. Por ello la busqueda por x dias anteriores tambien pide una fecha actual, en la cual se mostrarán las canciones hasta x dias anteriores, si existen canciones con fechas futuras, siplemente se ignoran.

Instrucciones: 
	Se debe tener creada una base de datos y añadir los datos correspondientes en un .env, con los nombres de las variables que aparecen en Init_BD
	Se debe tener todos los archivos .py dentro de una misma carpeta e iniciar el programa en el main.py.
