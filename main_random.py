from scipy.stats import entropy
import pandas as pd
import random

def calc_diff_entropy(deck):
    ret = []
    for i in range(59):
        ret.append(abs(deck[i] - deck[i + 1]))

    pd_series = pd.Series(ret)

    counts = pd_series.value_counts()
    ret = entropy(counts)
    print(ret)
    return ret
                   

def faro_shuffle(deck):
    deck1 = deck[0: 30]
#    print(deck1)
    deck2 = deck[30: 60]
    ret = []
    for i in range(30):
        ret.append(deck2[i])
        ret.append(deck1[i])
    
    return ret

    
def deeler_shuffle(deck,  unit):
    tmp = []
    for i in range(unit):
        tmp.append([])


    for i in range(60):
        tmp[i % unit].append(deck[i])

    ret = []
    for i in range(unit):
        for card in tmp[i]:
            ret.append(card)
    
    return ret
    


deck = []
for i in range(60):
    deck.append(i)

print(deck)

sum = 0.0
trial = 10000
for i in range(trial):
    random.shuffle(deck)
    sum += calc_diff_entropy(deck)

print("end")
print(sum / trial)
