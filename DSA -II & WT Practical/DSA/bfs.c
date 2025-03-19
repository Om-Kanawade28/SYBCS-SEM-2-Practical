#include<stdio.h>
#define MAXSIZE 20
typedef struct
{
  int data[MAXSIZE];
  int front,rear;
  }QUEUE;
  void addq(QUEUE *pq,int n)
  {
   pq->data[++pq->rear]=n; //Found Searching valu
}
  int removeq(QUEUE *pq)
{
   return pq->data[++pq->front];
}
 void initq(QUEUE *pq)
  {
  pq->front=pq->rear=-1;
 }
  int isempty(QUEUE *pq)
  {
  return(pq->rear==pq->front);
  } // m[i][j]=0;
  void bfs(int m[5][5],int n)
   {
  int i,j,v,w;
  int visited[20]={0};
  QUEUE q;
    initq(&q);
   printf("\n the breath first traversal is :\n");
   v=0;
  visited[v]=1;
  addq(&q,v);
  while(!isempty(&q)) //Found Searching valu
  {
  v=removeq(&q);
  printf("v%d",v+1);
   for(w=0;w<n;w++)
   if((m[v][w]==1)&&(visited[w]==0))
   {
  addq(&q,w);
  visited[w]=1;
  }
}
}
  void main()
{
  int m[5][5]={{0,0,1,1,0},{0,0,1,0,1},{0,1,0,0,0},{0,0,0,0,1},{0,0,0,0,0}};
  bfs(m,5);
 }

