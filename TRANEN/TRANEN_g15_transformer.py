from pandas import DataFrame
from data_transformers import chain, transformer


#  DEFINITIONS_START
@transformer.convert
def replace_value(df: DataFrame, col: str, curr_value: str, new_value: str):
    df = df.replace({col: curr_value}, new_value)
    return df

@transformer.convert
def rename_cols(df: DataFrame, map):
    df = df.rename(columns=map)
    return df

@transformer.convert
def query(df: DataFrame, condition: str):
    df = df.query(condition)    
    return df

@transformer.convert
def wide_to_long(df: DataFrame, primary_keys, value_name='valor', var_name='indicador'):
    return df.melt(id_vars=primary_keys, value_name=value_name, var_name=var_name)

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
def drop_col(df: DataFrame, col, axis=1):
    return df.drop(col, axis=axis)

@transformer.convert
def drop_na(df:DataFrame, cols:list):
    return df.dropna(subset=cols)

@transformer.convert
def sort_values(df: DataFrame, how: str, by: list):
    if how not in ['ascending', 'descending']:
        raise ValueError('how must be either "ascending" or "descending"')
    return df.sort_values(by=by, ascending=how == 'ascending')
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
replace_value(col='iso3', curr_value='OWID_WRL', new_value='WLD'),
	rename_cols(map={'tipo_energia': 'categoria', 'valor_en_mw': 'valor', 'iso3': 'geocodigo'}),
	query(condition='geocodigo == "WLD"'),
	wide_to_long(primary_keys=['anio', 'geocodigo'], value_name='valor', var_name='categoria'),
	replace_value(col='categoria', curr_value='emision_anual_co2_ton', new_value='Emisiones anuales de CO2'),
	replace_value(col='categoria', curr_value='energia_por_unidad_pib_kwh', new_value='Intensidad energética (por unidad de PIB medido en dólares de 2011 PPA)'),
	replace_value(col='categoria', curr_value='pib_per_cap_usd_ppa_2011', new_value='PIB per cápita en dólares PPA 2011'),
	replace_value(col='categoria', curr_value='poblacion', new_value='Población'),
	replace_value(col='categoria', curr_value='emision_anual_kgco2_por_kwh', new_value='Intensidad de carbono (CO2/kWh)'),
	drop_col(col='geocodigo', axis=1),
	drop_na(cols=['valor']),
	sort_values(how='ascending', by=['anio', 'categoria'])
)
#  PIPELINE_END


#  start()
#  RangeIndex: 201096 entries, 0 to 201095
#  Data columns (total 7 columns):
#   #   Column                       Non-Null Count   Dtype  
#  ---  ------                       --------------   -----  
#   0   anio                         201096 non-null  int64  
#   1   iso3                         201096 non-null  object 
#   2   emision_anual_co2_ton        24157 non-null   float64
#   3   energia_por_unidad_pib_kwh   7789 non-null    float64
#   4   pib_per_cap_usd_ppa_2011     21314 non-null   float64
#   5   poblacion                    54971 non-null   float64
#   6   emision_anual_kgco2_por_kwh  9328 non-null    float64
#  
#  |    |   anio | iso3   |   emision_anual_co2_ton |   energia_por_unidad_pib_kwh |   pib_per_cap_usd_ppa_2011 |   poblacion |   emision_anual_kgco2_por_kwh |
#  |---:|-------:|:-------|------------------------:|-----------------------------:|---------------------------:|------------:|------------------------------:|
#  |  0 |   1750 | GBR    |             9.30594e+06 |                          nan |                       2702 | 9.28817e+06 |                           nan |
#  
#  ------------------------------
#  
#  replace_value(col='iso3', curr_value='OWID_WRL', new_value='WLD')
#  RangeIndex: 201096 entries, 0 to 201095
#  Data columns (total 7 columns):
#   #   Column                       Non-Null Count   Dtype  
#  ---  ------                       --------------   -----  
#   0   anio                         201096 non-null  int64  
#   1   iso3                         201096 non-null  object 
#   2   emision_anual_co2_ton        24157 non-null   float64
#   3   energia_por_unidad_pib_kwh   7789 non-null    float64
#   4   pib_per_cap_usd_ppa_2011     21314 non-null   float64
#   5   poblacion                    54971 non-null   float64
#   6   emision_anual_kgco2_por_kwh  9328 non-null    float64
#  
#  |    |   anio | iso3   |   emision_anual_co2_ton |   energia_por_unidad_pib_kwh |   pib_per_cap_usd_ppa_2011 |   poblacion |   emision_anual_kgco2_por_kwh |
#  |---:|-------:|:-------|------------------------:|-----------------------------:|---------------------------:|------------:|------------------------------:|
#  |  0 |   1750 | GBR    |             9.30594e+06 |                          nan |                       2702 | 9.28817e+06 |                           nan |
#  
#  ------------------------------
#  
#  rename_cols(map={'tipo_energia': 'categoria', 'valor_en_mw': 'valor', 'iso3': 'geocodigo'})
#  RangeIndex: 201096 entries, 0 to 201095
#  Data columns (total 7 columns):
#   #   Column                       Non-Null Count   Dtype  
#  ---  ------                       --------------   -----  
#   0   anio                         201096 non-null  int64  
#   1   geocodigo                    201096 non-null  object 
#   2   emision_anual_co2_ton        24157 non-null   float64
#   3   energia_por_unidad_pib_kwh   7789 non-null    float64
#   4   pib_per_cap_usd_ppa_2011     21314 non-null   float64
#   5   poblacion                    54971 non-null   float64
#   6   emision_anual_kgco2_por_kwh  9328 non-null    float64
#  
#  |    |   anio | geocodigo   |   emision_anual_co2_ton |   energia_por_unidad_pib_kwh |   pib_per_cap_usd_ppa_2011 |   poblacion |   emision_anual_kgco2_por_kwh |
#  |---:|-------:|:------------|------------------------:|-----------------------------:|---------------------------:|------------:|------------------------------:|
#  |  0 |   1750 | GBR         |             9.30594e+06 |                          nan |                       2702 | 9.28817e+06 |                           nan |
#  
#  ------------------------------
#  
#  query(condition='geocodigo == "WLD"')
#  Index: 798 entries, 11172 to 11969
#  Data columns (total 7 columns):
#   #   Column                       Non-Null Count  Dtype  
#  ---  ------                       --------------  -----  
#   0   anio                         798 non-null    int64  
#   1   geocodigo                    798 non-null    object 
#   2   emision_anual_co2_ton        273 non-null    float64
#   3   energia_por_unidad_pib_kwh   13 non-null     float64
#   4   pib_per_cap_usd_ppa_2011     21 non-null     float64
#   5   poblacion                    259 non-null    float64
#   6   emision_anual_kgco2_por_kwh  58 non-null     float64
#  
#  |       |   anio | geocodigo   |   emision_anual_co2_ton |   energia_por_unidad_pib_kwh |   pib_per_cap_usd_ppa_2011 |   poblacion |   emision_anual_kgco2_por_kwh |
#  |------:|-------:|:------------|------------------------:|-----------------------------:|---------------------------:|------------:|------------------------------:|
#  | 11172 |   1750 | WLD         |             9.30594e+06 |                          nan |                        nan | 7.45664e+08 |                           nan |
#  
#  ------------------------------
#  
#  wide_to_long(primary_keys=['anio', 'geocodigo'], value_name='valor', var_name='categoria')
#  RangeIndex: 3990 entries, 0 to 3989
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       3990 non-null   int64  
#   1   geocodigo  3990 non-null   object 
#   2   categoria  3990 non-null   object 
#   3   valor      624 non-null    float64
#  
#  |    |   anio | geocodigo   | categoria             |       valor |
#  |---:|-------:|:------------|:----------------------|------------:|
#  |  0 |   1750 | WLD         | emision_anual_co2_ton | 9.30594e+06 |
#  
#  ------------------------------
#  
#  replace_value(col='categoria', curr_value='emision_anual_co2_ton', new_value='Emisiones anuales de CO2')
#  RangeIndex: 3990 entries, 0 to 3989
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       3990 non-null   int64  
#   1   geocodigo  3990 non-null   object 
#   2   categoria  3990 non-null   object 
#   3   valor      624 non-null    float64
#  
#  |    |   anio | geocodigo   | categoria                |       valor |
#  |---:|-------:|:------------|:-------------------------|------------:|
#  |  0 |   1750 | WLD         | Emisiones anuales de CO2 | 9.30594e+06 |
#  
#  ------------------------------
#  
#  replace_value(col='categoria', curr_value='energia_por_unidad_pib_kwh', new_value='Intensidad energética (por unidad de PIB medido en dólares de 2011 PPA)')
#  RangeIndex: 3990 entries, 0 to 3989
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       3990 non-null   int64  
#   1   geocodigo  3990 non-null   object 
#   2   categoria  3990 non-null   object 
#   3   valor      624 non-null    float64
#  
#  |    |   anio | geocodigo   | categoria                |       valor |
#  |---:|-------:|:------------|:-------------------------|------------:|
#  |  0 |   1750 | WLD         | Emisiones anuales de CO2 | 9.30594e+06 |
#  
#  ------------------------------
#  
#  replace_value(col='categoria', curr_value='pib_per_cap_usd_ppa_2011', new_value='PIB per cápita en dólares PPA 2011')
#  RangeIndex: 3990 entries, 0 to 3989
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       3990 non-null   int64  
#   1   geocodigo  3990 non-null   object 
#   2   categoria  3990 non-null   object 
#   3   valor      624 non-null    float64
#  
#  |    |   anio | geocodigo   | categoria                |       valor |
#  |---:|-------:|:------------|:-------------------------|------------:|
#  |  0 |   1750 | WLD         | Emisiones anuales de CO2 | 9.30594e+06 |
#  
#  ------------------------------
#  
#  replace_value(col='categoria', curr_value='poblacion', new_value='Población')
#  RangeIndex: 3990 entries, 0 to 3989
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       3990 non-null   int64  
#   1   geocodigo  3990 non-null   object 
#   2   categoria  3990 non-null   object 
#   3   valor      624 non-null    float64
#  
#  |    |   anio | geocodigo   | categoria                |       valor |
#  |---:|-------:|:------------|:-------------------------|------------:|
#  |  0 |   1750 | WLD         | Emisiones anuales de CO2 | 9.30594e+06 |
#  
#  ------------------------------
#  
#  replace_value(col='categoria', curr_value='emision_anual_kgco2_por_kwh', new_value='Intensidad de carbono (CO2/kWh)')
#  RangeIndex: 3990 entries, 0 to 3989
#  Data columns (total 4 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       3990 non-null   int64  
#   1   geocodigo  3990 non-null   object 
#   2   categoria  3990 non-null   object 
#   3   valor      624 non-null    float64
#  
#  |    |   anio | geocodigo   | categoria                |       valor |
#  |---:|-------:|:------------|:-------------------------|------------:|
#  |  0 |   1750 | WLD         | Emisiones anuales de CO2 | 9.30594e+06 |
#  
#  ------------------------------
#  
#  drop_col(col='geocodigo', axis=1)
#  RangeIndex: 3990 entries, 0 to 3989
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       3990 non-null   int64  
#   1   categoria  3990 non-null   object 
#   2   valor      624 non-null    float64
#  
#  |    |   anio | categoria                |       valor |
#  |---:|-------:|:-------------------------|------------:|
#  |  0 |   1750 | Emisiones anuales de CO2 | 9.30594e+06 |
#  
#  ------------------------------
#  
#  drop_na(cols=['valor'])
#  Index: 624 entries, 0 to 3464
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       624 non-null    int64  
#   1   categoria  624 non-null    object 
#   2   valor      624 non-null    float64
#  
#  |    |   anio | categoria                |       valor |
#  |---:|-------:|:-------------------------|------------:|
#  |  0 |   1750 | Emisiones anuales de CO2 | 9.30594e+06 |
#  
#  ------------------------------
#  
#  sort_values(how='ascending', by=['anio', 'categoria'])
#  Index: 624 entries, 3170 to 1868
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       624 non-null    int64  
#   1   categoria  624 non-null    object 
#   2   valor      624 non-null    float64
#  
#  |      |   anio | categoria   |       valor |
#  |-----:|-------:|:------------|------------:|
#  | 3170 | -10000 | Población   | 4.43227e+06 |
#  
#  ------------------------------
#  