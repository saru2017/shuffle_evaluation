from scipy.stats import entropy
import pandas as pd
import random

def calc_diff_entropy(deck):
    ret = []
    for i in range(59):
        ret.append(abs(deck[i] - deck[i + 1]))

#    print(ret)
    pd_series = pd.Series(ret)

    counts = pd_series.value_counts()
    ret = entropy(counts)
    print(ret)
                   

def shuffleA(deck):
    deck1 = deck[0: 30]
#    print(deck1)
    deck2 = deck[30: 60]
    ret = []
    for i in range(30):
        ret.append(deck2[i])
        ret.append(deck1[i])

    return ret

    
def shuffleB(deck):
    deck1 = deck[0: 40]
#    print(deck1)
    deck2 = deck[40: 60]
    ret = []
    for i in range(20):
        ret.append(deck2[i])
        ret.append(deck1[i])
    for i in range(20):
        ret.append(deck1[i + 20])
    
    return ret



deck = []
for i in range(60):
    deck.append(i)

print(deck)

for i in range(30):
    rnd = random.random()
    if i % 2 == 0:    
        deck = shuffleA(deck)
#        print(deck)
        calc_diff_entropy(deck)
    else:
        deck = shuffleB(deck)
#        print(deck)
        calc_diff_entropy(deck)
    
