list_of_elem = [1,5,-1,7,55]
target = 6

#Addition of any pair should return the target value and find the count of pairs

# * Approach 1 :
'''
Time complexity  : O(n^2)
Space complexity : O(1)
'''

count = 0

for i in range(len(list_of_elem)):
    for j in range(i+1,len(list_of_elem)):
        if list_of_elem[i] + list_of_elem[j] == target:
            count += 1
            
        

print(count)


# * Approach 2 :
'''
Time complexity  : O(n)
Space complexity : O(n)
'''

count = 0

check_list = []

for i in list_of_elem:
    if target - i in check_list:
        count += 1
    check_list.append(i)

print(count)

# * Approach 3 :
'''
Time complexity  : O(nlogn)
Space complexity : O(1)
'''

count=0

list_of_elem = sorted(list_of_elem)

l,r = 0,len(list_of_elem) - 1

while l < r:
    val = list_of_elem[l] + list_of_elem[r]
    if val > target:
        r = r -1
    elif val == target:
        count += 1
        l = l + 1
        r = r - 1

print(count)