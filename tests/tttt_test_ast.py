import ast
import re
# variable_regexp = r"\$([\w_]+)"
# def extract_variables(content):
#     return re.findall(variable_regexp, content)
# oo=extract_variables("$u_oken")
# print(oo)
pp='C:/Users/cheng/PycharmProjects/HttpRunner/tests/data/demo_testcase_cli.yml'
from httprunner.api import HttpRunner


def run_path(self, path, dot_env_path=None, mapping=None):
    """ run testcase/testsuite file or folder.

    Args:
        path (str): testcase/testsuite file/foler path.
        dot_env_path (str): specified .env file path.
        mapping (dict): if mapping is specified, it will override variables in config block.

    Returns:
        instance: HttpRunner() instance

    """
    # load tests
    self.exception_stage = "load tests"
    tests_mapping = loader.load_tests(path, dot_env_path)
    tests_mapping["project_mapping"]["test_path"] = path

    if mapping:
        tests_mapping["project_mapping"]["variables"] = mapping

    if self.save_tests:
        utils.dump_tests(tests_mapping, "loaded")

    return self.run_tests(tests_mapping)