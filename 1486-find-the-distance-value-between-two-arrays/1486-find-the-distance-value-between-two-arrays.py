class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        greater_value=[]
        count=0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                diff=abs(arr1[i] - arr2[j])
                if diff <= d:
                    count+=1
                    break;
                
                    
                    
            
        return len(arr1)-count       
        