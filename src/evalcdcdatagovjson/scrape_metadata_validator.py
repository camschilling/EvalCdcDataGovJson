from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd


def query_cdc_metadata_validator():
    """
    Activate a selenium web driver and use beautiful soup to parse web data
    """
    driver = webdriver.Edge()
    cdc_site = "https://data.cdc.gov/data.json"

    driver.get("https://catalog.data.gov/dcat-us/validator")

    search_bar = driver.find_element(By.ID, 'validate_url')  # can also try "validate_url"
    search_bar.clear()
    search_bar.send_keys(cdc_site)
    search_bar.send_keys(Keys.ENTER)

    html = driver.page_source
    driver.quit()
    # Pass source to bs4
    soup = BeautifulSoup(html, 'html.parser')
    validation_results = soup.find("div", {"class": "module-content"})
    return validation_results


def strip_unicode_characters_from_header(header_text: str):
    return header_text.encode('ascii', 'replace').decode()


def scrape_validation_results():
    """
    Query the validator and convert relevant data into a structured dictionary for future processing
    :returns: a dictionary with keys that are the individual headers with the unicode objects converted to "?"
    """
    validation_results = query_cdc_metadata_validator()

    # Get the headers within the validation results
    validation_headers = validation_results.find_all("h3")  # .get_text(strip=True)

    # Get specific text within the html blob
    validation_header_text = list()
    for h in validation_headers:
        header_text = h.get_text()
        validation_header_text.append(header_text)

    # Loop through the headers and pull text beneath the headers
    validation_dict = dict()
    for t in validation_header_text:
        validation_notes = list()
        target = validation_results.find("h3", string=t)
        for sib in target.find_next_siblings():
            if sib.name == "h3":
                break
            else:
                validation_notes.append(sib.get_text())
        # Combine any cases where there are multiple notes
        validation_notes_str = " & ".join(validation_notes)
        # Strip unicode out of dictionary keys
        stripped_header_text = strip_unicode_characters_from_header(header_text=t)
        validation_dict[stripped_header_text] = validation_notes_str

    return validation_dict


def convert_scraped_to_pandas(scraped_dict: dict):
    """
    Convert scraped validator data into a pandas dataframe
    """
    df = pd.DataFrame.from_dict(scraped_dict, orient='index')
    df = df.reset_index()
    df.columns = ["header", "notes"]
    return df


def map_header_column(df: pd.DataFrame):
    """
    Parse the data that came from the HTML header to get more structured data
    """
    # Remove unnecessary string from header
    df["header"] = df["header"].str.replace(" has a problem", "")

    # Parse header
    # we can't use
    # df[["record_type", "record_index", "record_problem_category"]] = df['header'].str.split("?", expand=True)
    # because there are variable number of unicode characters in a given header
    df['record_type'] = df["header"].str.split("?", expand=True)[0]
    df['record_index'] = df["header"].str.split("?", expand=True)[1]
    df['record_problem_category'] = df["header"].str.split("?", expand=True)[2]

    # Clean up columns
    df["record_type"] = df["record_type"].str.replace(" ", "")
    df["record_index"] = df["record_index"].str.replace(" ", "")
    df["record_problem_category"] = df["record_problem_category"].str.replace(" ", "")
    return df


def get_validation_data() -> pd.DataFrame:
    """
    Queries the data.gov metadata validator (https://catalog.data.gov/dcat-us/validator) to evaluate data.cdc.gov metadata (https://data.cdc.gov/data.json).

    :returns: a pandas dataframe containing scraped results
    """
    scraped_dict = scrape_validation_results()
    df = convert_scraped_to_pandas(scraped_dict=scraped_dict)
    df = map_header_column(df=df)
    return df
