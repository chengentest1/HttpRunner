from httprunner import loader, utils

from httprunner.loader import load_tests
pp='E:/HttpRunner/tests/data/demo_testcase_cli.yml'
# yu=load_tests(pp)
# print(yu)


def run_path(path, dot_env_path=None, mapping=None):

    tests_mapping = loader.load_tests(path, dot_env_path)
    print(tests_mapping)
    print(path)
    tests_mapping["project_mapping"]["test_path"] = path
    print(tests_mapping)

    if mapping:
        tests_mapping["project_mapping"]["variables"] = mapping

    if False:
        utils.dump_tests(tests_mapping, "loaded")
run_path(pp)