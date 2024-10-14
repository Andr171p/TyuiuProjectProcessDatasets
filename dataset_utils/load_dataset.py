import pandas as pd
from pandas import DataFrame

from misc.timer import run_timer

from loguru import logger


class LoadDataset:
    ENGINE = "openpyxl"

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def view_dataset(self) -> None:
        print(pd.read_excel(self.file_path))

    @staticmethod
    def get_columns_headers(dataframe: DataFrame) -> DataFrame:
        dataframe = dataframe.iloc[7:]
        dataframe.columns = dataframe.iloc[0]
        dataframe = dataframe[1:]
        return dataframe

    @run_timer
    def load_dataset(self, sheet_name: str = 'Абитуриенты') -> DataFrame:
        logger.info("Начало чтения файла...")
        dataframe = pd.read_excel(
            self.file_path,
            sheet_name=sheet_name,
            engine='openpyxl'
        )
        logger.info("Файл успешно прочитан...")
        dataframe = self.get_columns_headers(dataframe=dataframe)
        return dataframe


dataset = LoadDataset(file_path=r"/tyuiu_datasets/От Хохлова/Выгрузка/Бак 2019-2020.xlsx")
d = dataset.load_dataset()
print(d)