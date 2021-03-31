import numpy as np 

message='HI ALICE, IN ODER FOR OUR MESSAGES TO BE SAFE, WE HAVE TO USE A KEY WITH SAME LENGTH AS THE LENGTH OF THE MESSAGE'
key1='CRYPTOGRAPHY'
shift=4

key2=''
for i in key1:
    key2 += chr((ord(i)-65+shift)%26+65)

print(key2)

decrypted=''

counter=0
for i in message:
    if (ord(i)>64 and ord(i)<91):
        tmp = (ord(i)-65 + ord(key2[counter%12])-65) %26 + 65
        decrypted += chr(tmp)
        counter+=1
    else:
        decrypted+=i

print(decrypted)
