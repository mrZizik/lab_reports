#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    for item, group in groupby(data, itemgetter(0)):
        try:
            print item, list(group)
            # total_count = sum(int(count) for item[0], count in group)
            # print "%s%s%d" % (item, separator, total_count)
        except ValueError:
            pass
if __name__ == "__main__":
    main()