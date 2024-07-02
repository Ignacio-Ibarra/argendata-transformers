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
def drop_na(df:DataFrame, col:str):
    df = df.dropna(subset=col, axis=0)
    return df

@transformer.convert
def sort_values(df: DataFrame, how: str, by: list):
    if how not in ['ascending', 'descending']:
        raise ValueError('how must be either "ascending" or "descending"')
    
    return df.sort_values(by=by, ascending=how=='ascending').reset_index(drop=True)
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
drop_col(col='iso3_desc', axis=1),
	drop_col(col='nivel_agregacion', axis=1),
	rename_cols(map={'iso3': 'geocodigo', 'ratio_tasa_actividad_mujer_varon': 'valor'}),
	drop_na(col='valor'),
	sort_values(how='descending', by=['anio'])
)
#  PIPELINE_END


#  start()
#  RangeIndex: 16704 entries, 0 to 16703
#  Data columns (total 5 columns):
#   #   Column                            Non-Null Count  Dtype  
#  ---  ------                            --------------  -----  
#   0   iso3                              16704 non-null  object 
#   1   iso3_desc                         16704 non-null  object 
#   2   anio                              16704 non-null  int64  
#   3   ratio_tasa_actividad_mujer_varon  4951 non-null   float64
#   4   nivel_agregacion                  16704 non-null  object 
#  
#  |    | iso3   | iso3_desc                   |   anio |   ratio_tasa_actividad_mujer_varon | nivel_agregacion   |
#  |---:|:-------|:----------------------------|-------:|-----------------------------------:|:-------------------|
#  |  0 | AFE    | Africa Eastern and Southern |   2023 |                                nan | agregacion         |
#  
#  ------------------------------
#  
#  drop_col(col='iso3_desc', axis=1)
#  RangeIndex: 16704 entries, 0 to 16703
#  Data columns (total 4 columns):
#   #   Column                            Non-Null Count  Dtype  
#  ---  ------                            --------------  -----  
#   0   iso3                              16704 non-null  object 
#   1   anio                              16704 non-null  int64  
#   2   ratio_tasa_actividad_mujer_varon  4951 non-null   float64
#   3   nivel_agregacion                  16704 non-null  object 
#  
#  |    | iso3   |   anio |   ratio_tasa_actividad_mujer_varon | nivel_agregacion   |
#  |---:|:-------|-------:|-----------------------------------:|:-------------------|
#  |  0 | AFE    |   2023 |                                nan | agregacion         |
#  
#  ------------------------------
#  
#  drop_col(col='nivel_agregacion', axis=1)
#  RangeIndex: 16704 entries, 0 to 16703
#  Data columns (total 3 columns):
#   #   Column                            Non-Null Count  Dtype  
#  ---  ------                            --------------  -----  
#   0   iso3                              16704 non-null  object 
#   1   anio                              16704 non-null  int64  
#   2   ratio_tasa_actividad_mujer_varon  4951 non-null   float64
#  
#  |    | iso3   |   anio |   ratio_tasa_actividad_mujer_varon |
#  |---:|:-------|-------:|-----------------------------------:|
#  |  0 | AFE    |   2023 |                                nan |
#  
#  ------------------------------
#  
#  rename_cols(map={'iso3': 'geocodigo', 'ratio_tasa_actividad_mujer_varon': 'valor'})
#  RangeIndex: 16704 entries, 0 to 16703
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  16704 non-null  object 
#   1   anio       16704 non-null  int64  
#   2   valor      4951 non-null   float64
#  
#  |    | geocodigo   |   anio |   valor |
#  |---:|:------------|-------:|--------:|
#  |  0 | AFE         |   2023 |     nan |
#  
#  ------------------------------
#  
#  drop_na(col='valor')
#  Index: 4951 entries, 135 to 16681
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  4951 non-null   object 
#   1   anio       4951 non-null   int64  
#   2   valor      4951 non-null   float64
#  
#  |     | geocodigo   |   anio |   valor |
#  |----:|:------------|-------:|--------:|
#  | 135 | ARB         |   2016 | 32.8257 |
#  
#  ------------------------------
#  
#  sort_values(how='descending', by=['anio'])
#  RangeIndex: 4951 entries, 0 to 4950
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   geocodigo  4951 non-null   object 
#   1   anio       4951 non-null   int64  
#   2   valor      4951 non-null   float64
#  
#  |    | geocodigo   |   anio |   valor |
#  |---:|:------------|-------:|--------:|
#  |  0 | PAN         |   2023 | 67.7872 |
#  
#  ------------------------------
#  