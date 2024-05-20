import pandas as pd
from pandas.testing import assert_frame_equal
from src.evalcdcdatagovjson.analysis import get_distribution_options_list, compute_distribution_is_open_machine_readable
from src.evalcdcdatagovjson.clean_data import build_pandas_df


def test_get_distribution_options_list():
    df = build_pandas_df()
    distribution_options = get_distribution_options_list(df=df)
    assert isinstance(distribution_options, list)
    print(distribution_options)


def test_get_distribution_options_list_values():
    """Test to see if values are still the same. If values are not the same, function categorize_distribution_options_list should be updated"""
    df = build_pandas_df()
    distribution_options = get_distribution_options_list(df=df)
    expected_list = [
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/x-zip-compressed',
        'application/rdf+xml',
        'application/zip',
        'application/html',
        'text/plain',
        'application/json',
        'application/xml',
        'application/vnd.ms-excel',
        'application/pdf',
        'text/html',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'text/csv',
    ]
    assert distribution_options.sort() == expected_list.sort()


def test_compute_open_machine_readable_distributions():

    input_data = [[1, ["text/csv", "not"]], [2, ["not", "not"]], [3, [None]], [4, None]]
    input_columns = ["record_index", "distribution_options"]
    test_input_df = pd.DataFrame(data=input_data, columns=input_columns)

    expected_output_data = [
        [1, ["text/csv", "not"], True],
        [2, ["not", "not"], False],
        [3, [None], False],
        [4, None, False],
    ]
    expected_output_columns = ["record_index", "distribution_options", "distribution_is_open_machine_readable"]
    expected_output_df = pd.DataFrame(data=expected_output_data, columns=expected_output_columns)

    actual_output_df = compute_distribution_is_open_machine_readable(df=test_input_df)
    assert_frame_equal(left=expected_output_df, right=actual_output_df)
