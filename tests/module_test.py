import importlib
import os

from httprunner import validator

from httprunner import built_in


p='C:/Users/cheng/PycharmProjects/HttpRunner/tests/debugtalk.py'
def load_module_functions(module):

    module_functions = {}

    for name, item in vars(module).items():

        if validator.is_function(item):
            module_functions[name] = item
    return module_functions
def load_debugtalk_functions():

    imported_module = importlib.import_module("debugtalk")
    print(imported_module)
    return load_module_functions(imported_module)

