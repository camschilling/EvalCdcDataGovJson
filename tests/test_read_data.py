from src.evalcdcdatagovjson.read_data import get_data_cdc_gov_json, filter_to_dataset_dict
from src.evalcdcdatagovjson.clean_data import get_value_from_dict_if_exists


def test_get_data_cdc_gov_json():
    data = get_data_cdc_gov_json()

    assert data["@id"] == "https://data.cdc.gov/data.json"
    assert list(data.keys()) == ['@context', '@id', '@type', 'conformsTo', 'describedBy', 'dataset']


def test_filter_to_dataset_dict():
    expected_output={"one": 1, "two": 2, "three": 3}
    test_dict = {
        "source": "a good source",
        "dataset": expected_output
    }
    actual_output = filter_to_dataset_dict(dict=test_dict)
    assert actual_output == expected_output 



