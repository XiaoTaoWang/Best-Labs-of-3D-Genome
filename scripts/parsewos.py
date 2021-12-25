
def startswith_blank(line):

    test = line.lstrip()
    if test[0] == line[0]:
        return False
    else:
        return True

def WOS_records(infil):

    by_pubs = []
    correspondings = {}
    with open(infil, 'r') as source:
        for line in source:
            if line.startswith('FN') or line.startswith('VR') or (not line.strip()):
                continue
            if not startswith_blank(line):
                label = line.split()[0]

            if line.startswith('PT '):
                authors = []
                fulls = []
                title = []
                abstract = []
                RP_records = set()
                cited_times = 0
                published_year = 2021
            if line.startswith('AU '):
                authors.append(line.strip().split('AU ')[1])
            elif line.startswith('AF '):
                fulls.append(line.strip().split('AF ')[1].upper())
            elif line.startswith('TI '):
                title.append(line.strip().split('TI ')[1])
            elif line.startswith('AB '):
                abstract.append(line.strip().split('AB ')[1])
            elif line.startswith('RP '):
                parse = line.rstrip()[3:].split(';')
                for r in parse:
                    tmp = r.split('(corresponding author)')[0].strip()
                    RP_records.add(tmp)
                RP_records = list(RP_records)
            elif line.startswith('Z9 '):
                cited_times = int(line.rstrip().split()[1])
            elif line.startswith('PY '):
                published_year = line.rstrip().split()[1]
            else:
                if label=='AU':
                    authors.append(line.strip().split('AU ')[0])
                elif label=='AF':
                    fulls.append(line.strip().split('AF ')[0].upper())
                elif label=='TI':
                    title.append(line.strip().split('TI ')[0])
                elif label=='AB':
                    abstract.append(line.strip().split('AB ')[0])
            
            if line.rstrip()=='ER':
                title = ' '.join(title)
                abstract = ' '.join(abstract)
                authors_map = dict(zip(authors, fulls))
                authors_map_reverse = dict(zip(fulls, authors))
                current = {'authors':authors_map, 'authors_reverse':authors_map_reverse,
                        'title':title,
                        'abstract':abstract,
                        'cited times': cited_times,
                        'published year': published_year}
                reprint_authors = set()
                for n in RP_records:
                    reprint_authors.add(authors_map[n])
                    correspondings[authors_map[n]] = n
                current['reprint authors'] = reprint_authors
                by_pubs.append(current)
                
    #correspondings = list(correspondings)
    
    return by_pubs, correspondings


isi_fil = 'wos-records.isi'

by_pubs, correspondings = WOS_records(isi_fil)