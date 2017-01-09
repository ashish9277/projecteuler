a=100

total=long(1)

while(a>1):
    total*=a
    a-=1

sum_digits=0

for x in str(total):
    sum_digits+=int(x)

print sum_digits
