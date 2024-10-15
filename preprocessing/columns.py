from pandas import DataFrame
from typing import List
from loguru import logger
from concurrent.futures import ThreadPoolExecutor


class DatasetColumns:
    from preprocessing.config import COLUMNS
    columns = COLUMNS

    def __init__(self, dataframes: List[DataFrame]) -> None:
        self.dataframes = dataframes

    def pick_out_columns(self, dataframe: DataFrame) -> DataFrame:
        dataframe = dataframe[self.columns]
        return dataframe

    def process(self) -> List[DataFrame]:
        dataframes: List[DataFrame] = []
        with ThreadPoolExecutor(max_workers=len(self.dataframes)) as executor:
            for dataframe in executor.map(self.pick_out_columns, self.dataframes):
                logger.info(dataframe.shape)
                dataframes.append(dataframe)
                logger.info("Столбцы выделены успешно...")
        return dataframes
