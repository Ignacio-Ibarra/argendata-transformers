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
def rename_cols(df: DataFrame, map):
    df = df.rename(columns=map)
    return df
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
rename_cols(map={'iso3': 'geocodigo'}),
	drop_col(col='countryname', axis=1),
	rename_cols(map={'exportunitvalueindex_200': 'valor'})
)
#  PIPELINE_END


#  start()
#  RangeIndex: 16960 entries, 0 to 16959
#  Data columns (total 4 columns):
#   #   Column                     Non-Null Count  Dtype  
#  ---  ------                     --------------  -----  
#   0   anio                       16960 non-null  int64  
#   1   iso3                       16960 non-null  object 
#   2   countryname                16960 non-null  object 
#   3   exportunitvalueindex_2000  6291 non-null   float64
#  
#  |    |   anio | iso3   | countryname   |   exportunitvalueindex_2000 |
#  |---:|-------:|:-------|:--------------|----------------------------:|
#  |  0 |   2023 | ABW    | Aruba         |                         nan |
#  
#  ------------------------------
#  
#  rename_cols(map={'iso3': 'geocodigo'})
#  RangeIndex: 16960 entries, 0 to 16959
#  Data columns (total 4 columns):
#   #   Column                     Non-Null Count  Dtype  
#  ---  ------                     --------------  -----  
#   0   anio                       16960 non-null  int64  
#   1   geocodigo                  16960 non-null  object 
#   2   countryname                16960 non-null  object 
#   3   exportunitvalueindex_2000  6291 non-null   float64
#  
#  |    |   anio | geocodigo   | countryname   |   exportunitvalueindex_2000 |
#  |---:|-------:|:------------|:--------------|----------------------------:|
#  |  0 |   2023 | ABW         | Aruba         |                         nan |
#  
#  ------------------------------
#  
#  drop_col(col='countryname', axis=1)
#  RangeIndex: 16960 entries, 0 to 16959
#  Data columns (total 3 columns):
#   #   Column                     Non-Null Count  Dtype  
#  ---  ------                     --------------  -----  
#   0   anio                       16960 non-null  int64  
#   1   geocodigo                  16960 non-null  object 
#   2   exportunitvalueindex_2000  6291 non-null   float64
#  
#  |    |   anio | geocodigo   |   exportunitvalueindex_2000 |
#  |---:|-------:|:------------|----------------------------:|
#  |  0 |   2023 | ABW         |                         nan |
#  
#  ------------------------------
#  
#  rename_cols(map={'exportunitvalueindex_200': 'valor'})
#  RangeIndex: 16960 entries, 0 to 16959
#  Data columns (total 3 columns):
#   #   Column                     Non-Null Count  Dtype  
#  ---  ------                     --------------  -----  
#   0   anio                       16960 non-null  int64  
#   1   geocodigo                  16960 non-null  object 
#   2   exportunitvalueindex_2000  6291 non-null   float64
#  
#  |    |   anio | geocodigo   |   exportunitvalueindex_2000 |
#  |---:|-------:|:------------|----------------------------:|
#  |  0 |   2023 | ABW         |                         nan |
#  
#  ------------------------------
#  