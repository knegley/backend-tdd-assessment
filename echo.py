#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Kyle Negley"


# import sys
import argparse


def create_parser():
    """Returns namespace object"""
    parser = argparse.ArgumentParser(
        description="prints input and includes string methods", usage="echo.py[-h][-u][-l][-t] text")
    parser.add_argument(
        "-l", "--lower", action="store_true", help="lower case all characters")
    parser.add_argument(
        "-u", "--upper", action="store_true", help="upper case all characters")
    parser.add_argument(
        "-t", "--title", action="store_true", help="makes text titlecase")
    parser.add_argument(
        "text", help="echo.py <text> to print <text>")

    return parser.parse_args()


def text_manipulater(command):
    args = create_parser()
    return{
        "lower": lambda: args.text.lower(),
        "upper": lambda: args.text.upper(),
        "title": lambda: args.text.title()
    }.get(command, lambda: args.text)()


def echo_Output():
    args = create_parser()
    # print(args.__dict__)

    for arg, value in args.__dict__.items():
        if arg != "text" and value:
            return(text_manipulater(arg))
    return text_manipulater(None)

    # if args.lower is not None:
    #     print(args)
    #     print(lamba_dict["lower"]())

    # print(lambda_dict.get(None, lambda: args.text)())

    # if args.lower:
    #     print(lambda_dict["lower"]())
    # elif args.upper:
    #     print(lambda_dict["upper"]())
    # elif args.title:
    #     print(lambda_dict["title"]())
    # else:
    #     print(lambda_dict.get(None, lambda: args.text)())


def main():
    """Implementation of echo"""
    print(echo_Output())


if __name__ == '__main__':
    main()
