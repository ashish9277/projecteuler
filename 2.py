a=1
b=2
sum=0

even_sum=0

#4000000
while(b<=4000000):
    if(b%2==0):
        even_sum+=b
    sum=a+b
    a=b
    b=sum

    

print even_sum
    
