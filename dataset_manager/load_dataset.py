import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader

from misc.timer import run_timer
from misc.utils import get_columns_headers

from loguru import logger


class LoadDataset:
    ENGINE = ["openpyxl", "python", "c"]

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @run_timer
    def load_xlsx_dataset(self, sheet_name: str = 'Абитуриенты') -> DataFrame:
        logger.info("Начало чтения XLSX файла...")
        dataframe = pd.read_excel(
            self.file_path,
            sheet_name=sheet_name,
            engine="openpyxl"
        )
        logger.info("Файл успешно прочитан...")
        dataframe = get_columns_headers(dataframe=dataframe)
        return dataframe

    @run_timer
    def load_csv_dataset(self) -> DataFrame:
        logger.info("Начало чтения CSV файла...")
        dataframe = pd.read_csv(
            self.file_path,
            engine="python",
            encoding='utf-8',
            on_bad_lines='skip'
        )
        logger.info("Файл успешно прочитан...")
        return dataframe

    @run_timer
    def load_big_csv_dataset(self, chunk_size: int = 10_000) -> TextFileReader:
        logger.info("Начало чтения CSV файла...")
        chunks_dataframe = pd.read_csv(
            self.file_path,
            engine="python",
            chunksize=chunk_size,
            encoding='utf-8',
            on_bad_lines='skip'
        )
        logger.info("Файл успешно прочитан...")
        return chunks_dataframe

