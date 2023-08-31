#leetcode pno : 153 (medium)
#minimum in rotated sorted array

#python code

def minEle(arr):
    l  = 0 
    r = len(arr)-1
    
    while l<r:
        mid = (l+r) // 2
        
        if(arr[mid] > arr[r] ):
            l = mid + 1
        else:
            r = mid 
            
    return arr[l]


arr = [ 8 , 9 , 10 , 6 , 7 ]

result = minEle(arr)
print('the minimum element is',result)
