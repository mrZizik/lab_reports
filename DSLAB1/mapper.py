#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import re
import os

special = ("Media:", "Special:", "Talk:", "User:", "User_talk:", "Project:", "Project_talk:", "File:", "File_talk:", "MediaWiki:", "MediaWiki_talk:", "Template:", "Template_talk:", "Help:", "Help_talk:", "Category:", "Category_talk:", "Portal:", "Wikipedia:", "Wikipedia_talk:")
extens = (".jpg," ".gif," ".png," ".JPG," ".GIF," ".PNG," ".txt," ".ico")

def readInput(file):
    for line in file:
        yield line.split()

def checkSpecial(word):
    splitted = word.split(":")
    return len(splitted)>1 and splitted[0]+":" not in special

reg = "-([0-9]+)-"

def main(separator='\t'):
    data = readInput(sys.stdin)
    filename = os.environ["mapreduce_map_input_file"]
    date = re.search(reg, filename).group(0)[1:-1]
    for words in data:
        if words[0] == "en" and checkSpecial(words[1]) and words[1][0].istitle() and words[1][len(words[1])-4:] not in extens:
            print '%s%s%s%s%s' % (words[1], separator, words[2], separator, date)



if __name__ == "__main__":
    main()