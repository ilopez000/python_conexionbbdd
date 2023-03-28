import mysql.connector
from Persona import Persona

def connect_to_db(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(f'Conexión exitosa a la base de datos {database}')
        return conn
    except mysql.connector.Error as e:
        print(e)


def close_connection(conn):
    if conn:
        conn.close()
        print('Conexión cerrada')


def fetch_personas(conn, table_name):
    cursor = conn.cursor()
    try:
        cursor.execute(f'SELECT * FROM {table_name}')
        rows = cursor.fetchall()
        print(rows)
        personas = []
        for row in rows:
            persona = Persona(row[0], row[1], row[2], row[3])
            personas.append(persona)
        return personas
    except mysql.connector.Error as e:
        print(e)

def add_persona(conn, table_name, persona):
    cursor = conn.cursor()
    try:
        query = f"INSERT INTO {table_name} (id, nombre, apellido1, apellido2) VALUES (%s, %s, %s, %s)"
        values = (persona.id, persona.nombre, persona.apellido1, persona.apellido2)
        cursor.execute(query, values)
        conn.commit()
        print(f'Persona insertada exitosamente en la tabla {table_name}')
    except mysql.connector.Error as e:
        print(e)


if __name__ == '__main__':
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'persona'

    Personas=[]

    conn = connect_to_db(host, user, password, database)

    if conn:
        Personas = fetch_personas(conn, 'datos')
        close_connection(conn)


    conn2 = connect_to_db(host, user, password, database)


    #if conn2:
        #persona_nueva = Persona(501, 'Nombre501', 'Apellido1_501', 'Apellido2_501')
        #add_persona(conn, 'datos', persona_nueva)
        #close_connection(conn2)


for p in Personas:
    print(p)

