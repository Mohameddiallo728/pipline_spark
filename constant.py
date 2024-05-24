

DIM_COLUMNS = [
  'NO_UF', 'SG_UF', 'CO_UF', # State's data
  'NO_MUNICIPIO', 'CO_MUNICIPIO' # City's data
]

INTEGER_DIMENSIONS = [
    "TP_DEPENDENCIA",           # The school administration (state, city, private) 
    "TP_LOCALIZACAO",           # The school location (urban rural)
    "IN_AGUA_POTAVEL",          # has access to drinkable water 
    "IN_ENERGIA_INEXISTENTE",   # has (NOT) access to energy
    "IN_ESGOTO_INEXISTENTE",    # has (NOT) access to energy
    "IN_BANHEIRO",              # has restroom
    "IN_BIBLIOTECA",            # has library
    "IN_REFEITORIO",            # has canteen 
    "IN_COMPUTADOR",            # has computer
    "IN_INTERNET",              # has internet
    "IN_EQUIP_NENHUM"           # no electronic equipment
]

FACT_TABLE_NAME = "FACT_CENSO_ESCOLAR"

FACT_COLUMNS = [
    "QT_DOC_BAS",  	# Number of Teachers in the basic education (TOTAL)
    "QT_DOC_INF",	  # Number of Teachers in the basic education (child education)
    "QT_DOC_FUND",	# Number of Teachers in the basic education (elementary education)
    "QT_DOC_MED",	  # Number of Teachers in the basic education (high school)
  
    "QT_MAT_BAS",	  # Number of enrollments in the basic education (TOTAL)
    "QT_MAT_INF",	  # Number of enrollments in the basic education (child education)
    "QT_MAT_FUND",	# Number of enrollments in the basic education (elementary education)
    "QT_MAT_MED",	  # Number of enrollments in the basic education (high school)

    "QT_MAT_BAS_ND",	      # Number of enrollments in the basic education - Skin color/Race Not Declared
    "QT_MAT_BAS_BRANCA",	  # Number of enrollments in the basic education - Skin color/Race Branco
    "QT_MAT_BAS_PRETA",	    # Number of enrollments in the basic education - Skin color/Race Preto
    "QT_MAT_BAS_PARDA",	    # Number of enrollments in the basic education - Skin color/Race Parda
    "QT_MAT_BAS_AMARELA",	  # Number of enrollments in the basic education - Skin color/Race Amarela
    "QT_MAT_BAS_INDIGENA",	# Number of enrollments in the basic education - Skin color/Race Indígena
    
    "NU_ANO_CENSO"          # Census' year
]