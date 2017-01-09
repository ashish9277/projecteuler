sequences=[]
sequences_factors=[]

factors=1

no=1
total=0

count=1
while count<500:
    total+=no
    if(total>500):
        sequences.append(total)

    #generating factors and adding the count to list
    count=0
    for x in range(1,total+1):
        if total%x==0:
           count+=1
    sequences_factors.append(count)
    print count
    no+=1

    

print sequences
print sequences_factors
