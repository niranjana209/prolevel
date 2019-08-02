from itertools import combinations
rrr,ttt=input().split()
ttt=int(ttt)
bun=[]
sal=len(rrr)-ttt
cake=combinations(rrr,sal)
for i in list(cake):
  bun.append("".join(i))
print(min(bun))
