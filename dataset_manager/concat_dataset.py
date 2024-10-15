import pandas as pd
from pandas import DataFrame

from typing import List

from loguru import logger


class ConcatDataset:
    def __init__(self, dataframes: List[DataFrame]) -> None:
        self.dataframes = dataframes

    def concat(self) -> DataFrame:
        dataframe = pd.concat(self.dataframes)
        logger.info("Датасеты объеденены успешно...")
        return dataframe
