import re


class PurchaseCounter:

    def __init__(self, path_to_file):
        self._path_to_file = path_to_file

    @staticmethod
    def _check_row_is_nas_digit(row: str):
        return bool(re.search(r'\d', row))

    @staticmethod
    def _print_total_by_purchase(total_by_purchase):
        print("Итог по всем покупкам:")
        print(total_by_purchase)

    def _count_total_by_purchase(self, file_as_purchase_data):
        total_by_purchase = {}
        for row in file_as_purchase_data:
            row.strip()
            if self._check_row_is_nas_digit(row):
                purchase_name, purchase_count = row.split(":")
                purchase_count = purchase_count.strip()
                if purchase_count.isdigit():
                    if purchase_name not in total_by_purchase:
                        total_by_purchase[purchase_name] = int(purchase_count)
                    else:
                        total_by_purchase[purchase_name] += int(purchase_count)
        return total_by_purchase

    def process_purchase_data(self):
        with open(self._path_to_file, "r") as file_as_purchase_data:
            total_by_purchase = self._count_total_by_purchase(file_as_purchase_data)
            self._print_total_by_purchase(total_by_purchase)