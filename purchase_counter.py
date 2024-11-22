from expections import (
    ParseRowToPurchaseDataError,
    PurchaseCountIsNotIntegerError,
)


class PurchaseCounter:

    def __init__(self, path_to_file):
        self._path_to_file = path_to_file
        self._total_by_purchases = {}

    def _add_purchase_to_total_by_count(self, purchase_name: str, purchase_count: int):
        if purchase_name not in self._total_by_purchases:
            self._total_by_purchases[purchase_name] = purchase_count
        else:
            self._total_by_purchases[purchase_name] += purchase_count

    def _parse_row_to_purchase_data(self, row: str):
        purchase_data = [item.strip() for item in row.split(":")]
        if len(purchase_data) != 2:
            raise ParseRowToPurchaseDataError
        return purchase_data

    def _convert_purchase_count_to_integer(self, purchase_count: str) -> int:
        if not purchase_count.isdigit():
            raise PurchaseCountIsNotIntegerError
        return int(purchase_count)

    def _calculate_total_count_purchases(self):
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
        for purchase, count in self._total_by_purchases.items():
            print(f"{purchase}: {count}")

    def report_total_count_purchases(self):
        self._calculate_total_count_purchases()
        self._print_total_by_purchases()

counter = PurchaseCounter("data.txt")
counter._calculate_total_count_purchases()
print(counter._total_by_purchases)