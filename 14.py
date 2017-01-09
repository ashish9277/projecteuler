number=2



sequences=[]

while number<999999:
    no=number
    count=0
    #print no
    while(no!=1):
        if(no%2)==0:
            
            no/=2
            count+=1
        else:
            
            no=3*no+1
            count+=1    
    
    number+=1
    total_count=count+1
    
    sequences.append(total_count)    

major=0

for x in sequences:
    if x>major:
        major=x

print sequences[sequences.index(major)]        
   
