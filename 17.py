wordsDict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                      8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                      14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                      18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
                      50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninty',100: "hundered", 1000: "thousand"}


word=""
for x in range(100,201):
    if(x<=20):
        word+=(wordsDict[x])
    
    elif 20<x<=99:
        y=x-(x%10)
        word+=(wordsDict[y])
        
        if(x%10!=0):
            word+=(wordsDict[x%10])
    elif 100<=x<=999:
        
        m=(x/100)

    
        word_hundred=(wordsDict[m]+wordsDict[100])
        word+=(word_hundred)
        n=x%100
        
        if(1<=n<=20):
            
            word+="and"+(wordsDict[n])
        elif(21<=n<=99):
            p=n-n%10
            word+="and"+(wordsDict[p])
            q=n%10
            if(n%10!=0):
                word+=(wordsDict[n%10])

#adding one thousand
word+="onethousand"
print word
print len(word)
