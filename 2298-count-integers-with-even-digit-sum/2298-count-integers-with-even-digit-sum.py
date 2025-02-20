class Solution(object):
    def countEven(self, num):
        even_digit_num=[]

        for n in range(1,num+1):
            if n >9:
                splited_digit=[int(d) for d in str(n)]
                if sum(splited_digit)%2==0:
                    even_digit_num.append("".join(map(str,splited_digit)))
            else:
                if n %2==0:
                    even_digit_num.append(n)
                    
        result=[int(x) for x in even_digit_num]
        return len(result)