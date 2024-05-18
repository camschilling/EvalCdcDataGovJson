from .merge_data import produce_data


def execute(path: str):

    output = produce_data()

    validator_outpath = path + "/validator_detail" + ".csv"
    metadata_outpath = path + "/metadata_detail" + ".csv"

    output["validator_detail"].to_csv(validator_outpath)
    output["metadata_detail"].to_csv(metadata_outpath)
