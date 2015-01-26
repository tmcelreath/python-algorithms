#!/usr/bin/python
import csv
import time

def read_graph(file_name):
    tsv = csv.reader(open(file_name), delimiter=',')
    G = []
    for(name, gender, count) in tsv:
        G.append([name, gender, int(count)])
    return G

namesG = read_graph("yob1995.txt")

name1 = ["", "", 0]
name2 = ["", "", 0]

for record in namesG:
    if record[1] == 'F':
        if record[2] > name1[2]:
            name2 = name1
            name1 = record
        elif record[2] > name2[2]:
            name2 = record

print name1
print name2