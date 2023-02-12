class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        p=[]
        for i in tokens:
            if i=="+" or i=="-" or i=="*" or i=="/" :
                a=p.pop()
                b=p.pop()
                p.append(int(eval(str(b)+i+str(a))))
            else:
                p.append(i)
        return int(p[0]);
