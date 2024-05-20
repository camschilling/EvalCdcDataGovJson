import pandas as pd
from pandas.testing import assert_frame_equal
from src.evalcdcdatagovjson.merge_data import (
    attach_identifiers_to_validator_data,
    attach_metadata_is_valid_col_to_metadata,
)
import pytest


@pytest.fixture
def mock_validator_df():
    data = [
        [
            "Dataset ?  ? accrualPeriodicity",
            "description of accrualPeriodicity issue",
            "Dataset",
            36,
            "accrualPeriodicity",
        ],
        ["Dataset ? 36 ? somethingElse", "description of somethingElse issue", "Dataset", 36, "somethingElse"],
    ]
    columns = ["header", "notes", 'record_type', 'record_index', 'record_problem_category']

    return pd.DataFrame(data, columns=columns)


@pytest.fixture
def mock_metadata_df():
    data = [
        [
            "id_for_35",
            "title35",
            "url_for_35",
            "theme_for_35",
            "org",
            "publisher_35",
            "email35",
            "public",
            "type35",
            ["text/csv", "application/rdf+xml"],
            None,
            35,
        ],
        [
            "id_for_36",
            "title36",
            "url_for_36",
            "theme_for_36",
            "org",
            "publisher_36",
            "email36",
            "public",
            "type36",
            ["text/csv", "application/rdf+xml"],
            "method36",
            36,
        ],
    ]
    columns = [
        'id',
        'title',
        'url',
        'theme',
        'publisher_type',
        'publisher_name',
        'contact_email',
        'access_level',
        'type',
        'distribution_options',
        "methodology",
        "record_index",
    ]

    return pd.DataFrame(data, columns=columns)


def test_attach_identifiers_to_validator_data(mock_validator_df, mock_metadata_df):
    actual_df = attach_identifiers_to_validator_data(validator_df=mock_validator_df, metadata_df=mock_metadata_df)

    expected_data = [
        [
            "Dataset ?  ? accrualPeriodicity",
            "description of accrualPeriodicity issue",
            "Dataset",
            36,
            "accrualPeriodicity",
            "id_for_36",
            "url_for_36",
            "theme_for_36",
            "publisher_36",
            "email36",
        ],
        [
            "Dataset ? 36 ? somethingElse",
            "description of somethingElse issue",
            "Dataset",
            36,
            "somethingElse",
            "id_for_36",
            "url_for_36",
            "theme_for_36",
            "publisher_36",
            "email36",
        ],
    ]

    expected_schema = [
        "header",
        "notes",
        'record_type',
        'record_index',
        'record_problem_category',
        'id',
        'url',
        'theme',
        'publisher_name',
        'contact_email',
    ]

    expected_df = pd.DataFrame(expected_data, columns=expected_schema)
    assert_frame_equal(actual_df, expected_df)


def test_attach_metadata_is_valid_col_to_metadata(mock_validator_df, mock_metadata_df):
    actual_df = attach_metadata_is_valid_col_to_metadata(validator_df=mock_validator_df, metadata_df=mock_metadata_df)

    expected_data = [
        [
            "id_for_35",
            "title35",
            "url_for_35",
            "theme_for_35",
            "org",
            "publisher_35",
            "email35",
            "public",
            "type35",
            ["text/csv", "application/rdf+xml"],
            None,
            35,
            True,
        ],
        [
            "id_for_36",
            "title36",
            "url_for_36",
            "theme_for_36",
            "org",
            "publisher_36",
            "email36",
            "public",
            "type36",
            ["text/csv", "application/rdf+xml"],
            "method36",
            36,
            False,
        ],
    ]
    expected_columns = [
        'id',
        'title',
        'url',
        'theme',
        'publisher_type',
        'publisher_name',
        'contact_email',
        'access_level',
        'type',
        'distribution_options',
        'methodology',
        'record_index',
        'metadata_is_valid',
    ]

    expected_df = pd.DataFrame(expected_data, columns=expected_columns)
    assert_frame_equal(actual_df, expected_df)
    print(actual_df)
