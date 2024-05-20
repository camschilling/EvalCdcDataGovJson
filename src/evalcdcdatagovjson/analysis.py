import pandas as pd
import numpy as np
from typing import List, Dict


def get_distribution_options_list(df: pd.DataFrame) -> List[str]:
    """
    Read the data from the distribution options fields and categorize
    As of 5/20/24 the following distributions were included in the metadata:
    [
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
        'text/csv'
    ]
    The operation assumes the provided dataframe has column `distribution_options` as a list of strings (not string).
    :returns: a list of items that are found
    """

    all_distribution_options = df["distribution_options"]
    distribution_options = set()

    for dist_opt in all_distribution_options:
        if dist_opt is not None:

            if isinstance(dist_opt, list):
                for d in dist_opt:
                    distribution_options.add(d)
            else:
                distribution_options.add(dist_opt)
        else:
            pass

    return list(distribution_options)


def categorize_distribution_options_list(distribution_options_list: List[str]) -> Dict[str, bool]:
    """
    Accepts the list of distribution option values.
    Return a dictionary where the dictionary keys are the attributes of the list
    and the dictionary values are an indicator of whether the key is an open machine readable distribution option
    """
    # This is an approximation based on the current values as of 5/20/2024 by @camschilling.
    # TODO maintenance approach needed

    machine_readable_list = [
        "application/rdf+xml",
        "application/html",
        "text/plain",
        "application/json",
        "application/xml",
        "text/html",
        "text/csv",
    ]
    distribution_options_machine_readable_dict = dict()
    for dist_opt in distribution_options_list:
        eval = dist_opt in machine_readable_list
        distribution_options_machine_readable_dict[dist_opt] = eval

    return distribution_options_machine_readable_dict


def compute_distribution_is_open_machine_readable(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a column to the metadata table for whether the distribution formats are open and machine readable
    Refer to function categorize_distribution_options_list for the list of accepted machine readable distribution types
    """
    # Get dictionary mapping for values
    distribution_options_machine_readable_dict = categorize_distribution_options_list(
        distribution_options_list=get_distribution_options_list(df=df)
    )
    # Explode by distribution list
    df_exploded = df.explode("distribution_options").rename(columns={"distribution_options": "distribution_option"})
    # Map distribution method to boolean indicator
    df_exploded["distribution_is_open_machine_readable"] = df_exploded["distribution_option"].map(
        distribution_options_machine_readable_dict
    )
    # Group back down to record index level
    df_grouped = pd.DataFrame(
        df_exploded.groupby(["record_index"])["distribution_is_open_machine_readable"].max()
    ).reset_index()
    # Join back to original df
    df = pd.merge(df, df_grouped, on="record_index", how="left")
    return df
