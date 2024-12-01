
#Surface area of box is:", surfaceArea(box) 2*l*w + 2*w*h + 2*h*l
#each line in imut file is formated lxwxh write code to read that file line by line
surfaceArea = 0
with open('2015\Day 2\input.txt', 'r') as f:
    boxs = f.readlines()
    for box in boxs:
        print(box)
        l,w,h = box.split('x')
        surfaceArea += 2*int(l)*int(w) + 2*int(w)*int(h) + 2*int(h)*int(l)
        #find the smallest side of the box then add it to the total area.
        surfaceArea += min( (int(l)*int(w)), ((int(w)*int(h))), ((int(h)*int(l))))
        print("Surface Area:", surfaceArea)

