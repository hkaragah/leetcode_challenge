class Solution(object):
    def lemonadeChange(self, bills):
        five=0
        ten=0

        for i in bills:
            if i==5:
                five+=1
            elif i==10:
                if five>0:
                    ten+=1
                    five-=1 
                else:
                    return False
            elif i==20: 
                if five>0 and ten>0:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
        
