from environment import *
from shapes import *
from sprite import *
from manager import *
from execute import execute as codesters_run
import sys
import os

if sys.argv[0]:
    loc = os.path.join(os.getcwd(), sys.argv[0])
    print loc
    codesters_run(loc)

