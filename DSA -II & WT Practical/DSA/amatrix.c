#include<stdio.h>
void main()
{
 int m[5][5],  n, v, i, j;
 printf("how many vertices:");
 scanf("%d", &n);
 for(i=0; i<n; i++)
 for(j=0; j<n; j++)
 {
   m[i][j]=0;
   if(i!=j)
    { printf("is there is an edge between %d->%d(1/0):", i+1, j+1);
      scanf("%d", &m[i][j]); 
       
     } 
  }
for(i=0; i<n; i++){
 for(j=0; j<n; j++)
     { 
      printf("%d", m[i][j]);
      } 
     printf("\n");
  }
}
