
 code in c :
 
#include <stdio.h>

int searchEle(int arr[3][4],int t,int rows,int cols);

int main()
{
    int arr[3][4] = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
    int t = 13; 
    int rows = 3;
    int cols = 4;
    int result = searchEle(arr,t,rows,cols);
    if(result){
        printf("yes");
    }    
    else {
        printf("noo");
    }   
    return 0;
}

int searchEle(int arr[][4],int t,int rows,int cols)  // 1 2 3 -- 4 5 6 -- 7 8 9
{
    int row = 0;
    int col = cols-1;  //i.e (0,3)  ... 1  2  [3]
    
    while(row < rows && col >= 0){
        if(arr[row][col] == t){     
            return 1;
        }
        else if(arr[row][col] > t){
          col--;  
        }
        else {
            row++;
        }
    }
    return 0;
}
