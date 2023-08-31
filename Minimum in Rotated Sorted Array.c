//pno : 153
// Minimum in Rotated Sorted Array


#include <stdio.h>

int minEle(int arr[],int size){
    int l = 0;
    int r = size-1;
    
    while(l<r){
        int mid = (l+r)/2;   //3 4 5 1 2
        if(arr[mid] > arr[r])
        {
            l = mid+1;
        }
        else
        {
            r = mid;
        }
    }
    return arr[l];
}

int main()
{
    int arr[] = { 5, 6 , 7 , 8 , 0 , 1 , 2 , 3 , 4 };
    int size = 9;
    int result = minEle(arr,size);
    printf("the minimum element is  %d",result); 
}
