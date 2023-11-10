
CREATE_REPOSITORIO_MUSICA_TABLE = r'''
    IF OBJECT_ID (N'repositorio_musica', N'U') IS NULL 
        BEGIN
            CREATE TABLE repositorio_musica(
            id INTEGER PRIMARY KEY IDENTITY(1,1),
            position INTEGER,
            artist_name VARCHAR(50),
            song_name VARCHAR(100),
            days INTEGER,
            top_10 INTEGER,
            peak_position INTEGER,
            peak_position_time VARCHAR(7),
            peak_streams INTEGER,
            total_streams INTEGER
            );
        END  
'''

CREATE_REPRODUCCION_TABLE = r'''
    IF OBJECT_ID (N'reproduccion', N'U') IS NULL 
        BEGIN
            CREATE TABLE reproduccion(
                id INTEGER PRIMARY KEY,
                song_name VARCHAR(100),
                artist_name VARCHAR(50),
                fecha_reproduccion DATE,
                cant_reproducciones INTEGER,
                favorito BIT
            );
        END
'''

CREATE_LISTA_FAVORITOS_TABLE = r'''
    IF OBJECT_ID (N'lista_favoritos', N'U') IS NULL 
        BEGIN
            CREATE TABLE lista_favoritos(
                id INTEGER PRIMARY KEY,
                song_name VARCHAR(100),
                artist_name VARCHAR(50),
                fecha_agregada DATE
            );
        END
'''

CREATE_ARTIST_STATS_VIEW = r'''
    CREATE OR ALTER VIEW [ArtistStats] AS
    SELECT artist_name, MIN(peak_position) peak_position, SUM(cast(top_10 as bigint)) Total_top_15, SUM(cast(total_streams as bigint)) sum_streams, COUNT(*)num_songs
    FROM repositorio_musica 
    GROUP BY artist_name
'''

CREATE_PROMEDIO_FUNCTION = r'''
    CREATE OR ALTER FUNCTION Promedio (@cantidad INTEGER, @suma BIGINT) 
    RETURNS BIGINT AS
    BEGIN
        DECLARE @avg BIGINT
        SET @avg = @suma/@cantidad
        RETURN @avg
    END 
'''

INSERT_FAVORITO = r'''
    IF NOT EXISTS(SELECT * FROM lista_favoritos WHERE id = {0})
        BEGIN
            INSERT INTO
            lista_favoritos(id, song_name, artist_name, fecha_agregada)
            VALUES
            ({0}, '{1}', '{2}', CONVERT(date, '{3}', 23));

            UPDATE reproduccion
            SET favorito = 1
            WHERE id = {0}
        END
'''

SELECT_FAVORITO = r'''
    SELECT * FROM lista_favoritos
    WHERE song_name LIKE '%{0}%'
'''

DELETE_FAVORITO = r'''
    DELETE FROM lista_favoritos
    WHERE id = {0}

    UPDATE reproduccion
    SET favorito = 0
    WHERE id = {0}
'''

INSERT_AND_UPDATE = r'''
    IF NOT EXISTS(SELECT * FROM reproduccion WHERE id = {0})
        BEGIN
            INSERT INTO
            reproduccion(id, song_name, artist_name, fecha_reproduccion, cant_reproducciones, favorito)
            VALUES
            ({0}, '{1}', '{2}', CONVERT(date, '{3}', 23), {4}, {5});
        END
    ELSE
        BEGIN
            UPDATE reproduccion
            SET cant_reproducciones = (cant_reproducciones + 1)
            WHERE id = {0};
        END
'''

DELETE_DATA = r'''
    IF OBJECT_ID('repositorio_musica', 'U') IS NOT NULL
        DROP TABLE repositorio_musica;

    IF OBJECT_ID('reproduccion', 'U') IS NOT NULL
        DROP TABLE reproduccion;

    IF OBJECT_ID('lista_favoritos', 'U') IS NOT NULL
        DROP TABLE lista_favoritos;

    IF OBJECT_ID('[ArtistStats]', 'FN') IS NOT NULL
        DROP VIEW [ArtistStats];

    IF OBJECT_ID('Promedio', 'V') IS NOT NULL
        DROP FUNCTION Promedio;
'''