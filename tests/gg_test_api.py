from httprunner.loader import load_folder_content
from httprunner import exceptions, logger

def load_api_folder(api_folder_path):

    api_definition_mapping = {}

    api_items_mapping = load_folder_content(api_folder_path)

    for api_file_path, api_items in api_items_mapping.items():

        if isinstance(api_items, list):
            for api_item in api_items:
                key, api_dict = api_item.popitem()
                api_id = api_dict.get("id")
                if api_id in api_definition_mapping:
                    logger.log_warning("API definition duplicated: {}".format(api_id))

                api_definition_mapping[api_id] = api_dict

        elif isinstance(api_items, dict):
            if api_file_path in api_definition_mapping:
                logger.log_warning("API definition duplicated: {}".format(api_file_path))

            api_definition_mapping[api_file_path] = api_items

    return api_definition_mapping

r=load_folder_content('C:/Users/cheng/PycharmProjects/HttpRunner/tests/api')
print(r)