import random
n=int(input())
sv=0
lv=9
for i in range(n):
  if i==0:
    sv=0
    lv=9
  else:
    lv=(lv*10)+9
    if(i==1):
      sv=10
    else:
      sv=sv*10

print(random.randint(sv, lv))
