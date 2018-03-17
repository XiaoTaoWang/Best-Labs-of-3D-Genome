# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 19:33:55 2018

@author: XiaoTao Wang
"""

nwb = 'work-network.nwb'
author_file = 'domestic-researcher.txt'
outfile = 'med-network.nwb'

authors = set([line.rstrip().split('\t')[0] for line in open(author_file)])
with open(outfile, 'wb') as out:
    with open(nwb, 'rb') as source:
        for line in source:
            parse = line.rstrip().split('\t')
            if len(parse) < 2:
                out.write(line)
            else:
                if parse[0].isdigit() and (not parse[1].isdigit()):
                    tmp = parse[1].split('" ')
                    name = tmp[0].strip('"').lower()
                    w, c = tmp[1].split()
                    if not name in authors:
                        w = c = '-1'
                    newval = ' '.join([w, c])
                    newrec = '" '.join([tmp[0], newval])
                    newstr = '\t'.join([parse[0], newrec])+'\n'
                    out.write(newstr)
                else:
                    out.write(line)