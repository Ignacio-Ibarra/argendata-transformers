from pandas import DataFrame
from data_transformers import chain, transformer


#  DEFINITIONS_START
@transformer.convert
def drop_col(df: DataFrame, col, axis=1):
    return df.drop(col, axis=axis)

@transformer.convert
def drop_col(df: DataFrame, col, axis=1):
    return df.drop(col, axis=axis)

@transformer.convert
def rename_cols(df: DataFrame, map):
    df = df.rename(columns=map)
    return df

@transformer.convert
def query(df: DataFrame, condition: str):
    df = df.query(condition)    
    return df

@transformer.convert
def drop_col(df: DataFrame, col, axis=1):
    return df.drop(col, axis=axis)
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
drop_col(col='continente_fundar', axis=1),
	drop_col(col='pais_desc', axis=1),
	rename_cols(map={'iso3': 'geocodigo', 'tasa_desempleo': 'valor'}),
	query(condition="sexo == 'Total'"),
	drop_col(col='sexo', axis=1)
)
#  PIPELINE_END


#  start()
#  RangeIndex: 21483 entries, 0 to 21482
#  Data columns (total 6 columns):
#   #   Column             Non-Null Count  Dtype  
#  ---  ------             --------------  -----  
#   0   iso3               21483 non-null  object 
#   1   anio               21483 non-null  int64  
#   2   sexo               21483 non-null  object 
#   3   tasa_desempleo     18504 non-null  float64
#   4   pais_desc          21483 non-null  object 
#   5   continente_fundar  21483 non-null  object 
#  
#  |    | iso3   |   anio | sexo   |   tasa_desempleo | pais_desc   | continente_fundar   |
#  |---:|:-------|-------:|:-------|-----------------:|:------------|:--------------------|
#  |  0 | AFG    |   2023 | Total  |          0.15378 | Afganistán  | Asia                |
#  
#  ------------------------------
#  
#  drop_col(col='continente_fundar', axis=1)
#  RangeIndex: 21483 entries, 0 to 21482
#  Data columns (total 5 columns):
#   #   Column          Non-Null Count  Dtype  
#  ---  ------          --------------  -----  
#   0   iso3            21483 non-null  object 
#   1   anio            21483 non-null  int64  
#   2   sexo            21483 non-null  object 
#   3   tasa_desempleo  18504 non-null  float64
#   4   pais_desc       21483 non-null  object 
#  
#  |    | iso3   |   anio | sexo   |   tasa_desempleo | pais_desc   |
#  |---:|:-------|-------:|:-------|-----------------:|:------------|
#  |  0 | AFG    |   2023 | Total  |          0.15378 | Afganistán  |
#  
#  ------------------------------
#  
#  drop_col(col='pais_desc', axis=1)
#  RangeIndex: 21483 entries, 0 to 21482
#  Data columns (total 4 columns):
#   #   Column          Non-Null Count  Dtype  
#  ---  ------          --------------  -----  
#   0   iso3            21483 non-null  object 
#   1   anio            21483 non-null  int64  
#   2   sexo            21483 non-null  object 
#   3   tasa_desempleo  18504 non-null  float64
#  
#  |    | iso3   |   anio | sexo   |   tasa_desempleo |
#  |---:|:-------|-------:|:-------|-----------------:|
#  |  0 | AFG    |   2023 | Total  |          0.15378 |
#  
#  ------------------------------
#  
#  rename_cols(map={'iso3': 'geocodigo', 'tasa_desempleo': 'valor'})
#  RangeIndex: 21483 entries, 0 to 21482
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  21483 non-null  object 
#   1   anio       21483 non-null  int64  
#   2   sexo       21483 non-null  object 
#   3   valor      18504 non-null  float64
#  
#  |    | geocodigo   |   anio | sexo   |   valor |
#  |---:|:------------|-------:|:-------|--------:|
#  |  0 | AFG         |   2023 | Total  | 0.15378 |
#  
#  ------------------------------
#  
#  query(condition="sexo == 'Total'")
#  Index: 7161 entries, 0 to 21480
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  7161 non-null   object 
#   1   anio       7161 non-null   int64  
#   2   sexo       7161 non-null   object 
#   3   valor      6168 non-null   float64
#  
#  |    | geocodigo   |   anio | sexo   |   valor |
#  |---:|:------------|-------:|:-------|--------:|
#  |  0 | AFG         |   2023 | Total  | 0.15378 |
#  
#  ------------------------------
#  
#  drop_col(col='sexo', axis=1)
#  Index: 7161 entries, 0 to 21480
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  7161 non-null   object 
#   1   anio       7161 non-null   int64  
#   2   valor      6168 non-null   float64
#  
#  |    | geocodigo   |   anio |   valor |
#  |---:|:------------|-------:|--------:|
#  |  0 | AFG         |   2023 | 0.15378 |
#  
#  ------------------------------
#  