import pytest

from expections import ParseRowToPurchaseDataError, PurchaseCountIsNotIntegerError
from purchase_counter import PurchaseCounter


class TestPurchaseCounter:

    def test_parse_row_to_purchase_data(self):
        purchase_counter = PurchaseCounter("data.txt")

        assert purchase_counter._parse_row_to_purchase_data("apple: \n 13\n") == ["apple", "13"]

    def test_parse_row_to_purchase_data_when_row_has_not_purchase_data(self):
        purchase_counter = PurchaseCounter("data.txt")
        with pytest.raises(ParseRowToPurchaseDataError):
            assert purchase_counter._parse_row_to_purchase_data("appleqwqweqwe")

    def test_convert_purchase_count_to_integer(self):
        purchase_counter = PurchaseCounter("data.txt")

        assert purchase_counter._convert_purchase_count_to_integer("13") == 13

    def test_convert_purchase_count_to_integer_when_purchase_count_is_not_integer(self):
        purchase_counter = PurchaseCounter("data.txt")
        with pytest.raises(PurchaseCountIsNotIntegerError):
            assert purchase_counter._convert_purchase_count_to_integer("три")

    def test_calculate_total_count_by_purchases(self):
        purchase_counter = PurchaseCounter("data.txt")
        purchase_counter._calculate_total_amount_by_each_purchase()
        assert purchase_counter._total_amount_by_each_purchase == {'apple': 13, 'banana': 7, 'grape': 6}

    def test_calculate_total_count_by_purchases_when_file_has_empty_lines(self):
        purchase_counter = PurchaseCounter("data_with_empty_lines.txt")
        purchase_counter._calculate_total_amount_by_each_purchase()
        assert purchase_counter._total_amount_by_each_purchase == {'apple': 13, 'banana': 7, 'grape': 6}

    def test_calculate_total_count_by_purchases_when_file_has_only_float_integers(self):
        purchase_counter = PurchaseCounter("data_with_float.txt")
        purchase_counter._calculate_total_amount_by_each_purchase()
        assert purchase_counter._total_amount_by_each_purchase == {}