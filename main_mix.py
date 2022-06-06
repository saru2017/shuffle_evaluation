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
    

def faro_shuffle_1_2(deck):
    deck1 = deck[0: 30]
#    print(deck1)
    deck2 = deck[30: 60]
    ret = []
    for i in range(30):
        ret.append(deck2[i])
        ret.append(deck1[i])
    
    return ret


def hindu_shuffle(deck, num):
    if 60 % num != 0:
        print("hindu_shuffle error: you can't use %d", num)
        exit(1)

    num_per_parts = 60 // num
#    print(num_per_parts)

    ret = []
    for i in range(num):
        for j in range(num_per_parts):
            ret.append(deck[(num - i - 1) * num_per_parts + j])
    
    return ret

def faro_1_2_shuffle(deck):
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

#print(deck)

deck = deeler_shuffle(deck, 10)
calc_diff_entropy(deck)

for i in range(29):
    if i % 4 == 0:    
        deck = hindu_shuffle(deck, 3)
        calc_diff_entropy(deck)
    elif i % 4 == 1:    
        deck = faro_1_2_shuffle(deck)
        calc_diff_entropy(deck)
    elif i % 4 == 2:    
        deck = faro_1_2_shuffle(deck)
        calc_diff_entropy(deck)
    elif i % 4 == 3:    
        deck = faro_1_2_shuffle(deck)
        calc_diff_entropy(deck)
    else:
        print("impossible!!!")
        exit(1)
    
    #print(deck)
