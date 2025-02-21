class Solution(object):
    def differenceOfSums(self, n, m):
        not_div=[]
        div=[]
        for num in range(1,n+1):
            if num%m==0:
                div.append(num)
            else:
                not_div.append(num)
                
        return (sum(not_div)-sum(div))
                