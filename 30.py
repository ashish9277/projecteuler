#getting sum of the numbers that can be written as a sum of fifth powers of their digits.

import math
from datetime import datetime
startTime = datetime.now()

powers=[]

for i in range(2,354294):
    total =0
    for j in str(i):
        total += int(j)**5


    if total == i:
        powers.append(i)

print (sum(powers))

print ('Time for execution : ' , datetime.now() - startTime)
