number=600851475143
factor=0

a=0

def isprime(no):
    prime=True
    for j in range(2,no):
        if(no%j==0):
            prime=False
    return prime

while a < number:
    #print a, isprime(a)
    if isprime(a):
        try:
            if(number%a==0):
                factor=a
                print factor
        except:
            print a
        
    a+=1
#print factor
