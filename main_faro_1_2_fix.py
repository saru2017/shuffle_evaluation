from scipy.stats import entropy
import pandas as pd

def calc_diff_entropy(deck):
    ret = []
    for i in range(59):
        ret.append(abs(deck[i] - deck[i + 1]))

    pd_series = pd.Series(ret)

    counts = pd_series.value_counts()
    ret = entropy(counts)
    print(ret)
                   

def shuffle(deck):
    deck1 = deck[0: 30]
#    print(deck1)
    deck2 = deck[30: 60]
    ret = []
    for i in range(30):
        ret.append(deck2[i])
        ret.append(deck1[i])
    
    return ret
    


deck = []
for i in range(60):
    deck.append(i)

print(deck)

for i in range(30):
    deck = shuffle(deck)
    print(deck)
    calc_diff_entropy(deck)
