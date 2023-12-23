arr = [4,2,-3,1,7]

#Summation of any sub array should return zero

# * Approach 1 :
'''
Time complexity  : O(n^2)
Space complexity : O(1)
'''

def checkIfSumOfSubArraysIs0ExistOrNotV1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if sum(arr[i:j+1]) == 0:
                return True
            
print(checkIfSumOfSubArraysIs0ExistOrNotV1(arr=arr))

# * Approach 2 :
'''
Time complexity  : O(n)
Space complexity : O(n)
'''

def checkIfSumOfSubArraysIs0ExistOrNotV2(arr):
    n = len(arr)
    number_set = set()
    prefix_array = [0] * n
    for i in range(n):
        if i == 0:
            prefix_array[i] = arr[i]
        else:
            prefix_array[i] = arr[i] + prefix_array[i-1]
    
    for i in range(n):
        if prefix_array[i] in number_set:
            return True
        number_set.add(i)
        
    if 0 in number_set:
        return True
    else:
        return False



print(checkIfSumOfSubArraysIs0ExistOrNotV2(arr=arr))