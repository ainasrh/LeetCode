class Solution(object):
    def subtractProductAndSum(self, n):
        num=str(n)
        product=1
        total=0
        for i in range(0,len(num)):
            product*=int(num[i])
            total+=int(num[i])
        return product-total 
