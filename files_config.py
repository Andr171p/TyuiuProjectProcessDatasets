import os
from pathlib import Path
from typing import List

from loguru import logger


class RootPath:
    ROOT_PATH = Path(__file__).resolve().parents[0]


class DatasetsFiles:
    DIRECTORY_BAC_PATH = fr"{RootPath.ROOT_PATH}\ТИУ\От Хохлова\Выгрузка\Бакалавриат"
    DIRECTORY_MAG_PATH = fr"{RootPath.ROOT_PATH}\ТИУ\От Хохлова\Выгрузка\Магистратура"

    @property
    def applicant_bac_files(self) -> List[str]:
        files = [
            self.DIRECTORY_BAC_PATH + "\\" + file_path for file_path in os.listdir(self.DIRECTORY_BAC_PATH)
        ]
        logger.info(f"Файлы успешно получены: {files}")
        return files

    @property
    def applicant_mag_files(self) -> List[str]:
        files = [
            file_path for file_path in os.listdir(self.DIRECTORY_MAG_PATH)
        ]
        logger.info(f"Файлы успешно получены: {files}")
        return files


data_files = DatasetsFiles()
