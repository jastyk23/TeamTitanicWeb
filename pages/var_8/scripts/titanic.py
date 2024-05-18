import csv


class Titanic:
    def __init__(self, path_name: str):
        self.path_name = path_name
        self._class_sex_data = {}
        self._sex_class_data = {}
        self.__get_parch_data_dict()

    def get_class(self) -> dict:
        return self._class_sex_data

    def get_sex(self) -> dict:
        return self._sex_class_data

    def _parse_sex_data(self, row: list) -> None:
        if not row[4] in self._class_sex_data:
            self._sex_class_data[row[4]] = {
                '1': 0,
                '2': 0,
                '3': 0,
            }
        self._sex_class_data[row[4]][row[2]] += 1

    def _parse_class_data(self, row: list) -> None:
        if not row[2] in self._class_sex_data:
            self._class_sex_data[row[2]] = {
                'female': 0,
                'male': 0
            }
        self._class_sex_data[row[2]][row[4]] += 1

    def __get_parch_data_dict(self) -> None:
        with open(self.path_name, 'r') as f:
            next(f)
            file = csv.reader(f, delimiter=',')
            for row in iter(file):
                self._parse_class_data(row)
                self._parse_sex_data(row)
            self._class_sex_data = dict(sorted(self._class_sex_data.items()))
