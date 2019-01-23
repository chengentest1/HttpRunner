import importlib
import os
# from httprunner import validator
# testcase_cli_path = "tests/data/demo_testcase_cli.yml"
# if validator.is_testcase_path(testcase_cli_path):
#     print("34")
from httprunner import validator
from httprunner.loader import load_dot_env_file

# r=load_dot_env_file('C:/Users/cheng/PycharmProjects/HttpRunner/tests/.env')
# print(r)
# print(os.getcwd())
import io
# dot_env_path='C:/Users/cheng/PycharmProjects/HttpRunner/tests/.env'
# env_variables_mapping={}
# with io.open(dot_env_path, 'r', encoding='utf-8') as fp:
#     for line in fp:
#         # maxsplit=1
#         if "=" in line:
#             valu=line.split("=",1)
#
#             variable, value = line.split("=", 1)
#         elif ":" in line:
#             variable, value = line.split(":", 1)
#             print(valu.strip())
#         env_variables_mapping[variable.strip()] = value.strip()
# print(env_variables_mapping)
#
# def set_os_environ(variables_mapping):
#     """ set variables mapping to os.environ
#     """
#     for variable in variables_mapping:
#         print(variable)
#         os.environ[variable] = variables_mapping[variable]
# set_os_environ(env_variables_mapping)
imported_module = importlib.import_module("debugtalk")
print(imported_module)
def load_module_functions(module):
    module_functions = {}

    for name, item in vars(module).items():
        if validator.is_function(item):
            module_functions[name] = item

    return module_functions
u=load_module_functions(imported_module)
print(u)