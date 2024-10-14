from pandas import DataFrame

from loguru import logger


class SaveDataset:
    def __init__(self, dataframe: DataFrame) -> None:
        self.dataframe = dataframe

    def save_to_csv(self, filename: str) -> None:
        self.dataframe.to_csv(
            path_or_buf=filename,
            sep='\t',
            encoding='utf-8'
        )
        logger.info(f"Файл {filename} успешно сохранён...")


