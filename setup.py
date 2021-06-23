""" CaesarBot """
#################################
__author__ = "Alexander Ryzhov"
__email__ = "thed4rkof.gmail.com"
__version__ = "0.2.0-proto.2"
#################################

import os
import sys
from subprocess import Popen, PIPE, run
# from src.controllers import server


if __name__ == "__main__":
    # source1: https://stackoverflow.com/questions/12605498/how-to-use-subprocess-popen-python
    # source2: https://stackoverflow.com/a/16180450/14748231
    process = run("export-env-vars.sh", shell=True, check=True, timeout=10)
    process.wait() # Wait for process to complete.

    # iterate on the stdout line by line
    # for line in process.stdout.readlines():
    #     print(line)