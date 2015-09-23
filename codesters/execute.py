#!/usr/bin/python
import run
import example
import argparse


def execute(filename):
    run.run(filename)


def execute_example(filename):
    example.run(filename)


def runner():
    parser = argparse.ArgumentParser(
        usage="\nThis command runs codesters files. \
        A default command would be as follows:\n\n codesters <options> filename\n",
        description="Offline codesters library",
        epilog="",
        )
    parser.add_argument(
        "filename",
        help="REQUIRED ARGUMENT: the codesters python file in the current directory to run",
        metavar="filename")
    parser.add_argument(
        "-e",
        "--example",
        help="runs one of the example files from the codesters library (e.g. basketball.py)",
        action="store_true")

    args = parser.parse_args()

    if args.example:
        execute_example(args.filename)
    else:
        execute(args.filename)
