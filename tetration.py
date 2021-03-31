from sympy.ntheory.factor_ import totient

def fastmod(base, power, mod):
    result = 1
    while(power>0):
        if(power%2 == 1):
            result = (result*base)%mod
            power = power -1
        power = power/2
        base = (base*base)%mod
    return result

def tetration(x,y,mod):
    if mod == 1:
        return 0 
    if y == 0:
        return 1 
    return fastmod(x , tetration(x,y-1,totient(mod)) , mod )

x=1707
y=1783
mod = 10**16 
a = tetration(x,y,mod)
print(a)


