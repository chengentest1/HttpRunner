from httprunner import loader, utils, parser

from httprunner.loader import load_tests
from httprunner.parser import parse_tests, _parse_testsuite, _parse_testcase, __parse_config, parse_data

pp='C:/Users/cheng/PycharmProjects/HttpRunner/tests/data/demo_testcase.yml'
# yu=load_tests(pp)
# print(yu)


def run_path(path, dot_env_path=None, mapping=None):

    tests_mapping = loader.load_tests(path, dot_env_path)
    tests_mapping["project_mapping"]["test_path"] = path

    if mapping:
        tests_mapping["project_mapping"]["variables"] = mapping

    if False:
        utils.dump_tests(tests_mapping, "loaded")
    return tests_mapping

tests_mapping = run_path(pp)
project_mapping = tests_mapping.get("project_mapping", {})
parsed_tests_mapping = {
            "project_mapping": project_mapping,
            "testcases": []
        }
''''
for key,volue in tests_mapping.items():
    print(key,">>>>>>>>>============")
    print(volue,"???????======")
tease=tests_mapping["testcases"]
print("lllllllllllllllllhhhhhhhhhhhh")
print(tease[0]['config'])
print("ooooooooooooyyeeeeeeeeeeeeeeeeeeeee")
ttte=tease.setdefault("config", {})
print(ttte)
# print(tests_mapping)
'''
for test_type in tests_mapping:
    if test_type == "testsuites":
        testsuites = tests_mapping["testsuites"]
    elif test_type == "testcases":
        for config1 in tests_mapping["testcases"]:
            config1.setdefault("config", {})
            config=config1['config']
            print(config1,"==================")
            print(project_mapping)
            raw_config_variables = config.pop("variables", {})
            print("====radddd==============",raw_config_variables)


#             testsuites = tests_mapping["testsuites"]
#             for testsuite in testsuites:
#                 parsed_testcases = _parse_testsuite(testsuite, project_mapping)
#                 for parsed_testcase in parsed_testcases:
#                     parsed_tests_mapping["testcases"].append(parsed_testcase)
#
#         elif test_type == "testcases":
#             for testcase in tests_mapping["testcases"]:
#                 testcase.setdefault("config", {})
#                 print(testcase)
#                 # __parse_config(testcase["config"], project_mapping)
#                     # _parse_testcase(testcase, project_mapping)
#                     # parsed_tests_mapping["testcases"].append(testcase)
#
#                     # return parsed_tests_mapping
# parse_tests(yu)
#
#
#
#
#
#
#


    # _parse_testcase(testcase, project_mapping)
#             parsed_tests_mapping["testcases"].append(testcase)

# #print(parsed_tests_mapping)
# parsed_tests_mapping.setdefault("config", {})
# # __parse_config(parsed_tests_mapping["config"], project_mapping)
# def __parse_config(config, project_mapping):
#
#     raw_config_variables = config.pop("variables", {})
#     raw_config_variables_mapping = utils.ensure_mapping_format(raw_config_variables)
#
#     override_variables = utils.deepcopy_dict(project_mapping.get("variables", {}))
#     functions = project_mapping.get("functions", {})
#
#     # override config variables with passed in variables
#     raw_config_variables_mapping.update(override_variables)
#
#     # parse config variables
#     parsed_config_variables = {}
#     for key, value in raw_config_variables_mapping.items():
#         parsed_value = parse_data(
#             value,
#             raw_config_variables_mapping,
#             functions,
#             raise_if_variable_not_found=False
#         )
#         parsed_config_variables[key] = parsed_value
#
#
#     if parsed_config_variables:
#         config["variables"] = parsed_config_variables
#
#     # parse config name
#     config["name"] = parse_data(
#         config.get("name", ""),
#         parsed_config_variables,
#         functions
#     )
#     print(config)
#
#     # parse config base_url
#     if "base_url" in config:
#         config["base_url"] = parse_data(
#             config["base_url"],
#             parsed_config_variables,
#             functions
#         )

# __parse_config(parsed_tests_mapping["config"],project_mapping)