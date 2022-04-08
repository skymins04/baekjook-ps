from hashlib import sha1
from multiprocessing import Process
def findHash(id,s,e):
    f = open("sha1_"+str(id)+".txt", 'w')
    for i in range(s,e): 
        h = str(i)+"salt_for_you"
        tmp = h
        for j in range(500):
            h = sha1(h.encode('utf-8')).hexdigest()
        f.write(tmp+" - "+h+"\n")
    f.close()
    return
    
if __name__ == "__main__":
    start, end = 10000000,100000000
    th1 = Process(target=findHash, args=(1, start, end//8))
    th2 = Process(target=findHash, args=(2, start+end//8, start+(end//8)*2))
    th3 = Process(target=findHash, args=(3, start+(end//8)*2, start+(end//8)*3))
    th4 = Process(target=findHash, args=(4, start+(end//8)*3, start+(end//8)*4))
    th5 = Process(target=findHash, args=(5, start+(end//8)*4, start+(end//8)*5))
    th6 = Process(target=findHash, args=(6, start+(end//8)*5, start+(end//8)*6))
    th7 = Process(target=findHash, args=(7, start+(end//8)*6, start+(end//8)*7))
    th8 = Process(target=findHash, args=(8, start+(end//8)*7, end))
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
    th6.start()
    th7.start()
    th8.start()
    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()
    th6.join()
    th7.join()
    th8.join()