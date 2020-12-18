import argparse
import math
import sys
from typing import Any, Dict

from pancalc import version


def safe_eval(expr: str, variables: Dict[str, Any]):
    """
    Perform the evaluation
    :param expr:
    :return:
    """
    d = {}
    # add all methods in math module
    for name in dir(math):
        if name.startswith("_"):
            continue
        d[name] = getattr(math, name)
    # add all variables
    for k, v in variables.items():
        d[k] = v

    return eval(expr, d, d)


def parse_args(args):
    parser = argparse.ArgumentParser(prog="pancalc", description="""
    Calculator written in python. small project allowing you to perform some easy calculation from command line.
    Named derived from pancake (github project suggestion name) 
    """
    )
    parser.add_argument("-V", "--variable", action="append", nargs=2, default=[], help="""
    Varaible avaialble during calculation
    """)
    parser.add_argument("expression", type=str, nargs="+", help="""
    Expression to compute
    """)
    parser.add_argument("-v", "--version", action="store_true", help="""
    Show progam version and exits
    """)

    return parser.parse_args(args)


def main():
    try:
        options = parse_args(sys.argv[1:])

        if options.version:
            print(version.VERSION)
            sys.exit(0)

        expr = ' '.join(options.expression)
        variable = {x[0]: x[1] for x in options.variable}

        output = safe_eval(
            expr=expr,
            variables=variable
        )
        print(output)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
