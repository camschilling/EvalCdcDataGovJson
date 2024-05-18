from src.evalcdcdatagovjson.clean_data import (
    compile_record_attributes,
    get_distribution_option_list,
    get_value_from_dict_if_exists,
)


def test_get_value_from_dict_if_exists_pass():
    test_dict = {"test_key": 1}
    out = get_value_from_dict_if_exists(dict=test_dict, key="test_key")
    assert out == 1


def test_get_value_from_dict_if_exists_fail():
    test_dict = {"test_key": 1}
    out = get_value_from_dict_if_exists(dict=test_dict, key="bad")
    assert out is None


def test_get_distribution_option_list():
    record_input = {
        "distribution": [
            {
                '@type': 'dcat:Distribution',
                'downloadURL': 'https://data.cdc.gov/api/views/29hc-w46k/rows.csv?accessType=DOWNLOAD',
                'mediaType': 'text/csv',
            },
            {
                'mediaType': 'application/rdf+xml',
                'downloadURL': 'https://data.cdc.gov/api/views/29hc-w46k/rows.rdf?accessType=DOWNLOAD',
                'describedBy': 'https://data.cdc.gov/api/views/29hc-w46k/columns.rdf',
                'describedByType': 'application/rdf+xml',
                '@type': 'dcat:Distribution',
            },
            {
                'mediaType': 'application/json',
                'downloadURL': 'https://data.cdc.gov/api/views/29hc-w46k/rows.json?accessType=DOWNLOAD',
                'describedBy': 'https://data.cdc.gov/api/views/29hc-w46k/columns.json',
                'describedByType': 'application/json',
                '@type': 'dcat:Distribution',
            },
            {
                'mediaType': 'application/xml',
                'downloadURL': 'https://data.cdc.gov/api/views/29hc-w46k/rows.xml?accessType=DOWNLOAD',
                'describedBy': 'https://data.cdc.gov/api/views/29hc-w46k/columns.xml',
                'describedByType': 'application/xml',
                '@type': 'dcat:Distribution',
            },
        ]
    }
    expected_output = ["text/csv", "application/rdf+xml", "application/json", "application/xml"]
    actual_output = get_distribution_option_list(record=record_input)
    assert expected_output == actual_output


def test_compile_record_attributes():
    record_input = {
        'accessLevel': 'public',
        'landingPage': 'https://www.cdc.gov/rsv/research/rsv-net.html',
        'bureauCode': ['009:20'],
        'issued': '2024-04-25',
        '@type': 'dcat:Dataset',
        'modified': '2024-05-16',
        'references': ['https://www.cdc.gov/rsv/research/rsv-net.html'],
        'keyword': [
            'age-adjusted rates',
            'age-adjusted rates by race and ethnicity',
            'hospitalization',
            'hospitalization rate',
            'hospitalizations',
            'rate',
            'rates by race and ethnicity',
            'respiratory disease',
            'respiratory illness',
            'respiratory syncytial virus',
            'respiratory virus response',
            'rsv',
            'rsvnet',
            'rsv-net',
            'surveillance',
        ],
        'contactPoint': {'@type': 'vcard:Contact', 'fn': 'RESP-NET', 'hasEmail': 'mailto:pgn6@cdc.gov'},
        'publisher': {'@type': 'org:Organization', 'name': 'CDC'},
        'identifier': 'https://data.cdc.gov/api/views/29hc-w46k',
        'description': 'The Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET) is a network that conducts active, population-based surveillance for laboratory-confirmed RSV-associated hospitalizations in children younger than 18 years of age and adults. The network currently includes 58 counties in 12 states, and data are collected and reported during the October 1-April 30 season each year.  In some years, additional months of data are collected.  In adults, RSV hospitalization tracking began in the 2016–2017 season. In children less than 18 years of age, surveillance began in the 2018–19 season. Because the surveillance areas and age groups included in surveillance have changed over time, trends should be interpreted with caution. Hospitalization data are preliminary and subject to change as more data become available.  In particular, case counts and rates for recent hospitalizations are subject to lag.  Lag for RSV-NET case identification and reporting might increase around holidays or during periods of increased hospitalization utilization.  As data are received each week, prior case counts and rates are updated accordingly.\nFor more information about RSV-NET, please see https://www.cdc.gov/rsv/research/rsv-net.html.',
        'title': 'Weekly Rates of Laboratory-Confirmed RSV Hospitalizations from the RSV-NET Surveillance System',
        'programCode': ['009:038'],
        'distribution': [
            {
                '@type': 'dcat:Distribution',
                'downloadURL': 'https://data.cdc.gov/api/views/29hc-w46k/rows.csv?accessType=DOWNLOAD',
                'mediaType': 'text/csv',
            },
            {
                'mediaType': 'application/rdf+xml',
                'downloadURL': 'https://data.cdc.gov/api/views/29hc-w46k/rows.rdf?accessType=DOWNLOAD',
                'describedBy': 'https://data.cdc.gov/api/views/29hc-w46k/columns.rdf',
                'describedByType': 'application/rdf+xml',
                '@type': 'dcat:Distribution',
            },
            {
                'mediaType': 'application/json',
                'downloadURL': 'https://data.cdc.gov/api/views/29hc-w46k/rows.json?accessType=DOWNLOAD',
                'describedBy': 'https://data.cdc.gov/api/views/29hc-w46k/columns.json',
                'describedByType': 'application/json',
                '@type': 'dcat:Distribution',
            },
            {
                'mediaType': 'application/xml',
                'downloadURL': 'https://data.cdc.gov/api/views/29hc-w46k/rows.xml?accessType=DOWNLOAD',
                'describedBy': 'https://data.cdc.gov/api/views/29hc-w46k/columns.xml',
                'describedByType': 'application/xml',
                '@type': 'dcat:Distribution',
            },
        ],
        'spatial': 'RSV-NET Sites',
        'license': 'https://www.usa.gov/government-works',
        'accrualPeriodicity': 'Weekly',
        'theme': ['Public Health Surveillance'],
    }
    expected_output = {
        "id": "29hc-w46k",
        "url": "https://data.cdc.gov/api/views/29hc-w46k",
        "theme": "Public Health Surveillance",
        "publisher_type": "org:Organization",
        "publisher_name": "CDC",
        "access_level": "public",
        "distribution_options": ["text/csv", "application/rdf+xml", "application/json", "application/xml"],
    }
    actual_ouptput = compile_record_attributes(record=record_input)
    # assert expected_output == actual_ouptput
    print(expected_output)
