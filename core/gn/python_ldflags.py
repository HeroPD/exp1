from __future__ import print_function

import subprocess
import sys

def rfind_key(val):
  key1_i = val.rfind('-framework')
  key2_i = val.rfind('-l')
  key3_i = val.rfind('-L')
  max = key2_i if key1_i < key2_i else key1_i
  max = key3_i if max < key3_i  else max
  return max

libs = subprocess.check_output(['python3-config', '--ldflags'])
libs_str = libs.decode()
while (i := rfind_key(libs_str)) != -1:
  if libs_str[i:].strip().startswith('-L'):
    print(libs_str[i:].strip())
  libs_str = libs_str[:i]