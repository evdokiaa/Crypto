import numpy as np

crypt = open('krypto.txt' , 'r')
IC_max=0

correct_key_value=100
correct_key_length=0

encrypted=''
for k in range(5,12):
    keyLength=k
    counter=0
    IC=np.zeros(keyLength)
    frequency=np.zeros(26*keyLength)
    while True:
        c=crypt.read(1)
        if not c:
            break
        frequency[(ord(c)-ord('A'))+(counter%keyLength)*26]+=1
        counter+=1


    rowLength = int((counter-1)/keyLength)

    for j in range(0,keyLength):
        for i in range(0,26):
            IC[j]+=frequency[i+26*j]*(frequency[i+26*j]-1)
        if ( j <  (counter-1)%keyLength ):
            IC[j]/=rowLength*(rowLength+1)
        else:
            IC[j]/=rowLength*(rowLength-1)

    IC_mean=0
    for i in range(0,keyLength):
        IC_mean += IC[i]
    if (abs(0.065 - IC_mean/keyLength) < correct_key_value):
        correct_key_length = keyLength
        correct_key_value = abs(0.065 - IC_mean/keyLength)
    #print('mean value for key length ',keyLength ,':', IC_mean/keyLength)
    #print('correct',correct_key_length)

    crypt.seek(0,0)

english_frequency =np.array([8.12, 1.49 , 2.71 , 4.32 , 12.702 , 2.3 , 2.015, 5.92, 6.996 , 0.15 , 0.77, 3.98 , 2.61 , 6.95 , 7.5 , 1.9 , 0.09 , 5.98 , 6.32 , 9.056 , 2.76 , 0.978,  2.36,0.15,1.97,0.075]) 
keyLength = correct_key_length
frequency=np.zeros(26*keyLength)
counter=0
while True:
    c=crypt.read(1)
    if not c:
        break
    frequency[(ord(c)-ord('A'))+(counter%keyLength)*26]+=1
    counter+=1

key=np.zeros(keyLength)
key_2=np.zeros(keyLength)
for i in range(0,keyLength):
    max_product=0
    max2=0
    for j in range(0,26):
        tmp=0
        for k in range(0,26):
            tmp+=frequency[i*26+(j+k)%26]*english_frequency[k]
        if (tmp > max_product):
            max2=max_product
            max_product = tmp 
            key_2[i]=key[i] 
            key[i]=j
            
        elif (tmp<max_product and tmp>max2):
            max2=tmp
            key_2[i]=j
    
    print( 'difference from second possible key: ' , max_product - max2 ) 
    print( 'key' , i , ':' ,key[i] ,'2o kleidi' , key_2[i] ) 

crypt.seek(0,0)

i=0


print('Decrypted message', end=' ')
for counter in range(-1 , min(keyLength , 10)):
    temp_key=key.copy()
    if (counter!=-1) :
        temp_key[counter] = key_2[counter]
    print('with key: ' , temp_key )
    while True:
        c=crypt.read(1)
        if not c:
            break 
        else:

            out = ord(c)-temp_key[i%keyLength]
            if (out  < 65):
                out+=26 
            print(chr(int(out)),end="")
        i+=1
    print('')
    crypt.seek(0,0)

    



