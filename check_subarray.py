arr = [4,2,-3,1,7]

#Summation of any sub array should return zero

# * Approach 1 :
'''
Time complexity  : O(n^2)
Space complexity : O(1)
'''

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        print(arr[i:j+1])
        if sum(arr[i:j+1]) == 0:
            print(arr[i:j+1], " : Zero raised when summing")
