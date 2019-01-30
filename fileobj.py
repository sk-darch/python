#! /usr/bin/python
import os

fname = ''
fsize = 0

for file in os.listdir('.'):
    fname = file
    if fsize == os.path.getsize(fname):
        print 'The zero byte file is \t%s\t%d\tByte' % (fname, fsize)
