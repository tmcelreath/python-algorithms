import copy
import random
import operator
import math

# SELECTION SOR

def selection_sort(list):
    if not list: return []
    L = copy.copy(list)
    for i in range(len(L)):
        min = i
        for j in range(i+1, len(L)):
            if L[j] < L[min]:
                min = j
        swap(L, i, min)
    return L


# BUBBLE SORT

def bubble_sort(list):
    L = copy.copy(list)
    if not L: return []
    i = len(L)
    swapped = True
    while swapped:
        swapped = False
        for j in range(i):
            if j < (len(L)-1) and L[j] > L[j+1]:
                swap(L, j, j+1)
                swapped = True
        #print "Iteration ", i, " (swapped=" + str(swapped) + ") : ", L
        i = i-1
    return L


# SHELL SORT
def shell_sort(list):
    L = copy.copy(list)
    if not L: return []
    gap = len(L)//2
    while gap> 0:
        for start in range(gap):
            gap_insertion_sort(L, start, gap)
        gap = gap // 2
    return L

def gap_insertion_sort(L, start, gap):
    for i in range(start+gap, len(L), gap):
        current = L[i]
        position = i
        while position >= gap and L[position-gap] > current:
            L[position] = L[position-gap]
            position = position-gap
        L[position] = current


# QUICK SORT

def quick_sort(list, lo=0, hi=None):
    L = copy.copy(list)
    if L is None: return []
    if hi is None: hi = len(L)-1
    if lo >= hi: return L
    pivot = partition(L, lo, hi)
    #print 'pivot=', pivot
    quick_sort(L, lo, pivot-1)
    quick_sort(L, pivot+1, hi)
    return L

def partition(L, lo, hi):
    pivot = lo
    for i in xrange(lo+1, hi+1):
        if L[i] <= L[lo]:
            pivot += 1
            L[i], L[pivot] = L[pivot], L[i]
    L[pivot], L[lo] = L[lo], L[pivot]
    return pivot

# INSERTION SORT

def insertion_sort(list):
    L = copy.copy(list)
    for i in range(len(L)):
        j = i
        while j > 0 and L[j-1] > L[j]:
            L[j], L[j-1] = L[j-1], L[j]
            j -= 1
    return L

# HEAP SORT

def heap_sort(list, count=None):
    if list is None: return []
    L = copy.copy(list)
    if count is None: count = len(L)
    heapify(L, count)
    end = count - 1
    while end > 0:
        L[end], L[0] = L[0], L[end]
        end -= 1
        sift_down(L, 0, end)
    return L

def heapify(L, count):
    print 'heapify start: ', L
    start = (count-2)/2
    while start >= 0:
        sift_down(L, start, count-1)
        start -= 1
    print 'heapify end: ', L

def sift_down(L, start, end):
    root = start
    while (root * 2) + 1 <= end:
        child = (root * 2) + 1
        temp = root
        if L[temp] < L[child]:
            temp = child
        if child + 1 <= end and L[temp] < L[child+1]:
            temp = child + 1
        if temp == root:
            return
        else:
            swap(L, root, temp)
            root = temp

def sift_up(L, start, end):
    child = end
    while child > start:
        parent = (child-1)/2
        if L[parent] < L[child]:
            swap(L, parent, child)
            child = parent
        else:
            return

# MERGE SORT

def merge_sort(list):
    if list is None: return []
    L = copy.copy(list)
    if len(L) <=1: return L
    middle = len(L)/2
    left = L[:middle]
    right = L[middle:]
    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0
    while i<len(left) and j<len(right):
        if left[i]<right[i]:
            L[k] = left[i]
            i+=1
        else:
            L[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        L[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        L[k] = right[j]
        j+=1
        k+=1
    return L

def swap(L, index1, index2):
    L[index1], L[index2] = L[index2], L[index1]

# KNUTH SHUFFLE

def knuth_shuffle(list):
    if list is None: return []
    L = copy.copy(list)
    for i in range(len(L)):
        r = random.randrange(0, i+1)
        swap(L, i, r)
    return L

# CONVEX HULL - GRAHAM SCAN

def convex_hull(list):
    if list is None: return []
    L = copy.copy(list)
    """Returns points on convex hull of an array of points in CCW order."""
    L = sorted(L, key=operator.itemgetter(1))
    l = reduce(_keep_left, L, [])
    print l
    u = reduce(_keep_left, reversed(L), [])
    return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l

def turn(a, b, c):
    return cmp((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]),0)

def _keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != 1:
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull

# TESTS

def test():

    graph = []
    graph.append([2, 2])
    graph.append([2, 4])
    graph.append([1, -3])
    graph.append([2, -1])
    graph.append([4, 1])
    graph.append([0, 4])
    graph.append([-2, 2])
    graph.append([-3, -2])

    print convex_hull(graph)

    #L = [2,16,5,30,8,6,1,25,3]
    BEST_CASE  = [0,1,2,3,4,5,6,7,8,9]
    WORST_CASE = [9,8,7,6,5,4,3,2,1,0]
    AVERAGE_CASE = [0,9,1,8,2,7,3,6,4,5]
    #L = [8,9,7,6,5,4,3,2,1]


    print("SELECTION SORT: BEST CASE ", BEST_CASE)
    print selection_sort(BEST_CASE)
    print("SELECTION SORT: WORST CASE", WORST_CASE)
    print selection_sort(WORST_CASE)
    print("SELECTION SORT: AVERAGE CASE", AVERAGE_CASE)
    print selection_sort(AVERAGE_CASE)

    print("-------------------------")

    print("SHELL SORT: BEST CASE ", BEST_CASE)
    print shell_sort(BEST_CASE)
    print("SHELL SORT: WORST CASE", WORST_CASE)
    print shell_sort(WORST_CASE)
    print("SHELL SORT: AVERAGE CASE", AVERAGE_CASE)
    print shell_sort(AVERAGE_CASE)

    print("-------------------------")

    print "BUBBLE SORT: BEST CASE ", BEST_CASE
    print bubble_sort(BEST_CASE)
    print "BUBBLE SORT: WORST CASE", WORST_CASE
    print bubble_sort(WORST_CASE)
    print "BUBBLE SORT: AVERAGE CASE", AVERAGE_CASE
    print bubble_sort(AVERAGE_CASE)

    print("-------------------------")

    print("QUICK SORT: BEST CASE ", BEST_CASE)
    print quick_sort(BEST_CASE)
    print("QUICK SORT: WORST CASE", WORST_CASE)
    print quick_sort(WORST_CASE)
    print("QUICK SORT: AVERAGE CASE", AVERAGE_CASE)
    print quick_sort(AVERAGE_CASE)

    print("-------------------------")

    print("INSERTION SORT: BEST CASE ", BEST_CASE)
    print insertion_sort(BEST_CASE)
    print("INSERTION SORT: WORST CASE", WORST_CASE)
    print insertion_sort(WORST_CASE)
    print("INSERTION SORT: AVERAGE CASE", AVERAGE_CASE)
    print insertion_sort(AVERAGE_CASE)

    print("-------------------------")

    print("HEAP SORT: BEST CASE ", BEST_CASE)
    print heap_sort(BEST_CASE)
    print("HEAP SORT: WORST CASE", WORST_CASE)
    print heap_sort(WORST_CASE)
    print("HEAP SORT: AVERAGE CASE", AVERAGE_CASE)
    print heap_sort(AVERAGE_CASE)

    print("-------------------------")

    print("MERGE SORT: BEST CASE ", BEST_CASE)
    print merge_sort(BEST_CASE)
    print("MERGE SORT: WORST CASE", WORST_CASE)
    print merge_sort(WORST_CASE)
    print("MERGE SORT: AVERAGE CASE", AVERAGE_CASE)
    print merge_sort(AVERAGE_CASE)

    print("-------------------------")

    print("KNUTH SHUFFLE: BEST CASE ", BEST_CASE)
    print knuth_shuffle(BEST_CASE)
    print("KNUTH SHUFFLE: WORST CASE", WORST_CASE)
    print knuth_shuffle(WORST_CASE)
    print("KNUTH SHUFFLE: AVERAGE CASE", AVERAGE_CASE)
    print knuth_shuffle(AVERAGE_CASE)
test()