ls = []

while True:
    num = int(input())
    if num < 0:
        break
    ls.append(num)

print(ls)
ls.sort()
print(ls)
ls.reverse()
print(ls)