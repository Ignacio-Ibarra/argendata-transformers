from pandas import DataFrame
from data_transformers import chain, transformer


#  DEFINITIONS_START
@transformer.convert
def rename_cols(df: DataFrame, map):
    df = df.rename(columns=map)
    return df
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
rename_cols(map={'ano': 'anio', 'variable': 'indicador'})
)
#  PIPELINE_END


#  start()
#  RangeIndex: 64 entries, 0 to 63
#  Data columns (total 3 columns):
#   #   Column    Non-Null Count  Dtype  
#  ---  ------    --------------  -----  
#   0   ano       64 non-null     int64  
#   1   variable  64 non-null     object 
#   2   valor     64 non-null     float64
#  
#  |    |   ano | variable   |   valor |
#  |---:|------:|:-----------|--------:|
#  |  0 |  1992 | giniipcf   |   44.78 |
#  
#  ------------------------------
#  
#  rename_cols(map={'ano': 'anio', 'variable': 'indicador'})
#  RangeIndex: 64 entries, 0 to 63
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       64 non-null     int64  
#   1   indicador  64 non-null     object 
#   2   valor      64 non-null     float64
#  
#  |    |   anio | indicador   |   valor |
#  |---:|-------:|:------------|--------:|
#  |  0 |   1992 | giniipcf    |   44.78 |
#  
#  ------------------------------
#  