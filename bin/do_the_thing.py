#!/usr/bin/env python

import sys
sys.path.insert(0,"lib/")
from parseproblem import Parser

filename = sys.argv[1]

print("filename entered is ", filename)

Parser.parse(filename)
