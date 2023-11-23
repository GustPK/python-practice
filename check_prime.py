# Enter number: 100
# 100 is not a prime number.

# Enter number: 139
# 139 is a prime number.

def check_prime(n):
    for i in range(2,n):
        if n%i!=0:
            return True
        else:
            return False
        
n = int(input("Enter Number: "))
x = check_prime(n)
if x == True:
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")