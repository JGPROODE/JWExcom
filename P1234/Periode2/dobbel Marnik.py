import time
import math
from itertools import permutations 

def vereenvoudig(u):
    if u[1] < 0:
        u[0] = -u[0]
        u[1] = -u[1]
    g = math.gcd(u[0],u[1])
    if g == 0:
        return ([0,0])
    else:
        return ([u[0]//g,u[1]//g])

def fplus(u,v):
    return vereenvoudig([u[0]*v[1]+u[1]*v[0],u[1]*v[1]])

def fmin(u,v):
    return vereenvoudig([u[0]*v[1]-u[1]*v[0],u[1]*v[1]])

def fmaal(u,v):
    return vereenvoudig([u[0]*v[0],u[1]*v[1]])

def fdeel(u,v):
    return vereenvoudig([u[0]*v[1],u[1]*v[0]])

def fop(u,v,op):
    if op == 0:
        return fplus(u,v)
    if op == 1:
        return fmin(u,v)
    if op == 2:
        return fmaal(u,v)
    if op == 3:
        return fdeel(u,v)

def flippo(Q):
    a = Q[0]
    b = Q[1]
    c = Q[2]
    d = Q[3]
    r = Q[4]
    perms = permutations([a,b,c,d]) 
    # disc = (a-b)*(a-c)*(a-d)*(b-c)*(b-d)*(c-d)
    lipe = list(perms)
    lipe.sort()
    ok = 0
    for elt in lipe:
        if ok == 0:
            for u1 in range(4):
                r1 = fop([elt[0],1],[elt[1],1],u1)
                for u2 in range(4):
                    r2a = fop([elt[2],1],r1,u2)
                    r2b = fop(r1,[elt[2],1],u2)
                    r2c = fop([elt[2],1],[elt[3],1],u2)
                    for u3 in range(4):
                        r3a = fop([elt[3],1],r2a,u3)
                        r3b = fop([elt[3],1],r2b,u3)
                        r3c = fop(r2a,[elt[3],1],u3)
                        r3d = fop(r2b,[elt[3],1],u3)
                        r3e = fop(r1,r2c,u3)
                        if (r3a[0] == r) & (r3a[1] == 1):
                            ok += 1
                        if (r3b[0] == r) & (r3b[1] == 1):
                            ok += 1
                        if (r3c[0] == r) & (r3c[1] == 1):
                            ok += 1
                        if (r3d[0] == r) & (r3d[1] == 1):
                            ok += 1
                        if (r3e[0] == r) & (r3e[1] == 1):
                            ok += 1
    return ok

Dobbelsteen1 = (1, 2, 3, 4, 5, 6)
Dobbelsteen2 = (1, 2, 3, 4, 5, 6)
Dobbelsteen3 = (1, 2, 3, 4, 5, 6)
Dobbelsteen4 = (1, 2, 3, 4, 5, 6)

Dobbelsteen1 = (1, 2, 3, 4, 5, 6)
Dobbelsteen2 = (7, 8, 9, 10, 11, 12)
Dobbelsteen3 = (13, 14, 15, 16, 17, 18)
Dobbelsteen4 = (19, 20, 21, 22, 23, 24)

Dobbelsteen1 = (1, 2, 3, 4, 5, 6)
Dobbelsteen2 = (2, 4, 6, 8, 10, 12)
Dobbelsteen3 = (3, 6, 9, 12, 15, 18)
Dobbelsteen4 = (4, 8, 12, 16, 20, 24)

print(Dobbelsteen1, Dobbelsteen2, Dobbelsteen3, Dobbelsteen4, ":")

t0 = time.process_time()
niet_geslaagd = 0
for n in range(1,101):
    if n % 10 == 0: print (n, "% gedaan")
    for a1 in Dobbelsteen1:
        for a2 in Dobbelsteen2:
            for a3 in Dobbelsteen3:
                for a4 in Dobbelsteen4:
                    Q = [a1,a2,a3,a4,n]
                    f = flippo(Q)
                    if f == 0:
                        niet_geslaagd +=1
t1 = time.process_time()
print(round(100-niet_geslaagd/1296,2),"% door", \
      Dobbelsteen1, Dobbelsteen2, Dobbelsteen3, Dobbelsteen4)
T = t1-t0
M = math.floor(T / 60)
print("Rekentijd:", M, "minuten", T - 60*M, "seconden")
