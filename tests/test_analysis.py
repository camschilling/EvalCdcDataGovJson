import pandas as pd
from pandas.testing import assert_frame_equal
from src.evalcdcdatagovjson.analysis import (
    get_distribution_options_list,
    compute_distribution_is_open_machine_readable,
    eval_theme,
    eval_methodology,
    compute_is_fair_proxy,
)
from src.evalcdcdatagovjson.clean_data import build_pandas_df

# Add me back in if needing to test "add_analysis_fields"
# from src.evalcdcdatagovjson.analysis import add_analysis_fields
# from src.evalcdcdatagovjson.execute import produce_data


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


def test_org_theme_list():
    # df = build_pandas_df()
    # theme_list = get_org_theme_list(df=df)
    # print(theme_list)
    pass


def test_eval_theme():

    input_data = [[1, "NNDSS"], [2, "not_org"], [3, None]]
    input_columns = ["record_index", "theme"]
    test_input_df = pd.DataFrame(data=input_data, columns=input_columns)

    expected_output_data = [[1, "NNDSS", False], [2, "not_org", True], [3, None, False]]
    expected_output_columns = ["record_index", "theme", "theme_is_valid"]
    expected_output_df = pd.DataFrame(data=expected_output_data, columns=expected_output_columns)

    actual_output_df = eval_theme(df=test_input_df)
    assert_frame_equal(left=expected_output_df, right=actual_output_df)


def test_methodology_is_present():
    input_data = [[1, " "], [2, "a string"], [3, None]]
    input_columns = ["record_index", "methodology"]
    test_input_df = pd.DataFrame(data=input_data, columns=input_columns)

    expected_output_data = [[1, " ", False], [2, "a string", True], [3, None, False]]
    expected_output_columns = ["record_index", "methodology", "methodology_is_present"]
    expected_output_df = pd.DataFrame(data=expected_output_data, columns=expected_output_columns)

    actual_output_df = eval_methodology(df=test_input_df)
    assert_frame_equal(left=expected_output_df, right=actual_output_df)


def test_compute_is_fair_proxy():
    input_data = [
        [1, True, True, True, True],
        [2, True, True, True, False],
        [3, False, False, False, False],
        [4, None, True, True, True],
    ]
    input_columns = [
        "record_index",
        "methodology_is_present",
        "theme_is_valid",
        "distribution_is_open_machine_readable",
        "metadata_is_valid",
    ]
    test_input_df = pd.DataFrame(data=input_data, columns=input_columns)

    expected_output_data = [
        [1, True, True, True, True, True],
        [2, True, True, True, False, False],
        [3, False, False, False, False, False],
        [4, None, True, True, True, False],
    ]
    expected_output_columns = [
        "record_index",
        "methodology_is_present",
        "theme_is_valid",
        "distribution_is_open_machine_readable",
        "metadata_is_valid",
        "is_fair_proxy",
    ]
    expected_output_df = pd.DataFrame(data=expected_output_data, columns=expected_output_columns)

    actual_output_df = compute_is_fair_proxy(df=test_input_df)
    assert_frame_equal(left=expected_output_df, right=actual_output_df)


# def test_add_analysis_fields():

#     df_dict = produce_data()
#     df= df_dict["metadata_detail"]
#     df = add_analysis_fields(df=df)
#     cols = list(df.columns)
#     print(cols)
#     print(df)
