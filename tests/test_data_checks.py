from src.evalcdcdatagovjson.parse_data import get_value_from_dict_if_exists
from src.evalcdcdatagovjson.read_data import filter_to_dataset_dict, get_data_cdc_gov_json


def test_theme_is_single_attribute():
    data = get_data_cdc_gov_json()
    dataset = filter_to_dataset_dict(dict=data)  # this is a list of dictionaries
    cnt_list = set()
    for r in dataset:
        val = get_value_from_dict_if_exists(dict=r, key="theme")
        if val is not None:
            cnt_list.add(len(val))
    assert list(cnt_list) == [1]


## Below are some data profiling activities I didn't want to delete
# def test_get_data_profile():
#     data = get_data_cdc_gov_json()
#     dataset = filter_to_dataset_dict(dict=data) # this is a list of dictionaries
#     record = dataset[0]
#     # print(data["@context"])
#     # print(data["@id"])
#     # print(data["@type"])
#     # print(data["conformsTo"])
#     # print(data["describedBy"])
#     # json.loads(dataset[0])

#     # for i in data.keys():
#     #     d = data[i]
#     #     print("")
#     #     print(i)
#     #     if len(data[i]) < 5:
#     #         print(data[i])
#     #     else:
#     #         print("length of " + str(len(data[i])))

#     print(record["identifier"])
#     print(record["theme"])
#     print(record["publisher"]["@type"])
#     print(record["publisher"]["name"])
#     print(record["distribution"])
#     print(record["accessLevel"])


# def test_view_ninth():
#     data = get_data_cdc_gov_json()
#     dataset = filter_to_dataset_dict(dict=data) # this is a list of dictionaries
#     record = dataset[9]
#     id = record["identifier"]

#     print("")
#     # print(id)
#     # print("")
#     # print(record["distribution"])
#     # print("")
#     # print(record["distribution"][0])
#     # print("")
#     # print(record["distribution"][0]["mediaType"])
#     print(record)


# def test_get_keys():
#     data = get_data_cdc_gov_json()
#     dataset = filter_to_dataset_dict(dict=data) # this is a list of dictionaries

#     key_set = set()
#     l=0
#     for record in dataset:
#         for k in record.keys():
#             key_set.add(k)
#         l += 1

#     print(key_set)
