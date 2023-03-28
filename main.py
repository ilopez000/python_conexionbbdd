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


#elimina de la tabla la persona con identificador=id
def delete_persona(conn, table_name, id):
    cursor = conn.cursor()
    try:

        query = f"DELETE FROM {table_name} WHERE id={id}"
        cursor.execute(query)
        conn.commit()
        print(f'La persona com id {id} ha sido eliminada exitosamente en la tabla {table_name}')
    except mysql.connector.Error as e:
        print(e)


#devuelve el resultado de ejecutar consulta_mysql en la tabla table_name
#SELECT * FROM table_name WHERE id>100
def resultado_consulta(conn,  consulta_mysql):
    cursor = conn.cursor()
    try:
        cursor.execute(consulta_mysql)
        rows = cursor.fetchall()
        res = []
        for row in rows:
            aux = Persona(row[0], row[1], row[2], row[3])
            res.append(aux)

        return res

    except mysql.connector.Error as e:
        print(e)


if __name__ == '__main__':
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'persona'

    Personas=[]

    #conn = connect_to_db(host, user, password, database)

    #if conn:
        #Personas = fetch_personas(conn, 'datos')
        #close_connection(conn)


    #conn2 = connect_to_db(host, user, password, database)

    #if conn2:
        #delete_persona(conn2, 'datos', 499)
        #close_connection(conn2)

    #if conn2:
        #persona_nueva = Persona(501, 'Nombre501', 'Apellido1_501', 'Apellido2_501')
        #add_persona(conn2, 'datos', persona_nueva)
        #close_connection(conn2)


    conn3 = connect_to_db(host, user, password, database)
    if conn3:
        Personas=resultado_consulta(conn3, 'SELECT * FROM datos WHERE id<300')
        close_connection(conn3)

for p in Personas:
    p.imprimir_persona() #== print(p)

