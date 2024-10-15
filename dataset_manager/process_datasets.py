from dataset_manager.load_dataset import LoadDataset
from dataset_manager.concat_dataset import ConcatDataset
from dataset_manager.save_dataset import SaveDataset

from files_config import data_files

from concurrent.futures import ThreadPoolExecutor
from typing import List

from pandas import DataFrame


class ProcessXLSXDatasets:
    files = data_files.applicant_bac_files

    @classmethod
    def load_dataset(cls, file_path: str) -> DataFrame:
        loader = LoadDataset(file_path=file_path)
        dataframe = loader.load_xlsx_dataset()
        return dataframe

    @classmethod
    def process_datasets(cls, output_filename: str = 'Бак ТИУ 5 лет raw.csv') -> DataFrame:
        dataframes: List[DataFrame] = []
        with ThreadPoolExecutor(max_workers=len(cls.files)) as executor:
            for file in executor.map(cls.load_dataset, cls.files):
                dataframes.append(file)
        dataframe = ConcatDataset(dataframes=dataframes).concat()
        SaveDataset(dataframe=dataframe).save_to_csv(filename=output_filename)
        return dataframe


process = ProcessXLSXDatasets
data = process.process_datasets()
print(data)