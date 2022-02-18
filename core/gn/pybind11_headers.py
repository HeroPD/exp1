from __future__ import print_function

import subprocess
import sys

includes = subprocess.check_output(['python', '-m', 'pybind11', '--includes'])
includes_str = includes.decode()
# offset = 0
# while (i := includes_str.find('-I')) != -1:
#   path = includes_str[0:i]
#   includes_str = includes_str[i+2:]
#   if len(path) > 0:
#     print('-I' + path)
# print('-I' + includes_str)

while (i := includes_str.rfind('-I')) != -1:
  print(includes_str[i:].strip())
  includes_str = includes_str[:i]
  # print(includes_str)