
# List-based algorithm

def dijkstra(G, v):
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}
    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_so_far)
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
    return final_dist

def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 1000000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])
    return best_node

# Heap-based algorithm

def dijkstra_heap(G,v):
    H = []
    control = {}
    # map of the current, non-finalized distances
    dist_so_far = {}
    # map of finalized distances.
    final_dist = {}
    # the origin node has a distance of zero
    dist_so_far[v] = 0
    # insert the root node into the heap
    insert_heap(H,(v,dist_so_far[v]),control)
    # keep going until the final list of nodes is the
    # same size as the original graph
    while len(final_dist) < len(G):
        w = shortest_dist_node(H,control)
        print w
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    insert_heap(H,(x,dist_so_far[x]),control)
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    update_heap(H,(x,dist_so_far[x]),control)
    return final_dist

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G

def shortest_dist_node(H,control):
    print "BEGIN shortest_dist_node"
    print "H, control = ", H, control
    node = 'undefined'
    if H[0] == H[len(H)-1]:
        print "H[0] == H[len(H)-1] - return H.pop()[0]"
        node = H.pop()[0]
    else:
        best_node = H[0]
        H[0] = H.pop()
        print "Call down_heapify on ", H, 0, control
        down_heapify(H,0,control)
        node = best_node[0]
    print "END shortest_dist_node: ", node
    return node


#def shortest_dist_node(dist):
#    best_node = 'undefined'
#    best_value = 1000000
#    for v in dist:
#        if dist[v] < best_value:
#            (best_node, best_value) = (v, dist[v])
#    return best_node

# Heap functions

def parent(i):
    return (i-1)/2
def left_child(i):
    return 2*i+1
def right_child(i):
    return 2*i+2
def is_leaf(L,i):
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i):
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def insert_heap(H,val,control):
    H.append(val)
    up_heapify(H,len(H)-1,control)

def update_heap(H,val,control):
    index = control[val[0]]
    H[index] = val
    down_heapify(H,index,control)

def up_heapify(L, i,control):
    if parent(i) >= 0:
        if L[i][1] < L[parent(i)][1]:
            L[i],L[parent(i)] = L[parent(i)],L[i]
            up_heapify(L,parent(i),control)
    control[L[i][0]] = i

def down_heapify(L, i,control):
    if is_leaf(L, i):
        control[L[i][0]] = i
        return
    if one_child(L, i):
        if L[i][1] > L[left_child(i)][1]:
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        control[L[i][0]] = i
        return
    if min(L[left_child(i)][1], L[right_child(i)][1]) >= L[i][1]:
        control[L[i][0]] = i
        return
    if L[left_child(i)][1] < L[right_child(i)][1]:
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        down_heapify(L, left_child(i),control)
        control[L[i][0]] = i
        return
    else:
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        down_heapify(L, right_child(i),control)
        control[L[i][0]] = i
        return

############
#
# Test



def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3),
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    print G

    dist = dijkstra_heap(G, a)

    print dist

    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)


test()



