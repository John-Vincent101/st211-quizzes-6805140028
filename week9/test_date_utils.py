from unittest.mock import patch
from data_utils import report_name

@patch("data_utils.get_year")
def test_report_name(mock_get_year):
    mock_get_year.return_value = 2030

    assert report_name() == "report_2030"
