#include<stdio.h>
void indegree(int n,int m[5][5])
{
    int v,sumin,i;
    for(v=0; v<n; v++)
    {
     sumin= 0;
     for(i=0; i<n; i++)
      {
       sumin=sumin+m[i][v];
      
      
     } 
       printf("indegree of %d\t:-%d\n",v+1,sumin);
     }
}
int main()
{
 int m[5][5], n, i, j;
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
indegree(n,m);


return 0;
    
}
