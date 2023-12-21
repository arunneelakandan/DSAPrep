list_of_elem = [1,5,-1,7,55]
target = 6

#Addition of any pair should return the target value and find the count of pairs

# * Approach 1 :

count = 0

for i in list_of_elem:
    for j in list_of_elem:
        if i + j == target:
            count += 1
            break
        

print(count)
