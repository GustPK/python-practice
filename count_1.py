import random

ls = []
c = 1
count = 0

while c<=10:
    num = random.randrange(1,11)
    ls.append(num)
    c+=1

for i in ls:
    if i==1:
        count+=1

print(ls)
print(count)