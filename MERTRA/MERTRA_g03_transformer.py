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
def drop_na(df:DataFrame, col:str):
    df = df.dropna(subset=col, axis=0)
    return df

@transformer.convert
def sort_values(df: DataFrame, how: str, by: list):
    if how not in ['ascending', 'descending']:
        raise ValueError('how must be either "ascending" or "descending"')
    
    return df.sort_values(by=by, ascending=how=='ascending').reset_index(drop=True)

@transformer.convert
def multiplicar_por_escalar(df: DataFrame, col:str, k:float):
    df[col] = df[col]*k
    return df
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
drop_col(col='iso3_desc', axis=1),
	drop_col(col='nivel_agregacion', axis=1),
	rename_cols(map={'iso3': 'geocodigo', 'tasa_actividad': 'valor'}),
	query(condition='anio >= 1990'),
	drop_na(col='valor'),
	sort_values(how='ascending', by=['anio', 'geocodigo']),
	multiplicar_por_escalar(col='valor', k=100)
)
#  PIPELINE_END


#  start()
#  RangeIndex: 16704 entries, 0 to 16703
#  Data columns (total 5 columns):
#   #   Column            Non-Null Count  Dtype  
#  ---  ------            --------------  -----  
#   0   iso3              16704 non-null  object 
#   1   anio              16704 non-null  int64  
#   2   tasa_actividad    7620 non-null   float64
#   3   iso3_desc         16704 non-null  object 
#   4   nivel_agregacion  16704 non-null  object 
#  
#  |    | iso3   |   anio |   tasa_actividad | iso3_desc                    | nivel_agregacion   |
#  |---:|:-------|-------:|-----------------:|:-----------------------------|:-------------------|
#  |  0 | AFE    |   2023 |         0.412985 | África Oriental y Meridional | agregacion         |
#  
#  ------------------------------
#  
#  drop_col(col='iso3_desc', axis=1)
#  RangeIndex: 16704 entries, 0 to 16703
#  Data columns (total 4 columns):
#   #   Column            Non-Null Count  Dtype  
#  ---  ------            --------------  -----  
#   0   iso3              16704 non-null  object 
#   1   anio              16704 non-null  int64  
#   2   tasa_actividad    7620 non-null   float64
#   3   nivel_agregacion  16704 non-null  object 
#  
#  |    | iso3   |   anio |   tasa_actividad | nivel_agregacion   |
#  |---:|:-------|-------:|-----------------:|:-------------------|
#  |  0 | AFE    |   2023 |         0.412985 | agregacion         |
#  
#  ------------------------------
#  
#  drop_col(col='nivel_agregacion', axis=1)
#  RangeIndex: 16704 entries, 0 to 16703
#  Data columns (total 3 columns):
#   #   Column          Non-Null Count  Dtype  
#  ---  ------          --------------  -----  
#   0   iso3            16704 non-null  object 
#   1   anio            16704 non-null  int64  
#   2   tasa_actividad  7620 non-null   float64
#  
#  |    | iso3   |   anio |   tasa_actividad |
#  |---:|:-------|-------:|-----------------:|
#  |  0 | AFE    |   2023 |         0.412985 |
#  
#  ------------------------------
#  
#  rename_cols(map={'iso3': 'geocodigo', 'tasa_actividad': 'valor'})
#  RangeIndex: 16704 entries, 0 to 16703
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  16704 non-null  object 
#   1   anio       16704 non-null  int64  
#   2   valor      7620 non-null   float64
#  
#  |    | geocodigo   |   anio |    valor |
#  |---:|:------------|-------:|---------:|
#  |  0 | AFE         |   2023 | 0.412985 |
#  
#  ------------------------------
#  
#  query(condition='anio >= 1990')
#  Index: 8874 entries, 0 to 16673
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  8874 non-null   object 
#   1   anio       8874 non-null   int64  
#   2   valor      7620 non-null   float64
#  
#  |    | geocodigo   |   anio |    valor |
#  |---:|:------------|-------:|---------:|
#  |  0 | AFE         |   2023 | 0.412985 |
#  
#  ------------------------------
#  
#  drop_na(col='valor')
#  Index: 7620 entries, 0 to 16672
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  7620 non-null   object 
#   1   anio       7620 non-null   int64  
#   2   valor      7620 non-null   float64
#  
#  |    | geocodigo   |   anio |    valor |
#  |---:|:------------|-------:|---------:|
#  |  0 | AFE         |   2023 | 0.412985 |
#  
#  ------------------------------
#  
#  sort_values(how='ascending', by=['anio', 'geocodigo'])
#  RangeIndex: 7620 entries, 0 to 7619
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  7620 non-null   object 
#   1   anio       7620 non-null   int64  
#   2   valor      7620 non-null   float64
#  
#  |    | geocodigo   |   anio |   valor |
#  |---:|:------------|-------:|--------:|
#  |  0 | AFE         |   1991 | 38.9849 |
#  
#  ------------------------------
#  
#  multiplicar_por_escalar(col='valor', k=100)
#  RangeIndex: 7620 entries, 0 to 7619
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  7620 non-null   object 
#   1   anio       7620 non-null   int64  
#   2   valor      7620 non-null   float64
#  
#  |    | geocodigo   |   anio |   valor |
#  |---:|:------------|-------:|--------:|
#  |  0 | AFE         |   1991 | 38.9849 |
#  
#  ------------------------------
#  