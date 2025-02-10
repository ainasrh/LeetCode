class Solution(object):
    def mostWordsFound(self, sentences):
        leng=0
        arr=[]
        for sent in sentences:
            arr=sent.split()
            if leng<len(arr):
                leng=len(arr)
        return leng        
        