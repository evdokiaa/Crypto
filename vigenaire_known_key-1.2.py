import numpy as np

encrypted = 'Nd Dhy. A dcmgv yk ccob xsieewa svptdwn os ptp Kqg, url gz wazwry vaffu jj tmgzogk tsi os xyextrm lmb hildcmzu. B plsgp plpz oq npw dci Otikigkb usklxc.Egi ahr lrdrd zh g rcr qg wvox zwx hglpsqzw bxrunubydo os wpextrm cgb cik?'

encrypted = encrypted.upper()

key = 'CRYPTOGRAPHY'
key_length = 12

for shift in range (0,26):
    for i in range (0,12):
        tmp = (ord(key[i]) + shift + 13) % 65
    counter = 0
    decrypted = ''
    for i in encrypted: 
        if (i ==' ' or i == '?' or i==',' or i=='.'):
            decrypted += i 
        else:
           tmp = ((ord(i)-65) -(ord(key[counter%12])+shift-65))  % 26
           if (tmp < 0):
               tmp += 26
           tmp += 65
           decrypted += chr(tmp)
           counter+=1
    print('for shift:' , shift)
    print(decrypted)





