from expections import (
    ParseRowToPurchaseDataError,
    PurchaseCountIsNotIntegerError,
)


class PurchaseCounter:

    def __init__(self, path_to_file):
        self._path_to_file = path_to_file
        self._total_amount_by_each_purchase = {}

    def _add_purchase_to_total_by_count(self, purchase_name: str, purchase_count: int):
        if purchase_name not in self._total_amount_by_each_purchase:
            self._total_amount_by_each_purchase[purchase_name] = purchase_count
        else:
            self._total_amount_by_each_purchase[purchase_name] += purchase_count

    @staticmethod
    def _parse_row_to_purchase_data(row: str):
        purchase_data = [item.strip() for item in row.split(":")]
        if len(purchase_data) != 2:
            raise ParseRowToPurchaseDataError
        return purchase_data

    @staticmethod
    def _convert_purchase_count_to_integer(purchase_count: str) -> int:
        if not purchase_count.isdigit():
            raise PurchaseCountIsNotIntegerError
        return int(purchase_count)

    def _calculate_total_amount_by_each_purchase(self):
        with open(self._path_to_file, "r") as file_as_purchase_data:
            for row in file_as_purchase_data:
                try:
                    purchase_name, purchase_count = self._parse_row_to_purchase_data(row)
                    purchase_count_as_int = self._convert_purchase_count_to_integer(purchase_count)

                    self._add_purchase_to_total_by_count(purchase_name, purchase_count_as_int)
                except (ParseRowToPurchaseDataError, PurchaseCountIsNotIntegerError):
                    continue

    def _print_total_by_purchases(self):
        print("Итог по всем покупкам:")
        for purchase, count in self._total_amount_by_each_purchase.items():
            print(f"{purchase}: {count}")

    def report_total_amount_by_each_purchase(self):
        self._calculate_total_amount_by_each_purchase()
        self._print_total_by_purchases()
