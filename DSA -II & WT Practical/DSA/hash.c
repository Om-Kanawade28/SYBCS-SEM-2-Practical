    #include<stdio.h>  
    int main()  
    {  
        int size, i, indexes[3];  
        int keys[3] = {10, 11, 12};  
        printf("Enter the size of the Hash Table: ");  
        scanf("%d", &size);  
        int M = size;   
        for(i = 0; i < 3; i ++)  
        {  
            indexes[i] = (keys[i] % M);  
        }  
        printf("\nThe indexes of the values in the Hash Table: ");  
        for(i = 0; i < 3; i++)  
        {  
            printf("%d ", indexes[i]);  
        }  
        return 0;  
    }  
