# python complete code 

def search(a,t):
    l = 0
    r = len(a)-1
                  
    while l <= r:
        mid = (l+r) // 2
        
        if a[mid] == t:
            return mid
        
        if a[mid] >= a[l]:
            if a[l] <=  t < a[mid]:  #left sorted array
                r = mid-1
            else:
                l=mid+1
        
        else:
            if a[mid] <  t <= a[r]:  #check for right sorted array
                l = mid+ 1
            else:
                r = mid-1
                
    return -1  #not found  
  
    
a = [4, 5, 6, 7, 0, 1, 2]
t = 0
result = search(a, t)

if result != -1:
    print(f"Target {t} found at index {result}")
else:
    print(f"Target {t} not found in the array")    


                  #---------------------------or-------------------------#


  class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
                  
        while l <= r:
            mid = (l+r) // 2
        
            if nums[mid] == target:
                return mid
        
            if nums[mid] >= nums[l]:
                if nums[l] <=  target < nums[mid]:  #check for left sorted array
                    r = mid-1
                else:
                    l=mid+1

            else:
                if nums[mid] <  target <= nums[r]:  #check for right sorted array
                    l = mid+ 1
                else:
                    r = mid-1
                
        return -1 
        
    
    
    

            
