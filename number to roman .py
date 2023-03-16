dic = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
answer = ''
num = 20
while num > 0:
    for i in dic:
        if dic[i] <= num:
            answer = answer + i
            num = num - dic[i]
            break
        
print(answer)
