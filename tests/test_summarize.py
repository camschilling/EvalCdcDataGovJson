from src.evalcdcdatagovjson.summarize import summarize
import pandas as pd


def test_summarize():
    test_input_data = [
        [1, "public", True, True, True, True, True],
        [2, "restricted public", True, True, True, False, False],
        [3, "public", False, False, False, False, False],
        [4, "non-public", None, True, True, True, False],
        [5, "non-public", True, True, True, True, True],
    ]
    test_input_columns = [
        "record_index",
        "access_level",
        "methodology_is_present",
        "theme_is_valid",
        "distribution_is_open_machine_readable",
        "metadata_is_valid",
        "is_fair_proxy",
    ]
    test_input_df = pd.DataFrame(data=test_input_data, columns=test_input_columns)

    output_df = summarize(df=test_input_df)

    assert isinstance(output_df, pd.DataFrame)

    print(output_df)
