#!/usr/bin/python
import csv
import time


def mean(L):
    return (0.0 +max(L))/len(L)

print mean([2,3,2,3,2,4])

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter=',')
    G = {}
    for(node1, node2) in tsv:
        make_link(G, node1, node2)
    return G

marvelG = read_graph("hero-network.csv")

#print(marvelG)

def get_path(G, v1, v2):
    distance_from_start = {}
    open_list = [v1]
    distance_from_start[v1] = [v1]
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + [neighbor]
                if neighbor == v2:
                    return distance_from_start[v2]
                open_list.append(neighbor)
    return False


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
    return (sum(distance_from_start.values())+0.0)/len(distance_from_start)


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


from_node = "RESTON, CLIVE"
to_node = "FIRESTAR/ANGELICA JO"

path = get_path(marvelG, from_node, to_node)
print path

for node in marvelG:
    centrality = get_max_centrality(marvelG, node)
    print (node, centrality)