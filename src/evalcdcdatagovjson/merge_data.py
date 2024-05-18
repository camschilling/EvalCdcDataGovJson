from .scrape_metadata_validator import get_validation_data
from .clean_data import build_pandas_df
import pandas as pd


def attach_identifiers_to_validator_data(validator_df: pd.DataFrame, metadata_df: pd.DataFrame):
    """
    Joins the identifiers and certain attributes coming from the metadata itself to the validator output
    Uses the index of the metadata
    """
    df = pd.merge(
        validator_df,
        metadata_df[['id', 'url', 'theme', 'publisher_name', 'record_index']],
        on="record_index",
        how="left",
    )
    return df


def attach_metadata_is_valid_col_to_metadata(validator_df: pd.DataFrame, metadata_df: pd.DataFrame):
    """
    Finds the unique records that have invalid metadata and creates boolean indicator, attaches to metadata df
    """
    invalid_metadata_records = pd.DataFrame(
        {"record_index": validator_df["record_index"].unique(), "metadata_is_valid": False}
    )

    df = pd.merge(metadata_df, invalid_metadata_records, on="record_index", how="left")
    df[["metadata_is_valid"]] = df[["metadata_is_valid"]].fillna(value=True)

    return df


def produce_data():
    """
    Compiles real data at detail level for analysis
    """
    validator_df = get_validation_data()
    metadata_df = build_pandas_df()

    return {
        "validator_detail": attach_identifiers_to_validator_data(validator_df=validator_df, metadata_df=metadata_df),
        "metadata_detail": attach_metadata_is_valid_col_to_metadata(validator_df=validator_df, metadata_df=metadata_df),
    }
