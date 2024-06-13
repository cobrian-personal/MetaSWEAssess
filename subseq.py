# ● Compute the length of the longest strictly increasing subsequence in a list. ○ Input: nums = [11, 5, 2, 5, 3, 7, 101, 18] 
# ○ Output: 4 
# ○ Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

#Time Complexity: O(n^2)
#Space Complexity: O(n)
def findMaxSubseq(arr):
    #Edge cases to start, empty arrays are 0, so are non arrays. If length is 1 then it is 1 by default. 
    if not arr: #falsy so also covers empty array
        return 0
    if len(arr) == 1:
        return 1
    
    #dp
    else:
        #create array temp where temp[i] is the length of the max subseq to that point
        length = len(arr)
        temp = [1] * length
        top = 1
        #populate array, optimize by keeping track of max subseq in place
        for i in range(1,length):
            for j in range(i):
                if arr[i] > arr[j]:
                    temp[i] = max(temp[i], temp[j] + 1)
                    if temp[i] > top:
                        top = temp[i]

        return top
    

test = [11, 5, 2, 5, 3, 7, 101, 18]
print(findMaxSubseq(test))
