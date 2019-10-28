import sys
from collections import defaultdict

def name_from_nwb(infil):

    names = []
    with open(infil, 'r') as source:
        for line in source:
            parse = line.rstrip().split('\t')
            if parse[0].isdigit() and (not parse[1].isdigit()):
                names.append(parse[1].strip('"').upper())
    names.append('Mirny, L'.upper())
    nameset = set(names)

    return nameset, names

# original co-author network in NWB
nwb = sys.argv[1]
# full records from web of science
isi = sys.argv[2]

num_of_works = defaultdict(int)
times_cited = defaultdict(int)

nameset, names = name_from_nwb(nwb)
block = []
with open(isi, 'r') as source:
    for line in source:
        if (not line.startswith('FN')) and (not line.startswith('VR')) and (line.strip()):
            block.append(line.rstrip())
        if line.startswith('ER'):
            assert block[0].startswith('PT')
            for m in block:
                if m.startswith('Z9'):
                    cite = int(m.split()[1])
                hits = set()
                if m.startswith('RP'):
                    parse = m[3:].split(';')
                    for r in parse:
                        author = r.split('(reprint author)')[0].strip().upper()
                        if author in nameset:
                            hits.add(author)
                for author in hits:
                    num_of_works[author] += 1
                    times_cited[author] += cite
            block = []

for n in names:
    print('{0}\t{1}\t{2}'.format(n, num_of_works[n], times_cited[n]))



