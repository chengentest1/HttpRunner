import io
import yaml

from httprunner.loader import load_file, load_testsuite, load_testcase, __extend_with_api_ref, \
    __extend_with_testcase_ref
from httprunner import exceptions, logger

def load_test_file(path):

    raw_content = load_file(path)
    loaded_content = None

    if isinstance(raw_content, dict):

        if "testcases" in raw_content:
            print("tetscase")
            # file_type: testsuite

            loaded_content = load_testsuite(raw_content)
            loaded_content["path"] = path
            loaded_content["type"] = "testsuite"
        elif "request" in raw_content:
            print("request")
            # file_type: api

            loaded_content = raw_content
            loaded_content["path"] = path
            loaded_content["type"] = "api"
        else:
            # invalid format
            logger.log_warning("Invalid test file format: {}".format(path))

    elif isinstance(raw_content, list) and len(raw_content) > 0:
        print("78")
        # file_type: testcase

        loaded_content = load_testcase(raw_content)
        loaded_content["path"] = path
        loaded_content["type"] = "testcase"

    else:
        # invalid format
        logger.log_warning("Invalid test file format: {}".format(path))

    return loaded_content
def load_teststep(raw_testinfo):

    if "api" in raw_testinfo:
        __extend_with_api_ref(raw_testinfo)


    # elif "func" in raw_testinfo:
    #     pass

    # reference testcase
    elif "testcase" in raw_testinfo:
        __extend_with_testcase_ref(raw_testinfo)

    # define directly
    else:
        pass
    print("6666")

    return raw_testinfo
pp='E:/HttpRunner/tests/data/demo_testcase_cli.yml'
# hh=load_test_file(pp)
# print(hh)
def load_yaml_file(yaml_file):
    """ load yaml file and check file content format
    """
    with io.open(yaml_file, 'r', encoding='utf-8') as stream:
        yaml_content = yaml.load(stream)

        return yaml_content

di=load_yaml_file(pp)
print(di)
for item in di:
    key, test_block = item.popitem()
    print(key)
    load_teststep(test_block)