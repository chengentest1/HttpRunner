from httprunner.loader import load_tests, load_project_tests, locate_debugtalk_py, tests_def_mapping

pa='C:/Users/cheng/PycharmProjects/HttpRunner/tests/data/demo_testcase_cli.yml'
# y=locate_debugtalk_py(pa)
# print(y)

u=load_project_tests(pa)
tests_def_mapping
print(tests_def_mapping)

# e=load_tests(pa)
# print(e)