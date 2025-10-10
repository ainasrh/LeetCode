class Solution(object):
    def longestCommonPrefix(self, strs):

        common = ""

        if len(strs) == 0:
            return common

        test_word = strs[0]
        
    

        for index,char in enumerate(test_word):
        

            for i in range(1,len(strs)):

                if index >= len(strs[i]):
                    return common 

                if strs[i][index] != char:
                    return common
            
            common = common + char
        
        
    
        return common
        



