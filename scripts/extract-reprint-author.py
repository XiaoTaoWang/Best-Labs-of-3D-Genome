# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:45:13 2018

@author: XiaoTao Wang
"""

infile = 'final-wos-records.isi'
outfile = 'out_author_info.txt'

def parseID(block, lib, ID='RI'):
    
    string = ''
    state = 0
    for line in block:
        if line.startswith(ID):
            state = 1
            string += (line[3:].rstrip() + ' ')
        else:
            tmp = line.lstrip()
            if (len(tmp)<len(line)) and state:
                string += (tmp.rstrip() + ' ')
            elif len(tmp)==len(line):
                state = 0
    records = string.strip().split(';')
    for r in records:
        if r.strip():
            parse = r.split('/')
            author = parse[0].lstrip()
            lib[author] = parse[1].rstrip()
        
    return lib

def pair_name_and_abbr(block):
    
    names = []
    abbr = []
    state = 0
    for line in block:
        if line.startswith('AU'):
            state = 1
            abbr.append(line[3:].rstrip())
        elif line.startswith('AF'):
            state = 2
            names.append(line[3:].rstrip())
        else:
            tmp = line.lstrip()
            if (len(tmp)<len(line)) and (state==1):
                abbr.append(line.strip())
            elif (len(tmp)<len(line)) and (state==2):
                names.append(line.strip())
            elif len(tmp)==len(line):
                state = 0
    Map = dict(zip(abbr, names))
    
    return Map

def retrieve_name(abbr, Map, ID):
    
    name = Map[abbr]
    if name in ID:
        return ID[name]
    else:
        for n in ID:
            if n in name:
                return ID[n]

authors = {}
block = []
with open(infile, 'rb') as source:
    for line in source:
        if (not line.startswith('FN')) and (not line.startswith('VR')) and (line.strip()):
            block.append(line.rstrip())
        if line.startswith('ER'):
            assert block[0].startswith('PT')
            temp = {} # author's information within current record
            for m in block:
                if m.startswith('PY'):
                    year = int(m.split()[1])
                if m.startswith('RP'):
                    parse = m[3:].split(';')
                    for r in parse:
                        author = r.split('(reprint author)')[0].strip()
                        country = r.split(',')[-1].strip().rstrip('.')
                        temp[author] = [country]
            name_Map = pair_name_and_abbr(block)
            lib = parseID(block, {}, 'RI')
            lib = parseID(block, lib, 'OI')
            for name in temp:
                ID = retrieve_name(name, name_Map, lib)
                temp[name].append(ID)
            for name in temp:
                if not name in authors:
                    authors[name] = [year] + temp[name]
                else:
                    if year > authors[name][0]:
                        authors[name] = [year] + temp[name]
            block = []

# author name, last published year, country, id, total citation, nsf, nih, erc
template = '%s\t%d\t%s\t%s\t%d\t%d\t%d\t%d\n'
with open(outfile, 'wb') as out:
    for name in sorted(authors):
        info = (name,) + tuple(authors[name]) + (0, 0, 0, 0)
        out.write(template % info)
        
                    