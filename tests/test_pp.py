import os
#test



# y=os.getcwd()
# print(y)
from httprunner.loader import locate_file
path_debug="C:/Users/cheng/PycharmProjects/HttpRunner/tests/debugtalk.py"
y=locate_file(path_debug,"debugtalk.py")
print(y)
d=os.path.isdir(path_debug)
print(d)
t=os.path.isfile(path_debug)
print(t)
