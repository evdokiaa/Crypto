import string
import rsa
from queue import Queue 
import threading


def oracle(oracle_queue, attack_queue, priv):
        while(True):
                a = oracle_queue.get()
                oracle_queue.task_done()
                if (a==-1):
                        break
                decr = rsa.core.decrypt_int(a , priv.d, pub.n )
                attack_queue.put(decr % 2 == 0)



def attack(oracle_queue, attack_queue, pub, enc_message):
        
        enc_2 = rsa.core.encrypt_int(2 , pub.e, pub.n)
        lower = 0 
        upper = pub.n 
        c = enc_message
        while ( lower < upper ) :
                c = (enc_2 * c) % pub.n
                oracle_queue.put(c)
                if (attack_queue.get()):
                        upper = ( upper + lower)  // 2
                else:
                        lower = ( upper + lower )  // 2
                attack_queue.task_done()
                print(lower, upper)
        oracle_queue.put(-1)
        print(lower)

        



        



if __name__ == "__main__":
        pub, priv = rsa.newkeys(2048)

        oracle_queue = Queue()
        attack_queue = Queue()

        enc_message = rsa.core.encrypt_int(23478039342 , pub.e, pub.n)
 
        o = threading.Thread(target = oracle, args = (oracle_queue , attack_queue, priv))
        a = threading.Thread(target = attack, args = (oracle_queue, attack_queue,pub, enc_message))

        o.start()
        a.start()

        o.join()
        a.join()



        

        

        
        
