
#Surface area of box is:", surfaceArea(box) 2*l*w + 2*w*h + 2*h*l
#each line in imut file is formated lxwxh write code to read that file line by line
surfaceArea = 0
with open('2015\Day 2\input.txt', 'r') as f:
    boxs = f.readlines()
    q = 0
    for box in boxs:
        print(box)
        a = [int(x) for x in box.strip().split('x')]
        for r in sorted(a)[:2]:
            q += r*2
        q += a[0] + a[1] + a[2]
    print("Surface Area:", q)

