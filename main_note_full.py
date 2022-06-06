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
    return ret

def create_initial_deck():
    deck = []
    for i in range(60):
        deck.append(i)
    return deck

def faro_1_2_shuffle(deck):
    deck1 = deck[0: 30]
    deck2 = deck[30: 60]
    ret = []
    for i in range(30):
        ret.append(deck2[i])
        ret.append(deck1[i])
    return ret

def faro_1_3_up_shuffle(deck):
    deck1 = deck[0: 40]
    deck2 = deck[40: 60]
    ret = []
    for i in range(20):
        ret.append(deck1[i])
        
    for i in range(20):
        ret.append(deck2[i ])
        ret.append(deck1[i + 20])
        
    return ret
    
def faro_1_3_down_shuffle(deck):
    deck1 = deck[0: 40]
    deck2 = deck[40: 60]
    ret = []
    for i in range(20):
        ret.append(deck2[i])
        ret.append(deck1[i])
        
    for i in range(20):
        ret.append(deck1[i + 20])
        
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

def hindu_shuffle(deck, num):
    if 60 % num != 0:
        print("hindu_shuffle error: you can't use %d", num)
        exit(1)

    num_per_parts = 60 // num
    ret = []
    for i in range(num):
        for j in range(num_per_parts):
            ret.append(deck[(num - i - 1) * num_per_parts + j])
    
    return ret

def main():
    deck = create_initial_deck()
    print(deck)
    deck = deeler_shuffle(deck, 13)
    print(deck)
    deck = faro_1_3_up_shuffle(deck)
    print(deck)
    deck = faro_1_3_down_shuffle(deck)
    print(deck)
    deck = hindu_shuffle(deck, 5)
    print(deck)
    ret = calc_diff_entropy(deck)
    print(ret)
    
if __name__ == "__main__":
    main()
