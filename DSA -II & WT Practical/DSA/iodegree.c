#include<stdio.h>
void main()
{
 int m[5][5], sumin, sumout, n, v, i, j, total;
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
 printf("\n\n vertex indegree  outdegree  totaldegree\n");
 for(v=0; v<n; v++)
  {
   sumin=sumout = 0;
   for(i=0; i<n; i++)
    {
     sumin=sumin+m[i][v];
     sumout = sumout+m[v][i];
     total = sumin+sumout;
    
   } 
     printf("%d\t%d\t%d\t%d\n",v+1,sumin, sumout, total);
   }
    
}
