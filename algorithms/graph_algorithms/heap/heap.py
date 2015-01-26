
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