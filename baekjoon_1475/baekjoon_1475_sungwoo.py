a = input()
card = [0] * 10
for i in a:
    if i == '9' or i == '6':
        if card[6] == card[9]:
            card[6] += 1
        else:
            card[9] += 1
    else:
        card[int(i)] += 1
print(max(card))