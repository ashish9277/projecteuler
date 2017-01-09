def isprime(no):
    prime=True
    for j in range(2,no):
        if(no%j==0):
            prime=False
    return prime


total=0
no=1

while no<2000000:
    no+=1
    if(isprime(no)):
        total+=no

print total
    
