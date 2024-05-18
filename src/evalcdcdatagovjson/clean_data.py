from .read_data import get_data_cdc_gov_json, filter_to_dataset_dict
from .parse_data import compile_record_attributes
import pandas as pd


def build_pandas_df():
    dataset = filter_to_dataset_dict(dict=get_data_cdc_gov_json())
    attributes = dict()
    i = 0
    for record in dataset:
        attributes[i] = compile_record_attributes(record=record)
        i += 1
    df = pd.DataFrame.from_dict(attributes, orient='index')
    return df


## Evaluate if a record is a dataset or not using "@type" == 'dcat:Dataset'
