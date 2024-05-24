import psycopg2
from psycopg2 import sql

from config import POSTGRES_PROPERTIES, POSTGRES_URL


def create_database(dbname):
    """
    Crée une base de données PostgreSQL.

    Paramètres :
    dbname (str) : Le nom de la base de données à créer.
    user (str) : L'utilisateur à connecter à PostgreSQL : L'utilisateur à connecter à PostgreSQL.
    password (str) : Le mot de passe de l'utilisateur spécifié : Le mot de passe de l'utilisateur spécifié.
    host (chaîne) : L'hôte sur lequel tourne le serveur PostgreSQL. La valeur par défaut est 'localhost'.
    port (chaîne) : Le port sur lequel le serveur PostgreSQL écoute. La valeur par défaut est '5432'.
    
    """
    try:
        # Connect to the default 'postgres' database
        connection = connect_to_db()
        
        connection.autocommit = True

        cursor = connection.cursor()
        
         # Check if the database exists
        cursor.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [dbname])
        exists = cursor.fetchone()
        
        if exists:
            print(f"Database '{dbname}' already exists.")
        else:
            # Create the new database
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(dbname))
            )
            print(f"Database '{dbname}' created successfully.")

    except psycopg2.Error as e:
        print(f"Error creating database: {e}")
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
 
 
def connect_to_db(dbname="postgres"):
    # Configuring the postgres connection
    connection = psycopg2.connect(
            dbname=dbname,
            user='postgres',
            password='mohamed',
            host='localhost',
            port='5432'
    )
    return connection
 
   
 
def select_data(spark, table, columns, mode, filter_condition=None):
    
    df = spark.read.jdbc(url = POSTGRES_URL, table=table, mode=mode, properties = POSTGRES_PROPERTIES )
    
    selected_df = df.select(*columns)
    
    if filter_condition:
        selected_df = selected_df.filter(filter_condition)
        
    return selected_df        
            