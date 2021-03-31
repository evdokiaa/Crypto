import math
import random

#calculates (base^power)%mod using the repeated squaring algorithm  
def fastmod(base , power , mod):
    result = 1
    while(power > 0):
        if(power%2 == 1):
            result = (result*base)%mod
            power = power -1
        power = power//2
        base  = (base*base)%mod
    return result

#takes a continued fraction and calculates value of fraction
def fraction(a0 , list):
    numerator = 1
    denominator = list[-1]
    for d in list[-2::-1]:                           
        temp = denominator
        denominator = d * denominator + numerator
        numerator = temp
    numerator = numerator + a0 * denominator
    numerator = numerator//math.gcd(numerator,denominator)
    denominator = denominator//math.gcd(numerator,denominator)
    return denominator

#calculates private key d of rsa, known that it is small 
def rsa(public_N , public_e):
  m = 8
  e , N = public_e, public_N
  c = fastmod(m, e ,N) 
  listoula = []
  first = 1
  den = 0 
  while True:
    listoula.append( e // N )
    e = e % N
    e , N = N , e
    if ( not first):
      den = fraction(listoula[0], listoula[1:])
      if (fastmod(c, den, public_N) == m):
        return den
    first = 0
  
def factorisation_N( N, e, d):
  k = d*e - 1
  while ( True ) :
    g = random.randint( 2, N-1)
    t = k 
    while ( t % 2 == 0):
      t = t // 2
      x = fastmod(g, t, N)
      if (x > 1):
        y = math.gcd(x-1, N) 
        if (y > 1):
          p = y 
          q = N // p
          return p,q
      
  






N  = 0xb844986fc061a2c0baf528a960e208832625f725fa09bfe1ac4c15bccad6031d09f8f37bf00520bb59480070e59441ed34b7e3d118db67a035ac4b46a055a4963df4af0baa4dfab3f98566f2c09f7c83ffec458b63931ce311241c98614659172cfe9f21ecc7d7241aea1ae1e88f796568f49a645ffce12c87629e8783462e5dbeb52a85c95
e = 0x369d89b820f2450462f21b02d91bcec9de528805bb22123d843fcd776ad57025980f1c3359d45d65c9a9e363a0a51eaf8873b3dc2ffab45787c5e86bacbf2a6bbca5106828eec95cb2ea534fa2e64d672a2c69e21589f84daa54a164db28ade473e8009972279cd89c5afaf1b312914256dac666e7f824db23f33a9867616898686a1fe63c5 

d = rsa(N,e)
p,q = factorisation_N(N,e,d)
print('The private key d is:' , d)
print('p' , p , q)











  

