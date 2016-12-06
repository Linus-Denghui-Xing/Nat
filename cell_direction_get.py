### get the lattice vector in POSCAR for pyscf###
## By Linus Deng-Hui.Xing  ##
import numpy as np

print 'Use POSCAR format as the input\n'
X = raw_input('Input the origin POSCAR format file name:\n')

B=open(X,'r').readlines()

i = 2
Latt_vec = []

while i < 5:
    C = B[i].strip() # get the ith line and remove the whitespace at left
    D = C.split()  #split into three coordinate list
    k = 0
    while k < 3:
        D[k] = float(D[k])
        k +=1
    Latt_vec.append(D)
    i=i+1

Latt_vec = np.transpose(Latt_vec)
print Latt_vec,'\n',

h = np.eye(3)*3.5668
print h
