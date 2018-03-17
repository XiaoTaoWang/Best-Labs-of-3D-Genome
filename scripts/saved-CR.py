# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:25:56 2018

@author: XiaoTao Wang
"""
import os, cPickle

infile = 'final-wos-records.isi'
libfile = 'saved-CR.pickle'
minline = 233907
maxline = 234007
minyear = 2007
state = ''

def parseCR(line, database):
    
    parse = line.strip().split()
    try:
        year = int(line.strip().split(',')[1])
        if ('DOI' in parse) and (year >= minyear):
            doi = parse[-1].strip('[]')
            database.add(doi.lower())
    except:
        pass

if os.path.exists(libfile):
    with open(libfile, 'rb') as source:
        database = cPickle.load(source)
else:
    database = set()

current = set()
count = 0
with open(infile, 'rb') as source:
    for line in source:
        count += 1
        if count > maxline:
            break
        if count < minline:
            continue
        tmp = line.lstrip()
        if len(tmp) == len(line):
            parse = line.strip().split()
            state = parse[0]
        
        if state == 'CR':
            parseCR(line, current)

if os.path.exists(libfile):
    tmp = current - database
    print len(tmp)
    for line in tmp:
        print line

database = database | current
with open(libfile, 'wb') as out:
    cPickle.dump(database, out, 2)
            
        