### add T or F based on fractional z-coordination###
## By Linus Deng-Hui Xing   ##

print 'If you are under linux system ,then happy computing!\n'
print 'If you are under windows system, modify the line 17 as the tips in script.\n'
X = raw_input('Input the origin POSCAR format file name:\n')
Thresh = float(raw_input('Input the z-height threshhold for fixed optimization:\n'))

A=len(open(X,'r').readlines())
#print A  ## Number of lines in this file

B=open(X,'r').readlines()
#print B  ## make the file to list

i=8 ## starting line of coordination

while i < A-1: 
## TIP: if the last line is blank, here are 2 cases:
## 1. Under linux system ,everything is fine.
## 2. Under Windows system, use A rather than A-1 above
    C = B[i].strip() # get the ith line and remove the whitespace at left
    D = C.split()  #split into three coordinate list
    F = float(D[len(D)-1].rstrip('\n'))  ## remove the \n of the third and turn the Z-coord from string to number
    if F > Thresh:
        B[i] = B[i].rstrip('\n') + ' T T T\n'
    else: B[i] = B[i].rstrip('\n') + ' F F F\n'

    i=i+1
## add T or F

B[7] = 'Selective Dynamics \n' + B[7]

G = X + '_modified'
open(G,'w').close() # clear the file to write
for n in B:
    open(G,'a+').write(n)

#'01_modified.vasp'.close()