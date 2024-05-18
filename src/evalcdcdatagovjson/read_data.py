import json
import urllib.request


def get_data_cdc_gov_json():
    data_cdc_gov_json = "https://data.cdc.gov/data.json"
    with urllib.request.urlopen(data_cdc_gov_json) as url:
        data = json.load(url)
        return data


def filter_to_dataset_dict(dict: dict):
    # dict_keys(['@context', '@id', '@type', 'conformsTo', 'describedBy', 'dataset'])
    return dict["dataset"]


def validate_data_structure(dataset_list: list):
    # maybe use something like a pydantic model
    # available keys are
    # {'describedByType', 'distribution', 'theme', 'references', 'landingPage', 'title', 'accrualPeriodicity', 'license', 'publisher', 'identifier', 'language', 'contactPoint', 'programCode', 'isPartOf', 'modified', 'describedBy', 'issued', 'rights', 'keyword', 'temporal', '@type', 'accessLevel', 'bureauCode', 'description', 'spatial', 'systemOfRecords'}
    return dataset_list
