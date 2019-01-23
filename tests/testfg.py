import os

from httprunner.loader import tests_def_mapping, project_mapping, load_testcase, load_file
rr={ 'testcase':{
                "name": "add product to cart",
                "testcase": "/path/to/testcase",
                "variables": {}
            }}

def extend_with_testcase_ref(raw_testinfo):
    """ extend with testcase reference
    """
    testcase_path = raw_testinfo["testcase"]

    if testcase_path not in tests_def_mapping["testcases"]:
        # make compatible with Windows/Linux
        testcase_path = os.path.join(
            project_mapping["PWD"],
            *testcase_path.split("/")
        )
        testcase_dict = load_testcase(load_file(testcase_path))
        tests_def_mapping[testcase_path] = testcase_dict
    else:
        testcase_dict = tests_def_mapping[testcase_path]
        print(testcase_dict)

    raw_testinfo["testcase_def"] = testcase_dict
extend_with_testcase_ref(rr)