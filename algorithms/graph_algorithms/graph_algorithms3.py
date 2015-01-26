
#    animal          speed  weight lifespan brain mass
animals = [
    ("dog",          46,     35,     13,     280     ),
    ("elephant",     30,   3500,     50,    6250     ),
    ("frog",          5,      0.5,    8,       3     ),
    ("hippopotamus", 45,   1600,     45,     573     ),
    ("horse",        40,    385,     30,     642     ),
    ("human",        27,     80,     78,    2000     ),
    ("lion",         50,    250,     30,     454     ),
    ("mouse",         8,      0.025,  2,       0.625 ),
    ("rabbit",       25,      4,     12,      40     ),
    ("shark",        26,    230,     20,      92     ),
    ("sparrow",      16,      0.024,  7,       2     )
]

def importance_rank(items, weights):
    names = [item[0] for item in items]
    scores = [sum([a*b for (a,b) in zip(items[i][1:], weights)]) for i in range(len(items))]
    results = zip(scores, names)
    results.sort()
    return results

answer = importance_rank(animals, (51,0.4,2,0.1))

print answer

L = [21, 43, 48, 49, 50, 51, 75, 77, 79, 87, 93]
L.sort()
print ( (L[len(L)/2]) + (L[0] + L[len(L)-1]/2.0) ) / 2