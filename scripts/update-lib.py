# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 16:20:40 2018

@author: XiaoTao Wang
"""

import cPickle, os

infile = 'lastest-wos-records.isi'
libfile = 'saved-CR.pickle'

if os.path.exists(libfile):
    with open(libfile, 'rb') as source:
        database = cPickle.load(source)
        
current = set()
with open(infile, 'rb') as source:
    for line in source:
        tmp = line.lstrip()
        if len(tmp) == len(line):
            parse = line.strip().split()
            if parse[0] == 'DI':
                try:
                    current.add(parse[1])
                except:
                    pass

database = database | current
with open(libfile, 'wb') as out:
    cPickle.dump(database, out, 2)