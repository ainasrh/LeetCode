class Solution(object):
    def truncateSentence(self, s, k):
        result=[]
        splited=s.split(" ")
        # print(splited)

        for i in range(k):
            result.append(splited[i])

        return " ".join(result)
 