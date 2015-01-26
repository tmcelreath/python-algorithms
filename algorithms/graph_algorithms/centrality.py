import csv
from operator import itemgetter

actors = []

def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for(node1, node2, node3) in tsv:
        make_link(G, node1, node2 + " (" + node3 + ")")
    return G

def make_link(G, node1, node2):
    if node1 not in G:
        actors.append(node1)
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

G = read_graph("file.tsv")

#print G

def get_centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)

def get_max_centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return (max(distance_from_start.values())+0.0)

results = []

for actor in actors:
    results.append([actor, get_centrality(G, actor)])

results = sorted(results, key=itemgetter(1))

for i in range(30):
    print results[i]
