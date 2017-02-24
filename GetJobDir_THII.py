'''
This is used to get the directory of each running jobs with the job ID.

It works well in Tianhe II(Guangzhou) and should works as well in else with some modifications, though I didn't test it.

by Linus Deng-Hui Xing
'''

### Version 1 ###
import os
os.system('squeue|grep R > Queue')

A = len(open('Queue','r').readlines())
#print A  ## Number of lines in this file. FOR DEBUGGING

B = open('Queue','r').readlines()
#print B  ## make the file to list. FOR DEBUGGING

i = 1
while i < A :
    C = B[i].strip() # get the ith line and remove the whitespace at left
    D = C.split()  #split into three coordinate list
    #print D[0]  FOR DEBUGGING
    E = 'find -name *' + D[0] + '*'
    #print E  FOR DEBUGGING
    print str(i) + '--' + str(D[0]) + ': '
    os.system(E)
    i=i+1

print 'There are ' + str(A-1) + ' jobs.'

os.system('rm Queue')



### Version 2 BETTER ###
import os
os.system('squeue > Queue')

A = len(open('Queue','r').readlines())
B = open('Queue','r').readlines()

i = 1
while i < A :
    C = B[i].strip()
    D = C.split()
    E = 'scontrol show job ' + D[0] + ' > infotmp'
    os.system(E)
    F = len(open('infotmp','r').readlines())
    G = open('infotmp','r').readlines()
    print str(i) + '--' + str(D[0]) + ': '
    print G[F-2].strip('\n')
    i=i+1
    os.system('rm infotmp')

print 'There are ' + str(A-1) + ' running jobs.'

os.system('rm Queue')
