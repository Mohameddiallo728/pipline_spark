import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F


  
def download_csv(folderName, years):
    # Chemin absolu vers le répertoire du projet
    project_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(project_dir, folderName)

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    for year in years:
        # Construire l'URL et le nom du fichier
        url = f"https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_{year}.zip"
        file_name = f"microdados_censo_escolar_{year}.zip"
        file_path = os.path.join(data_dir, file_name)

        # Télécharger le fichier zip
        command  = f"wget --no-check-certificate {url} -P {data_dir}"
        os.system(command)

        # Décompresser le fichier zip
        command = f"unzip {file_path} -d {data_dir}"
        os.system(command)

        # Déplacer les fichiers .csv vers le répertoire ./data
        csv_folder = f"microdados_ed_basica_{year}/dados/"
        csv_path = os.path.join(data_dir, csv_folder)
        csv_files = [f for f in os.listdir(csv_path) if f.lower().endswith('.csv')]
        for csv_file in csv_files:
            old_file_path = os.path.join(csv_path, csv_file)
            new_file_path = os.path.join(data_dir, f"{year}.csv")
            os.rename(old_file_path, new_file_path)

        # Effacer les fichiers et dossiers temporaires
        os.remove(file_path)
        os.system(f"rm -rf {os.path.join(data_dir, f'microdados_ed_basica_{year}')}")
   
    
    
def create_spark_session():
    """
    Crée et configure une session Spark
    
    Configuration :
    - appName : Définit le nom de l'application Spark à "CensoEscolarStarSchema".
    - spark.sql.shuffle.partitions : Configure le nombre de partitions pour les opérations de 
      pour les opérations de mélange à 4, ce qui permet d'optimiser les performances des 
      de données plus petits en réduisant la charge de travail liée à la gestion d'un trop grand nombre de partitions.
      
    """
    # Chemin vers le fichier JAR du driver PostgreSQL
    driver_path = "/home/mohamed/.config/JetBrains/IntelliJIdea2021.1/jdbc-drivers/PostgreSQL/42.2.5/postgresql-42.2.5.jar"

    try:
        spark = SparkSession.builder \
            .appName("CensoEscolarStarSchema") \
            .config("spark.jars", driver_path) \
            .getOrCreate()
        
        print("Spark session created successfully")
        return spark
    
    except Exception as e:
        print(f"Failed to create Spark session: {e}")
        return None    
 
 
 
def read_csv(spark):
    data_csv = (
        spark
        .read
        .format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .option("delimiter", ";")
        .option("encoding", "latin1")
        .load("./data/csv/*.csv")
    )
    
    return data_csv
      
  
    
def convert_to_parquet(data, folderName): 
    return data.write.parquet("./" + folderName)



def read_parquet(spark):
    data_parquet = (
        spark
        .read
        .format("parquet")
        .load("./data/parquets/")
    )
    
    return data_parquet