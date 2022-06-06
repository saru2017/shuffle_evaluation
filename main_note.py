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
    
def main():
    deck = create_initial_deck()
    random.shuffle(deck)
    ret = calc_diff_entropy(deck)
    print(ret)
    
if __name__ == "__main__":
    main()
