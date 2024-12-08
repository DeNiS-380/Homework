my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
while x < len(my_list):
    ag = my_list[x]
    x += 1
    if ag == 0:
        continue
    elif ag < 0:
        break
    print(ag)

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ret = (my_list[::-1])
c = 0
while c < len(ret):
    lj = ret[c]
    c += 1
    if lj == 0:
        continue
    elif lj <= 0:
        break
    print(lj)
