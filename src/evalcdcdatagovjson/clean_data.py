def get_value_from_dict_if_exists(dict: dict, key: str):
    """
    Returns a value from a dictionary if the corresponding key exists.
    If the key does not exist, then returns None
    """
    if key in dict.keys():
        return dict[key]
    else:
        return None
    

def get_url(record: dict):
    """Get the url for the record"""
    return get_value_from_dict_if_exists(dict=record, key="identifier")


def get_identifier(record: dict):
    """Parses the longer URL from the record identifier """
    id_string = get_url(record=record)
    if id_string is not None:
        return id_string.rstrip("/")
    else:
        return None


def get_theme(record: dict):
    """Get the theme for the record"""
    theme_list = get_value_from_dict_if_exists(dict=record, key="theme")
    return theme_list[0]


def get_publisher_attribute(record: dict, publisher_attribute_key: str):
    """Helper function to get publisher information from a record """
    record_publisher = get_value_from_dict_if_exists(dict=record, key="publisher")
    if record_publisher is not None:
        return get_value_from_dict_if_exists(dict=record_publisher, key=publisher_attribute_key)
    else:
        return None


def get_publisher_type(record: dict):
    """Operation to get the publisher type (e.g. organization) from a record"""
    return get_publisher_attribute(record=record, publisher_attribute_key="@type")


def get_publisher_name(record: dict):
    """Operation to get the publisher name from a record"""
    return get_publisher_attribute(record=record, publisher_attribute_key="name")


def get_access_level(record:dict):
    """
    Operation to get the access level for a given record (e.g. public, restricted)
    """
    return get_value_from_dict_if_exists(dict=record, key="accessLevel")


def get_distribution_option_list(record:dict):
    """
    Operation to get the various download formats that are available for a given catalog record
    :returns: a list of values 
    """
    distribution_list = get_value_from_dict_if_exists(dict=record, key="distribution")
    media_list = list()
    for d in distribution_list:
        media_list.append(d["mediaType"])
    return media_list


def compile_record_attributes(record:dict):
    """Produces a dictionary of relevant attributes for a given record"""
    record_attributes = {
        "id": get_identifier(record=record),
        "url": get_url(record=record),
        "theme": get_theme(record=record),
        "publisher_type": get_publisher_type(record=record),
        "publisher_name": get_publisher_name(record=record),
        "access_level": get_access_level(record=record),
        "distribution_options": get_distribution_option_list(record=record)
    }
    return record_attributes


## Evaluate if a record is a dataset or not using "@type" == 'dcat:Dataset'