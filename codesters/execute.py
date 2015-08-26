#!/usr/bin/python
import run, example, sys

def execute():
    if len(sys.argv) != 2:
        print 'You must supply a filename to run with the codesters library e.g. "python run.py example1.py"'
        exit()
    filename = sys.argv[1]

    run.run(filename)

def execute_example():
    if len(sys.argv) != 2:
        print 'You must supply a filename to run with the codesters library e.g. "python example.py example1.py"'
        exit()

    filename = sys.argv[1]
    example.run(filename)