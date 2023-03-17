dic = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}

k = input("input your string")
string = k[0]+k
answer = 0
n = len(string)-1
while n >= 1:
    
    if dic[string[n]] > dic[string[n-1]]:
        answer = answer + dic[string[n-1]+string[n]]
        n = n - 2
    else:
        answer = answer + dic[string[n]]
        n = n-1
        
print(answer)
