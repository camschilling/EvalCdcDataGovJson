from .merge_data import produce_data
from .summarize import summarize


def execute(path: str, include_summary=True):

    output = produce_data()

    validator_outpath = path + "/validator_detail" + ".csv"
    metadata_outpath = path + "/metadata_detail" + ".csv"

    output["validator_detail"].to_csv(validator_outpath)
    output["metadata_detail"].to_csv(metadata_outpath)

    if include_summary:
        summary_df = summarize(df=output["metadata_detail"])
        summary_path = path + "/summary" + ".csv"
        summary_df.to_csv(summary_path)
