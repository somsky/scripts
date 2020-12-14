#!/usr/bin/env python

# author: somsky
# generate title blocks to separate different sections
# in config files.
# example below:
#
#+=------------=+ ~~~~~~~~~~~~~~~ +=-------------=+#
#+=------------=+ example section +=-------------=+#
#+=------------=+ ~~~~~~~~~~~~~~~ +=-------------=+#

from math import floor
import argparse

s1 = '+='
s2 = '-'
s3 = '=+ '
s4 = '~'

def genHeader(title: str, headerLen: int, commentChar: str) -> str:
    s2Len = floor((headerLen - (len(commentChar) + len(s1) + len(s3)) * 2 - len(title)) / 2)
    genHalfLine = lambda pad: commentChar + s1 + s2 * (s2Len + 1 if pad else s2Len) + s3
    middleLineLeft = genHalfLine(False)
    middleLineRight = genHalfLine(len(title) % 2 != 0)[::-1]
    middleLine = middleLineLeft + title + middleLineRight
    outerLine = middleLineLeft + s4 * len(title) + middleLineRight
    header = '{}\n{}\n{}'.format(outerLine, middleLine, outerLine)
    return header

def main():
    parser = argparse.ArgumentParser(description='Generater three line-long separators for headers in config files')
    parser.add_argument('-c', '--comment-char', default='#', required=True, help='The comment char/string, printed on every line of the header block')
    parser.add_argument('-l', '--line-len', default=80, type=int, help='The length of the header block')
    parser.add_argument('-t', '--headers', nargs='+', required=True, help='A list of the headers to generate header blocks for')
    args = parser.parse_args()

    for header in args.headers:
        print(genHeader(header, args.line_len, args.comment_char) + '\n')

if __name__ == '__main__':
    main()
