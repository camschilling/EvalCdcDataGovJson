import pandas as pd

# how many records?
# how many records are public? (access level)
# how many records are public or restricted-public? Use this as denominator

# How many of these records have valid metadata?
# How many records have valid theme?
# How many records have open mechine readable distribution?
# How many records have a methodology?
# How many records meet fair proxy definition?


def summarize(df: pd.DataFrame):
    summary_dict = dict()

    summary_dict["total_count"] = len(df)
    summary_dict["count_public"] = len(df.loc[df["access_level"] == "public"])
    summary_dict["count_public_or_restricted_public"] = len(
        df.loc[df["access_level"].isin(["public", "restricted public"])]
    )

    denom_df = df.loc[df["access_level"].isin(["public", "restricted public"])]

    summary_dict["count_denom"] = len(denom_df)
    summary_dict["count_non_org_theme"] = len(denom_df.loc[denom_df["theme_is_valid"] == True])
    summary_dict["open_machine_readable_distribution"] = len(
        denom_df.loc[denom_df["distribution_is_open_machine_readable"] == True]
    )
    summary_dict["has_methodology"] = len(denom_df.loc[denom_df["methodology_is_present"] == True])
    summary_dict["valid_metadata"] = len(denom_df.loc[denom_df["metadata_is_valid"] == True])
    summary_dict["count_fair_proxy"] = len(denom_df.loc[denom_df["is_fair_proxy"] == True])

    summary_df = pd.DataFrame.from_dict(summary_dict, orient='index')

    return summary_df
