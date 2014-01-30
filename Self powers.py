somme=0
i=1
for i in xrange(1,1000,1):
    somme+=pow(i,i)
somme=str(somme)
print(somme[-10:])
