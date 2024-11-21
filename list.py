list = [[1,2,3],[4,5,6]]
list[0].append(7)
list[1].remove(4)


d2 = sum(list[1])
d1 = sum(list[0])
list[0].append(d1)
list[1].append(d2)
print(list)
