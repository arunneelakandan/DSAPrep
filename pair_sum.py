list_of_elem = [1,5,-1,7,55]
target = 6

#Addition of any pair should return the target value and find the count of pairs

# * Approach 1 :

count = 0

for i in range(len(list_of_elem)):
    for j in range(i+1,len(list_of_elem)):
        print(list_of_elem[i], list_of_elem[j])
        if list_of_elem[i] + list_of_elem[j] == target:
            count += 1
            
        

print(count)
