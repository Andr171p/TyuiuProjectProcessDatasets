from pandas import DataFrame


def get_columns_headers(dataframe: DataFrame) -> DataFrame:
    dataframe = dataframe.iloc[7:]
    dataframe.columns = dataframe.iloc[0]
    dataframe = dataframe[1:]
    return dataframe
