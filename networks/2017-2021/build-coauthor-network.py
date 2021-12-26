import networkx as nx
from collections import defaultdict

def initial_coauthors(by_pubs, correspondings):
    
    G = nx.Graph()
    edges = defaultdict(int)
    for pub in by_pubs:
        authors = pub['authors_reverse']
        for i in authors:
            for j in authors:
                if (i<j) and (i in correspondings) and (j in correspondings):
                    edges[(i, j)] += 1
    for e in edges:
        G.add_edge(e[0], e[1], weight=edges[e])
    
    deg = nx.closeness_centrality(G, normalized=True)
    ndeg = {}
    for n in deg:
        k = correspondings[n]
        if k in ndeg:
            ndeg[k] = max(ndeg[k], deg[n])
        else:
            ndeg[k] = deg[n]
    
    # assign node attrs: total cited times and number of works
    # only counted works as corresponding authors
    for n in G:
        G.node[n]['cited'] = 0
        G.node[n]['nworks'] = 0
        G.node[n]['centrality'] = deg[n]
    
    for pub in by_pubs:
        authors = pub['reprint authors']
        for i in authors:
            if i in G:
                G.node[i]['cited'] += pub['cited times']
                G.node[i]['nworks'] += 1
    
    # filter by degree, cited times, or number of works
    rnodes = []
    for n in G:
        if (G.node[n]['cited'] > 50) and (G.node[n]['nworks'] > 4):
            continue
        rnodes.append(n)
    G.remove_nodes_from(rnodes)
    
    degrees = G.degree(list(G))
    rnodes = []
    for n in degrees:
        if (degrees[n] >= 1):
            continue
        rnodes.append(n)
    G.remove_nodes_from(rnodes)
    '''
    # only outputs the largest components
    components = nx.connected_component_subgraphs(G)
    graph = None
    maxn = 0
    for g in components:
        if len(g) > maxn:
            graph = g
            maxn = len(g)
    
    # abbr name graph
    author_map = {n:correspondings[n] for n in graph}
    graph = nx.relabel_nodes(graph, author_map, copy=True)
    
    nx.write_gexf(graph, 'largest-component.gexf')
    '''
    graph = G
    author_map = {n:correspondings[n] for n in graph}
    graph = nx.relabel_nodes(graph, author_map, copy=True)
    nx.write_gexf(graph, '2017-2021.coauthors.gexf')

    # sorted
    metrics = []
    for n in graph:
        metrics.append((graph.node[n]['cited'], graph.node[n]['nworks'], ndeg[n], n))
    metrics.sort(reverse=True)
    
    return graph, metrics, degrees