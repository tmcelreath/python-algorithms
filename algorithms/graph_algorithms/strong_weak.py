import csv
from operator import itemgetter

characters = []
results = {}

def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for(node1, node2) in tsv:
        make_link(G, node1, node2, 1)
    return G

def make_link(G, node1, node2, weight):
    if node1 not in G:
        characters.append(node1)
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

G = read_graph("marvel.tsv")
charG = {}

for character in characters:
    for book in G[character]:
        for book_character in G[book]:
            if character > book_character:
                key = character + " | " + book_character
                if results.has_key(key):
                    results[key][0] += 1
                else:
                    results[key] = [1, character, book_character]


for key in results.keys():
    make_link(charG, results[key][1], results[key][2], results[key][0])

print charG['SPIDER-MAN/PETER PAR']



#winner = results.keys()[0]
#list_results = []
#for key in results.keys():
#    list_results.append([key, results[key]])

#list_results = sorted(list_results, key=itemgetter(1), reverse=True)

#for i in range(50):
#    print list_results[i]
