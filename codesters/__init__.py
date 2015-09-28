from environment import *
from shapes import *
from sprite import *
from manager import *
from execute import execute as codesters_run
import sys
import os

# This can't be the best way to do this
# We want to skip this part when we use the command line tool (e.g. codesters --example flappyfox.py)
# We want to run this part when we just use python to run the file (e.g. python flappyfox.py)
# when we just use python, the first arg is the python file, thus:
if sys.argv[0][-3:] == '.py':  # does the arg end in .py?
    loc = os.path.join(os.getcwd(), sys.argv[0])
    codesters_run(loc)

