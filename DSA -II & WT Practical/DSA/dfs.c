
#include<stdio.h>
void main()
{
 int m[3][3]={{0,1,0}, {0,0,1}, {0,0,0}};
 
 printf("\n The depth first search traversal is:");
 dfs(m,3,0);
}
int dfs(int m[3][3], int n, int v)
{
 int w;
 static int visited[20]={0};
 visited[v]=1;
 printf("V%d", v+1);
 for(w=0; w<n; w++)
 {
  if((m[v][w]==1)&&(visited[w]==0))
     dfs(m,n,w);
  }
}


