
#include <stdio.h>

int main()
{
    int i,k,size; 
    int arr[10];
    int max = 0;
    
    printf("enter the size array: ");
    scanf("%d",&size);
    
    printf("enter the array: ");
    
    for(i=0;i<size;i++){
        scanf("%d",&arr[i]);  
    }
    
    printf("enter the value of k: ");
    scanf("%d",&k);
    if(k>size){
        return 0;
    }
    
    for(i=0;i<k;i++){
        max = (arr[i] > max) ? arr[i]: max ;
        
    }
    
    printf("%d ",max); // Calculate the 1st k-ele max 
    
    
    
    for(i=k ; i<size ;i++){
        if(arr[i-k] == max){
            max = 0;
            
            for(int j=i-k+1;j<=i;j++){
                max = (arr[j] > max) ? arr[j]: max ;
            }
            
        }
        max = (arr[i] > max) ? arr[i]: max ;
        printf("%d ",max);
    }
    

    return 0;
}
