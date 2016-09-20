import math

def prime(num):
    if num <= 1:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0 and num != i:
            return False
        elif num % i != 0 and num == int(math.sqrt(i)):
            return True
    return True

def monisen(no):
    count = 0
    num = 0
    while count < no:
        num += 1
        if prime(num):
            if(prime(2**num - 1)):
                count += 1
    return 2**num - 1


while True:
    c = input()
    if c == "q":
        print("Bye Bye")
    else:
        print(monisen(int(c)))
