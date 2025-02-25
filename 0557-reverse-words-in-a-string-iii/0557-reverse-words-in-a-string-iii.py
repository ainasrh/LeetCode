class Solution(object):
    def reverseWords(self, s):
        arr=[]
        splited_value=s.split(" ")
        print(splited_value)
        for word in splited_value:
            arr.append(word[::-1])
        result=" ".join(arr)   
        return result   
        