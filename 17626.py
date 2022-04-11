from math import floor

def fourSqures(n):
    tmp=0
    for i in range(floor(n**0.5), -1, -1):
        tmp += i**2
        if tmp==n:
            print(1)
            return
        elif i!=0:
            for j in range(i, -1, -1):
                tmp += j**2
                if tmp==n:
                    print(2)
                    return
                elif j!= 0:
                    for k in range(j, -1, -1):
                        tmp += k**2
                        if tmp==n:
                            print(3)
                            return
                        elif k!=0:
                            for g in range(k, -1, -1):
                                tmp += g**2
                                if tmp==n:
                                    print(4)
                                    return
                                tmp -= g**2
                        tmp -= k**2
                tmp -= j**2
        tmp -= i**2
fourSqures(int(input()))