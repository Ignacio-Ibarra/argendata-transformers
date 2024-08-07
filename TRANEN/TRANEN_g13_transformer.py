from pandas import DataFrame
from data_transformers import chain, transformer


#  DEFINITIONS_START
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
def replace_value(df: DataFrame, col: str, curr_value: str, new_value: str):
    df = df.replace({col: curr_value}, new_value)
    return df

@transformer.convert
def query(df: DataFrame, condition: str):
    df = df.query(condition)    
    return df

@transformer.convert
def drop_na(df:DataFrame, cols:list):
    return df.dropna(subset=cols)

@transformer.convert
def drop_col(df: DataFrame, col, axis=1):
    return df.drop(col, axis=axis)

@transformer.convert
def sort_values_by_comparison(df, colname: str, precedence: dict, prefix=[], suffix=[]):
    mapcol = colname+'_map'
    df_ = df.copy()
    df_[mapcol] = df_[colname].map(precedence)
    df_ = df_.sort_values(by=[*prefix, mapcol, *suffix])
    return df_.drop(mapcol, axis=1)
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
replace_value(col='iso3', curr_value='OWID_KOS', new_value='XKX'),
	replace_value(col='iso3', curr_value='OWID_WRL', new_value='WLD'),
	rename_cols(map={'tipo_energia': 'indicador', 'porcentaje': 'valor', 'iso3': 'geocodigo'}),
	replace_value(col='indicador', curr_value='Bioenergia', new_value='Bioenergía'),
	replace_value(col='indicador', curr_value='Bioenergia', new_value='Bioenergía'),
	replace_value(col='indicador', curr_value='Carbon', new_value='Carbón'),
	replace_value(col='indicador', curr_value='Petroleo', new_value='Petróleo'),
	replace_value(col='indicador', curr_value='Eolica', new_value='Eólica'),
	query(condition='indicador != "Total"'),
	drop_na(cols=['valor']),
	drop_col(col=['valor_en_twh'], axis=1),
	sort_values_by_comparison(colname='indicador', precedence={'Bioenergía': 10, 'Otras renovables': 1, 'Biocombustibles': 2, 'Solar': 3, 'Eólica': 4, 'Nuclear': 5, 'Hidro': 6, 'Gas natural': 7, 'Petróleo': 8, 'Carbón': 9}, prefix=['anio', 'geocodigo'], suffix=[])
)
#  PIPELINE_END


#  start()
#  RangeIndex: 81900 entries, 0 to 81899
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          81900 non-null  int64  
#   1   iso3          81900 non-null  object 
#   2   tipo_energia  81900 non-null  object 
#   3   valor_en_twh  57843 non-null  float64
#   4   porcentaje    81900 non-null  float64
#  
#  |    |   anio | iso3   | tipo_energia     |   valor_en_twh |   porcentaje |
#  |---:|-------:|:-------|:-----------------|---------------:|-------------:|
#  |  0 |   1985 | GBR    | Otras renovables |              0 |            0 |
#  
#  ------------------------------
#  
#  replace_value(col='iso3', curr_value='OWID_KOS', new_value='XKX')
#  RangeIndex: 81900 entries, 0 to 81899
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          81900 non-null  int64  
#   1   iso3          81900 non-null  object 
#   2   tipo_energia  81900 non-null  object 
#   3   valor_en_twh  57843 non-null  float64
#   4   porcentaje    81900 non-null  float64
#  
#  |    |   anio | iso3   | tipo_energia     |   valor_en_twh |   porcentaje |
#  |---:|-------:|:-------|:-----------------|---------------:|-------------:|
#  |  0 |   1985 | GBR    | Otras renovables |              0 |            0 |
#  
#  ------------------------------
#  
#  replace_value(col='iso3', curr_value='OWID_WRL', new_value='WLD')
#  RangeIndex: 81900 entries, 0 to 81899
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          81900 non-null  int64  
#   1   iso3          81900 non-null  object 
#   2   tipo_energia  81900 non-null  object 
#   3   valor_en_twh  57843 non-null  float64
#   4   porcentaje    81900 non-null  float64
#  
#  |    |   anio | iso3   | tipo_energia     |   valor_en_twh |   porcentaje |
#  |---:|-------:|:-------|:-----------------|---------------:|-------------:|
#  |  0 |   1985 | GBR    | Otras renovables |              0 |            0 |
#  
#  ------------------------------
#  
#  rename_cols(map={'tipo_energia': 'indicador', 'porcentaje': 'valor', 'iso3': 'geocodigo'})
#  RangeIndex: 81900 entries, 0 to 81899
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          81900 non-null  int64  
#   1   geocodigo     81900 non-null  object 
#   2   indicador     81900 non-null  object 
#   3   valor_en_twh  57843 non-null  float64
#   4   valor         81900 non-null  float64
#  
#  |    |   anio | geocodigo   | indicador        |   valor_en_twh |   valor |
#  |---:|-------:|:------------|:-----------------|---------------:|--------:|
#  |  0 |   1985 | GBR         | Otras renovables |              0 |       0 |
#  
#  ------------------------------
#  
#  replace_value(col='indicador', curr_value='Bioenergia', new_value='Bioenergía')
#  RangeIndex: 81900 entries, 0 to 81899
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          81900 non-null  int64  
#   1   geocodigo     81900 non-null  object 
#   2   indicador     81900 non-null  object 
#   3   valor_en_twh  57843 non-null  float64
#   4   valor         81900 non-null  float64
#  
#  |    |   anio | geocodigo   | indicador        |   valor_en_twh |   valor |
#  |---:|-------:|:------------|:-----------------|---------------:|--------:|
#  |  0 |   1985 | GBR         | Otras renovables |              0 |       0 |
#  
#  ------------------------------
#  
#  replace_value(col='indicador', curr_value='Bioenergia', new_value='Bioenergía')
#  RangeIndex: 81900 entries, 0 to 81899
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          81900 non-null  int64  
#   1   geocodigo     81900 non-null  object 
#   2   indicador     81900 non-null  object 
#   3   valor_en_twh  57843 non-null  float64
#   4   valor         81900 non-null  float64
#  
#  |    |   anio | geocodigo   | indicador        |   valor_en_twh |   valor |
#  |---:|-------:|:------------|:-----------------|---------------:|--------:|
#  |  0 |   1985 | GBR         | Otras renovables |              0 |       0 |
#  
#  ------------------------------
#  
#  replace_value(col='indicador', curr_value='Carbon', new_value='Carbón')
#  RangeIndex: 81900 entries, 0 to 81899
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          81900 non-null  int64  
#   1   geocodigo     81900 non-null  object 
#   2   indicador     81900 non-null  object 
#   3   valor_en_twh  57843 non-null  float64
#   4   valor         81900 non-null  float64
#  
#  |    |   anio | geocodigo   | indicador        |   valor_en_twh |   valor |
#  |---:|-------:|:------------|:-----------------|---------------:|--------:|
#  |  0 |   1985 | GBR         | Otras renovables |              0 |       0 |
#  
#  ------------------------------
#  
#  replace_value(col='indicador', curr_value='Petroleo', new_value='Petróleo')
#  RangeIndex: 81900 entries, 0 to 81899
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          81900 non-null  int64  
#   1   geocodigo     81900 non-null  object 
#   2   indicador     81900 non-null  object 
#   3   valor_en_twh  57843 non-null  float64
#   4   valor         81900 non-null  float64
#  
#  |    |   anio | geocodigo   | indicador        |   valor_en_twh |   valor |
#  |---:|-------:|:------------|:-----------------|---------------:|--------:|
#  |  0 |   1985 | GBR         | Otras renovables |              0 |       0 |
#  
#  ------------------------------
#  
#  replace_value(col='indicador', curr_value='Eolica', new_value='Eólica')
#  RangeIndex: 81900 entries, 0 to 81899
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          81900 non-null  int64  
#   1   geocodigo     81900 non-null  object 
#   2   indicador     81900 non-null  object 
#   3   valor_en_twh  57843 non-null  float64
#   4   valor         81900 non-null  float64
#  
#  |    |   anio | geocodigo   | indicador        |   valor_en_twh |   valor |
#  |---:|-------:|:------------|:-----------------|---------------:|--------:|
#  |  0 |   1985 | GBR         | Otras renovables |              0 |       0 |
#  
#  ------------------------------
#  
#  query(condition='indicador != "Total"')
#  Index: 73710 entries, 0 to 73709
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          73710 non-null  int64  
#   1   geocodigo     73710 non-null  object 
#   2   indicador     73710 non-null  object 
#   3   valor_en_twh  49653 non-null  float64
#   4   valor         73710 non-null  float64
#  
#  |    |   anio | geocodigo   | indicador        |   valor_en_twh |   valor |
#  |---:|-------:|:------------|:-----------------|---------------:|--------:|
#  |  0 |   1985 | GBR         | Otras renovables |              0 |       0 |
#  
#  ------------------------------
#  
#  drop_na(cols=['valor'])
#  Index: 73710 entries, 0 to 73709
#  Data columns (total 5 columns):
#   #   Column        Non-Null Count  Dtype  
#  ---  ------        --------------  -----  
#   0   anio          73710 non-null  int64  
#   1   geocodigo     73710 non-null  object 
#   2   indicador     73710 non-null  object 
#   3   valor_en_twh  49653 non-null  float64
#   4   valor         73710 non-null  float64
#  
#  |    |   anio | geocodigo   | indicador        |   valor_en_twh |   valor |
#  |---:|-------:|:------------|:-----------------|---------------:|--------:|
#  |  0 |   1985 | GBR         | Otras renovables |              0 |       0 |
#  
#  ------------------------------
#  
#  drop_col(col=['valor_en_twh'], axis=1)
#  Index: 73710 entries, 0 to 73709
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       73710 non-null  int64  
#   1   geocodigo  73710 non-null  object 
#   2   indicador  73710 non-null  object 
#   3   valor      73710 non-null  float64
#  
#  |    |   anio | geocodigo   | indicador        |   valor |
#  |---:|-------:|:------------|:-----------------|--------:|
#  |  0 |   1985 | GBR         | Otras renovables |       0 |
#  
#  ------------------------------
#  
#  sort_values_by_comparison(colname='indicador', precedence={'Bioenergía': 10, 'Otras renovables': 1, 'Biocombustibles': 2, 'Solar': 3, 'Eólica': 4, 'Nuclear': 5, 'Hidro': 6, 'Gas natural': 7, 'Petróleo': 8, 'Carbón': 9}, prefix=['anio', 'geocodigo'], suffix=[])
#  Index: 73710 entries, 6942 to 11855
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       73710 non-null  int64  
#   1   geocodigo  73710 non-null  object 
#   2   indicador  73710 non-null  object 
#   3   valor      73710 non-null  float64
#  
#  |      |   anio | geocodigo   | indicador        |   valor |
#  |-----:|-------:|:------------|:-----------------|--------:|
#  | 6942 |   1985 | ABW         | Otras renovables |       0 |
#  
#  ------------------------------
#  