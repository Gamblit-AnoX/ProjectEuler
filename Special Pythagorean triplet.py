from math import sqrt
i=1
j=1
for i in xrange(1,1000,1):
    for j in xrange(1,1000,1):
        if((sqrt(i*i+j*j)==int(sqrt(i*i+j*j))) and i+j+sqrt(i*i+j*j)==1000):
            print(i*j*sqrt(i*i+j*j))
            break
    
