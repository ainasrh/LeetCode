/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    num_len=nums.length
// console.log(num_len)



    for(i=0;i<=num_len;i++){
        if (!nums.includes(i)){
            return i
        }
    }
    }    
