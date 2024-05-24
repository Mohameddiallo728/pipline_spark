from constant import FACT_COLUMNS, INTEGER_DIMENSIONS


POSTGRES_URL = "jdbc:postgresql://localhost:5432/censo_escolar"

POSTGRES_PROPERTIES = {
    "user": "postgres", 
    "password": "mohamed",
    "driver": "org.postgresql.Driver"
}


DIMENSION_TABLES_CONFIG = {
    "DIM_LOCAL":{
        "fields": [
            {"field":"NO_UF", "type":"string",},        # State's name 
            {"field":"SG_UF", "type":"string",},        # State's abbreviation
            {"field":"CO_UF", "type":"string",},        # State's code
            {"field":"NO_MUNICIPIO", "type":"string",}, # City's name
            {"field":"CO_MUNICIPIO", "type":"string",}  # City's code
        ]
    },
}



DIMENSION_TABLES_CONFIG.update(
    {
        "DIM_"+dimension.upper():{
            "fields": [
                {"field":dimension, "type":"integer"} 
            ]
        }
        for dimension in INTEGER_DIMENSIONS
    }
)




FACT_CONFIG = {
    fact:{
        "fields": [
            {"field":fact, "type":"integer"}
        ]
    }
    for fact in FACT_COLUMNS
}

DIMENSION_ID_CONFIG = {
    table_name:[
        field['field'] 
        for field 
        in table_fields['fields']
    ]
    for table_name, table_fields in DIMENSION_TABLES_CONFIG.items()
}



FACT_TABLE_ALL_COLUMNS_ORDERED = FACT_COLUMNS + list(map(lambda col:"ID_"+col, DIMENSION_ID_CONFIG.keys()))

