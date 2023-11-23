number = []

while True:
    num = int(input())
    if num < 0:
        break
    number.append(num)

print("Min:", min(number))
print("Max:", max(number))