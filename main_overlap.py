import random

deck = []
for i in range(15):
    deck.append(i)
    deck.append(i)
    deck.append(i)
    deck.append(i)

try_count = 1000
sum = 0

for j in range(try_count):
    random.shuffle(deck)

    print(deck)

    count = 0
    pre = -1
    for i in range(60):
        if pre == deck[i]:
            print("found!")
            count += 1

        pre = deck[i]


    sum += count

print(sum / try_count)
