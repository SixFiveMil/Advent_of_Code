with open('2024\Day 1\input.txt') as f:
    l, r = zip(*[map(int, line.split()) for line in f if len(line.split()) == 2])
print(sum(abs(x - y) for x, y in zip(sorted(l), sorted(r))))
