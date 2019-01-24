from httprunner.loader import load_folder_content, load_folder_files, load_api_folder
from httprunner import exceptions, logger
import os
name_path='C:/Users/cheng/PycharmProjects/HttpRunner/tests/api'
r=load_folder_content(name_path)
print(r)
# print("=========")
# for api_file_path, api_items in r.items():
#     print(api_file_path)
#     print(type(api_items))
# t=load_folder_files(name_path)
# print(os.getcwd())
# print(t)
g=load_api_folder(name_path)
print(g)