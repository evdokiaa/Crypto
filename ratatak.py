
def fastmod(base, power, mod):
    result = 1
    while(power>0):
        if(power%2 == 1):
            result = (result*base)%mod
            power = power -1 
        power = power/2
        base = (base*base)%mod
    return result 

Z = int(input())
M = int(input()) 

exp1 = 1998000
exp2 = 1000

a = fastmod(exp1, exp2 , 4*pow(10,M-1))
p = fastmod( Z , 4*pow(10,M-1)+a , pow(10,M))

print('Ο μικρός Ραττατακιανός θα χρειαστεί', p, 'πλεξοδευτερόλεπτα')
