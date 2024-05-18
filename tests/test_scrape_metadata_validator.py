from src.evalcdcdatagovjson.scrape_metadata_validator import (
    query_cdc_metadata_validator,
    get_validation_data,
    strip_unicode_characters_from_header,
    convert_scraped_to_pandas,
    map_header_column,
    scrape_validation_results,
)
import pandas as pd
from pandas.testing import assert_frame_equal


def test_query_cdc_metadata_validator():
    query_cdc_metadata_validator()


def test_strip_unicode_characters_from_header():
    test_input = "Dataset ➡ 36 ➡ accrualPeriodicity has a problem"
    expected_output = "Dataset ? 36 ? accrualPeriodicity has a problem"

    actual_output = strip_unicode_characters_from_header(header_text=test_input)
    assert expected_output == actual_output


def test_scrape_validation_results():
    results_dict = scrape_validation_results()
    print("")
    print(results_dict)


def test_convert_scraped_to_pandas_multi():
    test_input = {"header1": "str1", "header2": "str2 & str3"}
    df = convert_scraped_to_pandas(scraped_dict=test_input)
    assert isinstance(df, pd.DataFrame)


def test_convert_scraped_to_pandas():
    test_input = {
        "Dataset ? 36 ? accrualPeriodicity has a problem": "'No longer updated (dataset archived)' is not valid under any of the given schemas.",
        "Dataset ? 102 ? rights has a problem": "'This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\\xa0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\\xa0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\\xa0 For more information about submitting a proposal for data access, please see:\\xa0https://www.cdc.gov/rdc/leftbrch/presubmit.htm' is not valid under any of the given schemas.",
    }
    actual_df = convert_scraped_to_pandas(scraped_dict=test_input)

    expected_data = [
        [
            "Dataset ? 36 ? accrualPeriodicity has a problem",
            "'No longer updated (dataset archived)' is not valid under any of the given schemas.",
        ],
        [
            "Dataset ? 102 ? rights has a problem",
            "'This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\\xa0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\\xa0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\\xa0 For more information about submitting a proposal for data access, please see:\\xa0https://www.cdc.gov/rdc/leftbrch/presubmit.htm' is not valid under any of the given schemas.",
        ],
    ]
    expected_columns = ["header", "notes"]

    expected_df = pd.DataFrame(expected_data, columns=expected_columns)
    assert_frame_equal(expected_df, actual_df)


def test_map_header_column():
    data = [
        [
            "Dataset ? 36 ? accrualPeriodicity has a problem",
            "'No longer updated (dataset archived)' is not valid under any of the given schemas.",
        ],
        [
            "Dataset ? 102 ? rights has a problem",
            "'This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\\xa0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\\xa0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\\xa0 For more information about submitting a proposal for data access, please see:\\xa0https://www.cdc.gov/rdc/leftbrch/presubmit.htm' is not valid under any of the given schemas.",
        ],
        ["Dataset ? 45 has a problem", "something else."],
        ["Dataset ? 22 ? attribute has a problem ?", "something else."],
    ]
    columns = ["header", "notes"]

    input_df = pd.DataFrame(data, columns=columns)
    df = map_header_column(df=input_df)
    df_cols = list(df.columns)
    for c in ['record_type', 'record_index', 'record_problem_category']:
        assert c in df_cols


def test_get_validation_data():
    df = get_validation_data()
    assert isinstance(df, pd.DataFrame)
    print("")
    print("num_records")
    print(len(df))
    for c in ['record_type', 'record_index', 'record_problem_category']:
        print("")
        print(c)
        print(df[c].unique())
