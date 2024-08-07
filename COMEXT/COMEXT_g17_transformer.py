from pandas import DataFrame
from data_transformers import chain, transformer


#  DEFINITIONS_START
@transformer.convert
def query(df: DataFrame, condition: str):
    df = df.query(condition)    
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
def rename_cols(df: DataFrame, map):
    df = df.rename(columns=map)
    return df

@transformer.convert
def sort_values(df: DataFrame, how: str, by: list):
    if how not in ['ascending', 'descending']:
        raise ValueError('how must be either "ascending" or "descending"')
    
    return df.sort_values(by=by, ascending=how=='ascending').reset_index(drop=True)
#  DEFINITIONS_END


#  PIPELINE_START
pipeline = chain(
query(condition='iso3 == "ARG"'),
	drop_col(col='iso3', axis=1),
	drop_col(col='location_name_short_en', axis=1),
	drop_col(col='partner_region_id', axis=1),
	rename_cols(map={'year': 'anio', 'partner_region_name_short_es': 'indicador', 'import_value_pc': 'valor'}),
	sort_values(how='ascending', by=['anio'])
)
#  PIPELINE_END


#  start()
#  RangeIndex: 75560 entries, 0 to 75559
#  Data columns (total 6 columns):
#   #   Column                        Non-Null Count  Dtype  
#  ---  ------                        --------------  -----  
#   0   year                          75560 non-null  int64  
#   1   iso3                          75560 non-null  object 
#   2   location_name_short_en        75560 non-null  object 
#   3   partner_region_id             75560 non-null  int64  
#   4   partner_region_name_short_es  75560 non-null  object 
#   5   import_value_pc               75539 non-null  float64
#  
#  |    |   year | iso3   | location_name_short_en   |   partner_region_id | partner_region_name_short_es   |   import_value_pc |
#  |---:|-------:|:-------|:-------------------------|--------------------:|:-------------------------------|------------------:|
#  |  0 |   2005 | ABW    | Aruba                    |                 356 | Asia                           |           1.30083 |
#  
#  ------------------------------
#  
#  query(condition='iso3 == "ARG"')
#  Index: 415 entries, 8 to 75090
#  Data columns (total 6 columns):
#   #   Column                        Non-Null Count  Dtype  
#  ---  ------                        --------------  -----  
#   0   year                          415 non-null    int64  
#   1   iso3                          415 non-null    object 
#   2   location_name_short_en        415 non-null    object 
#   3   partner_region_id             415 non-null    int64  
#   4   partner_region_name_short_es  415 non-null    object 
#   5   import_value_pc               415 non-null    float64
#  
#  |    |   year | iso3   | location_name_short_en   |   partner_region_id | partner_region_name_short_es   |   import_value_pc |
#  |---:|-------:|:-------|:-------------------------|--------------------:|:-------------------------------|------------------:|
#  |  8 |   2009 | ARG    | Argentina                |                 357 | Otros                          |           4.50635 |
#  
#  ------------------------------
#  
#  drop_col(col='iso3', axis=1)
#  Index: 415 entries, 8 to 75090
#  Data columns (total 5 columns):
#   #   Column                        Non-Null Count  Dtype  
#  ---  ------                        --------------  -----  
#   0   year                          415 non-null    int64  
#   1   location_name_short_en        415 non-null    object 
#   2   partner_region_id             415 non-null    int64  
#   3   partner_region_name_short_es  415 non-null    object 
#   4   import_value_pc               415 non-null    float64
#  
#  |    |   year | location_name_short_en   |   partner_region_id | partner_region_name_short_es   |   import_value_pc |
#  |---:|-------:|:-------------------------|--------------------:|:-------------------------------|------------------:|
#  |  8 |   2009 | Argentina                |                 357 | Otros                          |           4.50635 |
#  
#  ------------------------------
#  
#  drop_col(col='location_name_short_en', axis=1)
#  Index: 415 entries, 8 to 75090
#  Data columns (total 4 columns):
#   #   Column                        Non-Null Count  Dtype  
#  ---  ------                        --------------  -----  
#   0   year                          415 non-null    int64  
#   1   partner_region_id             415 non-null    int64  
#   2   partner_region_name_short_es  415 non-null    object 
#   3   import_value_pc               415 non-null    float64
#  
#  |    |   year |   partner_region_id | partner_region_name_short_es   |   import_value_pc |
#  |---:|-------:|--------------------:|:-------------------------------|------------------:|
#  |  8 |   2009 |                 357 | Otros                          |           4.50635 |
#  
#  ------------------------------
#  
#  drop_col(col='partner_region_id', axis=1)
#  Index: 415 entries, 8 to 75090
#  Data columns (total 3 columns):
#   #   Column                        Non-Null Count  Dtype  
#  ---  ------                        --------------  -----  
#   0   year                          415 non-null    int64  
#   1   partner_region_name_short_es  415 non-null    object 
#   2   import_value_pc               415 non-null    float64
#  
#  |    |   year | partner_region_name_short_es   |   import_value_pc |
#  |---:|-------:|:-------------------------------|------------------:|
#  |  8 |   2009 | Otros                          |           4.50635 |
#  
#  ------------------------------
#  
#  rename_cols(map={'year': 'anio', 'partner_region_name_short_es': 'indicador', 'import_value_pc': 'valor'})
#  Index: 415 entries, 8 to 75090
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       415 non-null    int64  
#   1   indicador  415 non-null    object 
#   2   valor      415 non-null    float64
#  
#  |    |   anio | indicador   |   valor |
#  |---:|-------:|:------------|--------:|
#  |  8 |   2009 | Otros       | 4.50635 |
#  
#  ------------------------------
#  
#  sort_values(how='ascending', by=['anio'])
#  RangeIndex: 415 entries, 0 to 414
#  Data columns (total 3 columns):
#   #   Column     Non-Null Count  Dtype  
#  ---  ------     --------------  -----  
#   0   anio       415 non-null    int64  
#   1   indicador  415 non-null    object 
#   2   valor      415 non-null    float64
#  
#  |    |   anio | indicador   |   valor |
#  |---:|-------:|:------------|--------:|
#  |  0 |   1962 | Asia        | 7.87201 |
#  
#  ------------------------------
#  