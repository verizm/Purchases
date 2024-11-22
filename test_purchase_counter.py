from purchase_counter import PurchaseCounter


class TestPurchaseCounter:
    def test_count_total_by_purchase(self):
        purchase_counter = PurchaseCounter("data.txt")
        with open("data.txt", "r") as file_as_purchase_data:
            total_by_purchase = purchase_counter._count_total_by_purchase(file_as_purchase_data)
        assert total_by_purchase == {'apple': 13, 'banana': 7, 'grape': 6}

    def test_count_total_by_purchase_when_file_has_empty_lines(self):
        purchase_counter = PurchaseCounter("data_with_empty_lines.txt")
        with open("data_with_empty_lines.txt", "r") as file_as_purchase_data:
            total_by_purchase = purchase_counter._count_total_by_purchase(file_as_purchase_data)
        assert total_by_purchase == {'apple': 13, 'banana': 7, 'grape': 6}

    def test_count_total_by_purchase_when_file_has_float_integers(self):
        purchase_counter = PurchaseCounter("data.txt")
        with open("data_with_float.txt", "r") as file_as_purchase_data:
            total_by_purchase = purchase_counter._count_total_by_purchase(file_as_purchase_data)
        assert total_by_purchase == {}

    def test_count_total_by_purchase_when_file_has_not_purchase_data(self):
        purchase_counter = PurchaseCounter("data.txt")
        with open("data_with_float.txt", "r") as file_as_purchase_data:
            total_by_purchase = purchase_counter._count_total_by_purchase(file_as_purchase_data)
        assert total_by_purchase == {}
