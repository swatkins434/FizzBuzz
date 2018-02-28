#!/bin/python2 -tt
import sys
import argparse

class DictionaryBuild(argparse.Action):
    """
        Class to take command line arguments and build a dictionary from key-
        value pairs.
    """
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self.nargs = nargs
        super(DictionaryBuild, self).__init__(
            option_strings = option_strings,
            dest = dest,
            nargs = nargs,
            **kwargs
        )

    def __call__(self, parser, namespace, values, option_string=None):
        newDict = {}

        for keyval in values:
            key, val = keyval.split("=")
            try:
                newDict[int(key)] = val
            except ValueError as e:
                sys.stderr.write("key in key=value argument must be an integer literal, recieved \"{}\"\n".format(key))
                sys.exit()

        setattr(namespace, self.dest, newDict)

defaultWordDict = {
    3 : "fizz",
    5 : "buzz"
}

def getOutput(wordDict, currentNum):
    out = ""

    for i in wordDict.keys():
        if currentNum % i == 0:
            out += wordDict[i]

    if out == "":
        out += str(currentNum)

    return out

def parseArgs(args):
    parser = argparse.ArgumentParser(
        description = "Parse arguments from a comma-separated key-value list into a dict."
    )

    parser.add_argument(
        "--key_values",
        dest = "newDict",
        action = DictionaryBuild,
        nargs = "+",
        metavar = "key=val"
    )

    if len(args) == 1:
        return defaultWordDict
    else:
        return parser.parse_args(args[1:]).newDict

def main():
    wordDict = parseArgs(sys.argv)

    for i in xrange(1,100):
        print getOutput(wordDict, i)

if __name__ == '__main__':
    main()
