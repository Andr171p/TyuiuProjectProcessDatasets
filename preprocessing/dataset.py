from dataset_manager.load_dataset import LoadDataset
from dataset_manager.concat_dataset import ConcatDataset
from dataset_manager.save_dataset import SaveDataset
from preprocessing.columns import DatasetColumns

from pandas import DataFrame
from pandas.io.parsers import TextFileReader

from typing import List


class Dataset:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load(self) -> TextFileReader:
        loader = LoadDataset(file_path=self.file_path)
        chunk_dataframe = loader.load_big_csv_dataset()
        return chunk_dataframe

    @staticmethod
    def chunk_list(chunk_dataframe: TextFileReader) -> List[DataFrame]:
        dataframes: List[DataFrame] = []
        for chunk in chunk_dataframe:
            dataframes.append(chunk)
        return dataframes

    def columns(self) -> List[DataFrame]:
        chunk_dataframe = self.load()
        dataframes = self.chunk_list(chunk_dataframe=chunk_dataframe)
        dataset_columns = DatasetColumns(dataframes=dataframes)
        dataframes = dataset_columns.process()
        return dataframes

    @staticmethod
    def merge(dataframes: List[DataFrame]) -> DataFrame:
        concat_dataset = ConcatDataset(dataframes=dataframes)
        dataframe = concat_dataset.concat()
        return dataframe

    @staticmethod
    def save(dataframe: DataFrame, filename: str = 'Бак ТИУ 5 лет data.csv') -> None:
        save_dataset = SaveDataset(dataframe=dataframe)
        save_dataset.save_to_csv(filename=filename)


dataset = Dataset(
    file_path=r"/datasets\Бак ТИУ 5 лет raw.csv"
)
dfs = dataset.columns()
df = dataset.merge(dataframes=dfs)
dataset.save(dataframe=df)
