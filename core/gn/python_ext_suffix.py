from __future__ import print_function

import subprocess
import sys

includes = subprocess.check_output(['python3-config', '--extension-suffix'])
print(includes.decode().strip())