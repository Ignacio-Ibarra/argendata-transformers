from pandas import DataFrame
from data_transformers import chain, transformer


#  DEFINITIONS_START
@transformer.convert
def query(df: DataFrame, condition: str):
    df = df.query(condition)    
    return df

@transformer.convert
def replace_value(df: DataFrame, col: str, curr_value: str, new_value: str):
    df = df.replace({col: curr_value}, new_value)
    return df

@transformer.convert
def replace_value(df: DataFrame, col: str, curr_value: str, new_value: str):
    df = df.replace({col: curr_value}, new_value)
    return df

@transformer.convert
def replace_value(df: DataFrame, col: str, curr_value: str, new_value: str):
    df = df.replace({col: curr_value}, new_value)
    return df

@transformer.convert
def replace_value(df: DataFrame, col: str, curr_value: str, new_value: str):
    df = df.replace({col: curr_value}, new_value)
    return df

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
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
query(condition='iso3 == "ARG" & anio == anio.max() & tipo_energia != "Total"'),
	replace_value(col='iso3', curr_value='OWID_WRL', new_value='WLD'),
	replace_value(col='fuente_energia', curr_value='Eolica', new_value='Eólica'),
	replace_value(col='fuente_energia', curr_value='Carbon', new_value='Carbón'),
	replace_value(col='fuente_energia', curr_value='Petroleo', new_value='Petróleo'),
	rename_cols(map={'fuente_energia': 'nivel2', 'porcentaje': 'valor', 'tipo_energia': 'nivel1'}),
	drop_col(col='anio', axis=1),
	drop_col(col='iso3', axis=1),
	drop_col(col='valor_en_twh', axis=1)
)
#  PIPELINE_END


#  start()
#  RangeIndex: 51852 entries, 0 to 51851
#  Data columns (total 6 columns):
#   #   Column          Non-Null Count  Dtype  
#  ---  ------          --------------  -----  
#   0   iso3            51852 non-null  object 
#   1   anio            51852 non-null  int64  
#   2   fuente_energia  51852 non-null  object 
#   3   tipo_energia    51852 non-null  object 
#   4   valor_en_twh    40880 non-null  float64
#   5   porcentaje      51852 non-null  float64
#  
#  |    | iso3   |   anio | fuente_energia   | tipo_energia   |   valor_en_twh |   porcentaje |
#  |---:|:-------|-------:|:-----------------|:---------------|---------------:|-------------:|
#  |  0 | AGO    |   1965 | Biocombustibles  | Limpias        |            nan |            0 |
#  
#  ------------------------------
#  
#  query(condition='iso3 == "ARG" & anio == anio.max() & tipo_energia != "Total"')
#  Index: 9 entries, 985 to 1443
#  Data columns (total 6 columns):
#   #   Column          Non-Null Count  Dtype  
#  ---  ------          --------------  -----  
#   0   iso3            9 non-null      object 
#   1   anio            9 non-null      int64  
#   2   fuente_energia  9 non-null      object 
#   3   tipo_energia    9 non-null      object 
#   4   valor_en_twh    9 non-null      float64
#   5   porcentaje      9 non-null      float64
#  
#  |     | iso3   |   anio | fuente_energia   | tipo_energia   |   valor_en_twh |   porcentaje |
#  |----:|:-------|-------:|:-----------------|:---------------|---------------:|-------------:|
#  | 985 | ARG    |   2022 | Biocombustibles  | Limpias        |        13.9313 |      1.39177 |
#  
#  ------------------------------
#  
#  replace_value(col='iso3', curr_value='OWID_WRL', new_value='WLD')
#  Index: 9 entries, 985 to 1443
#  Data columns (total 6 columns):
#   #   Column          Non-Null Count  Dtype  
#  ---  ------          --------------  -----  
#   0   iso3            9 non-null      object 
#   1   anio            9 non-null      int64  
#   2   fuente_energia  9 non-null      object 
#   3   tipo_energia    9 non-null      object 
#   4   valor_en_twh    9 non-null      float64
#   5   porcentaje      9 non-null      float64
#  
#  |     | iso3   |   anio | fuente_energia   | tipo_energia   |   valor_en_twh |   porcentaje |
#  |----:|:-------|-------:|:-----------------|:---------------|---------------:|-------------:|
#  | 985 | ARG    |   2022 | Biocombustibles  | Limpias        |        13.9313 |      1.39177 |
#  
#  ------------------------------
#  
#  replace_value(col='fuente_energia', curr_value='Eolica', new_value='Eólica')
#  Index: 9 entries, 985 to 1443
#  Data columns (total 6 columns):
#   #   Column          Non-Null Count  Dtype  
#  ---  ------          --------------  -----  
#   0   iso3            9 non-null      object 
#   1   anio            9 non-null      int64  
#   2   fuente_energia  9 non-null      object 
#   3   tipo_energia    9 non-null      object 
#   4   valor_en_twh    9 non-null      float64
#   5   porcentaje      9 non-null      float64
#  
#  |     | iso3   |   anio | fuente_energia   | tipo_energia   |   valor_en_twh |   porcentaje |
#  |----:|:-------|-------:|:-----------------|:---------------|---------------:|-------------:|
#  | 985 | ARG    |   2022 | Biocombustibles  | Limpias        |        13.9313 |      1.39177 |
#  
#  ------------------------------
#  
#  replace_value(col='fuente_energia', curr_value='Carbon', new_value='Carbón')
#  Index: 9 entries, 985 to 1443
#  Data columns (total 6 columns):
#   #   Column          Non-Null Count  Dtype  
#  ---  ------          --------------  -----  
#   0   iso3            9 non-null      object 
#   1   anio            9 non-null      int64  
#   2   fuente_energia  9 non-null      object 
#   3   tipo_energia    9 non-null      object 
#   4   valor_en_twh    9 non-null      float64
#   5   porcentaje      9 non-null      float64
#  
#  |     | iso3   |   anio | fuente_energia   | tipo_energia   |   valor_en_twh |   porcentaje |
#  |----:|:-------|-------:|:-----------------|:---------------|---------------:|-------------:|
#  | 985 | ARG    |   2022 | Biocombustibles  | Limpias        |        13.9313 |      1.39177 |
#  
#  ------------------------------
#  
#  replace_value(col='fuente_energia', curr_value='Petroleo', new_value='Petróleo')
#  Index: 9 entries, 985 to 1443
#  Data columns (total 6 columns):
#   #   Column          Non-Null Count  Dtype  
#  ---  ------          --------------  -----  
#   0   iso3            9 non-null      object 
#   1   anio            9 non-null      int64  
#   2   fuente_energia  9 non-null      object 
#   3   tipo_energia    9 non-null      object 
#   4   valor_en_twh    9 non-null      float64
#   5   porcentaje      9 non-null      float64
#  
#  |     | iso3   |   anio | fuente_energia   | tipo_energia   |   valor_en_twh |   porcentaje |
#  |----:|:-------|-------:|:-----------------|:---------------|---------------:|-------------:|
#  | 985 | ARG    |   2022 | Biocombustibles  | Limpias        |        13.9313 |      1.39177 |
#  
#  ------------------------------
#  
#  rename_cols(map={'fuente_energia': 'nivel2', 'porcentaje': 'valor', 'tipo_energia': 'nivel1'})
#  Index: 9 entries, 985 to 1443
#  Data columns (total 6 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   iso3          9 non-null      object 
#   1   anio          9 non-null      int64  
#   2   nivel2        9 non-null      object 
#   3   nivel1        9 non-null      object 
#   4   valor_en_twh  9 non-null      float64
#   5   valor         9 non-null      float64
#  
#  |     | iso3   |   anio | nivel2          | nivel1   |   valor_en_twh |   valor |
#  |----:|:-------|-------:|:----------------|:---------|---------------:|--------:|
#  | 985 | ARG    |   2022 | Biocombustibles | Limpias  |        13.9313 | 1.39177 |
#  
#  ------------------------------
#  
#  drop_col(col='anio', axis=1)
#  Index: 9 entries, 985 to 1443
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   iso3          9 non-null      object 
#   1   nivel2        9 non-null      object 
#   2   nivel1        9 non-null      object 
#   3   valor_en_twh  9 non-null      float64
#   4   valor         9 non-null      float64
#  
#  |     | iso3   | nivel2          | nivel1   |   valor_en_twh |   valor |
#  |----:|:-------|:----------------|:---------|---------------:|--------:|
#  | 985 | ARG    | Biocombustibles | Limpias  |        13.9313 | 1.39177 |
#  
#  ------------------------------
#  
#  drop_col(col='iso3', axis=1)
#  Index: 9 entries, 985 to 1443
#  Data columns (total 4 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   nivel2        9 non-null      object 
#   1   nivel1        9 non-null      object 
#   2   valor_en_twh  9 non-null      float64
#   3   valor         9 non-null      float64
#  
#  |     | nivel2          | nivel1   |   valor_en_twh |   valor |
#  |----:|:----------------|:---------|---------------:|--------:|
#  | 985 | Biocombustibles | Limpias  |        13.9313 | 1.39177 |
#  
#  ------------------------------
#  
#  drop_col(col='valor_en_twh', axis=1)
#  Index: 9 entries, 985 to 1443
#  Data columns (total 3 columns):
#   #   Column  Non-Null Count  Dtype  
#  ---  ------  --------------  -----  
#   0   nivel2  9 non-null      object 
#   1   nivel1  9 non-null      object 
#   2   valor   9 non-null      float64
#  
#  |     | nivel2          | nivel1   |   valor |
#  |----:|:----------------|:---------|--------:|
#  | 985 | Biocombustibles | Limpias  | 1.39177 |
#  
#  ------------------------------
#  