# Evaluating data.cdc.gov
This modules aims to capture and evaluate metrics pertaining to whether the data meets certain data principles.

This module produces 2 analysis-ready .csv files for evaluating certain metrics.

The `metadata_detail.csv` file is metadata regarding datasets on data.cdc.gov. This metadata has been sourced from https://data.cdc.gov/data.json alongside an indicator regarding adherence to federal metadata standards sourced from https://catalog.data.gov/dcat-us/validator. Columns produced are: [`id`, `url`, `theme`, `publisher_type`, `publisher_name`, `contact_email`, `access_level`, `type`, `distribution_options`, `record_index`, `metadata_is_valid`]

The `validator_detail.csv` file is detailed data obtained from an evaluation (conducted by https://catalog.data.gov/dcat-us/validator) of federal metadata standards of  https://data.cdc.gov/data.json. This data has been joined with the metadata itself such that additional record information is readily available. Columns produced are  [`header`, `notes`, `record_type`, `record_index`, `record_problem_category`, `id`, `url`, `theme`, `publisher_name`, `contact_email`]

## Execution
After cloning this respository, executing this module should look like running a python file such as:
```
from EvalCdcDataGovJson.src.evalcdcdatagovjson.execute import execute
execute(path="<path to write data to>")
```

The module assumes the user has the required packages installed on their machine and that a selenium web driver for Microsoft Edge is installed. 

## Contribution
The virtual environment for contribution is included in the repo at `eval_cdc_data_gov_json`. Contributors should use `pre-commit install` prior to contributing. Contributors should test module using `poetry run pytest`.

Repository adapted from https://laszlo.substack.com/p/cq4ds-python-project-from-scratch
