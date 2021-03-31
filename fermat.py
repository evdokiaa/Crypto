import random

def fastmod(base , power , mod):
    result = 1
    while(power > 0):
        if(power%2 == 1):
            result = (result*base)%mod
            power = power -1
        power = power/2
        base  = (base*base)%mod
    return result

def fermat_test(n,k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(1,n-1)

        if fastmod(a , n-1, n) != 1:
            return False 
    return True


trials = 10
number = int(input())

if fermat_test(number,trials):
    print("is prime")
else:
    print("is not prime")


