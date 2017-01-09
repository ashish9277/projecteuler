import math

roots=[]

roots1=[]

for x in range(1,1000):
    if math.sqrt(x)-int(math.sqrt(x))==0.0:
        roots.append(x)

print roots

for x in roots:
    for y in roots:
        for z in roots:
            if(math.sqrt(x)+math.sqrt(y)+math.sqrt(z)==1000.0):
                print x*y*z 
                break
#ab=500000-1000c


            
            
            


