#include <stdio.h>
int main()
{
    int m[5][5], v, i, j, n;
    printf("Enter the how many verties:-");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
        {
            m[i][j] = 0;
            if (i != j)
            {
                printf("Do you want to edge betwen %d -> %d(0,1)", i + 1, j + 1);
                scanf("%d", &m[i][j]);
            }
        }
    printf("Your matrix is:-\n");
    for (i = 0; i < n; i++){
        for (j = 0; j < n; j++)
        {

            printf(" %d", m[i][j]);
        }
       printf("\n") ;
    }
    return 0;
}