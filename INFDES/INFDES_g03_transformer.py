from pandas import DataFrame
from data_transformers import chain, transformer


#  DEFINITIONS_START
@transformer.convert
def rename_cols(df: DataFrame, map):
    df = df.rename(columns=map)
    return df

@transformer.convert
def drop_col(df: DataFrame, col, axis=1):
    return df.drop(col, axis=axis)

@transformer.convert
def drop_col(df: DataFrame, col, axis=1):
    return df.drop(col, axis=axis)

@transformer.convert
def drop_col(df: DataFrame, col, axis=1):
    return df.drop(col, axis=axis)

@transformer.convert
def query(df: DataFrame, condition: str):
    df = df.query(condition)    
    return df
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
rename_cols(map={'iso3': 'geocodigo', 'cat_ocup_detalle': 'indicador'}),
	drop_col(col='formal_def_productiva', axis=1),
	drop_col(col='cat_ocup_cod', axis=1),
	drop_col(col='pais', axis=1),
	query(condition='anio == anio.max() & indicador != "Total formal"')
)
#  PIPELINE_END


#  start()
#  RangeIndex: 120 entries, 0 to 119
#  Data columns (total 7 columns):
#   #   Column                 Non-Null Count  Dtype  
#  ---  ------                 --------------  -----  
#   0   iso3                   120 non-null    object 
#   1   pais                   120 non-null    object 
#   2   anio                   120 non-null    int64  
#   3   formal_def_productiva  120 non-null    object 
#   4   cat_ocup_cod           105 non-null    float64
#   5   cat_ocup_detalle       120 non-null    object 
#   6   valor                  120 non-null    float64
#  
#  |    | iso3   | pais      |   anio | formal_def_productiva   |   cat_ocup_cod | cat_ocup_detalle   |   valor |
#  |---:|:-------|:----------|-------:|:------------------------|---------------:|:-------------------|--------:|
#  |  0 | ARG    | Argentina |   2022 | Formal                  |              1 | Empleadores        |     3.7 |
#  
#  ------------------------------
#  
#  rename_cols(map={'iso3': 'geocodigo', 'cat_ocup_detalle': 'indicador'})
#  RangeIndex: 120 entries, 0 to 119
#  Data columns (total 7 columns):
#   #   Column                 Non-Null Count  Dtype  
#  ---  ------                 --------------  -----  
#   0   geocodigo              120 non-null    object 
#   1   pais                   120 non-null    object 
#   2   anio                   120 non-null    int64  
#   3   formal_def_productiva  120 non-null    object 
#   4   cat_ocup_cod           105 non-null    float64
#   5   indicador              120 non-null    object 
#   6   valor                  120 non-null    float64
#  
#  |    | geocodigo   | pais      |   anio | formal_def_productiva   |   cat_ocup_cod | indicador   |   valor |
#  |---:|:------------|:----------|-------:|:------------------------|---------------:|:------------|--------:|
#  |  0 | ARG         | Argentina |   2022 | Formal                  |              1 | Empleadores |     3.7 |
#  
#  ------------------------------
#  
#  drop_col(col='formal_def_productiva', axis=1)
#  RangeIndex: 120 entries, 0 to 119
#  Data columns (total 6 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   geocodigo     120 non-null    object 
#   1   pais          120 non-null    object 
#   2   anio          120 non-null    int64  
#   3   cat_ocup_cod  105 non-null    float64
#   4   indicador     120 non-null    object 
#   5   valor         120 non-null    float64
#  
#  |    | geocodigo   | pais      |   anio |   cat_ocup_cod | indicador   |   valor |
#  |---:|:------------|:----------|-------:|---------------:|:------------|--------:|
#  |  0 | ARG         | Argentina |   2022 |              1 | Empleadores |     3.7 |
#  
#  ------------------------------
#  
#  drop_col(col='cat_ocup_cod', axis=1)
#  RangeIndex: 120 entries, 0 to 119
#  Data columns (total 5 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  120 non-null    object 
#   1   pais       120 non-null    object 
#   2   anio       120 non-null    int64  
#   3   indicador  120 non-null    object 
#   4   valor      120 non-null    float64
#  
#  |    | geocodigo   | pais      |   anio | indicador   |   valor |
#  |---:|:------------|:----------|-------:|:------------|--------:|
#  |  0 | ARG         | Argentina |   2022 | Empleadores |     3.7 |
#  
#  ------------------------------
#  
#  drop_col(col='pais', axis=1)
#  RangeIndex: 120 entries, 0 to 119
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  120 non-null    object 
#   1   anio       120 non-null    int64  
#   2   indicador  120 non-null    object 
#   3   valor      120 non-null    float64
#  
#  |    | geocodigo   |   anio | indicador   |   valor |
#  |---:|:------------|-------:|:------------|--------:|
#  |  0 | ARG         |   2022 | Empleadores |     3.7 |
#  
#  ------------------------------
#  
#  query(condition='anio == anio.max() & indicador != "Total formal"')
#  Index: 70 entries, 0 to 104
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  70 non-null     object 
#   1   anio       70 non-null     int64  
#   2   indicador  70 non-null     object 
#   3   valor      70 non-null     float64
#  
#  |    | geocodigo   |   anio | indicador   |   valor |
#  |---:|:------------|-------:|:------------|--------:|
#  |  0 | ARG         |   2022 | Empleadores |     3.7 |
#  
#  ------------------------------
#  