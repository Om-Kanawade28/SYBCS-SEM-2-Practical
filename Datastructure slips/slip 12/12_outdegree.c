#include<stdio.h>
void outdegree(int n,int m[5][5]){
    int sumout,v,i;
    for(v=0;v<n;v++){
        sumout = 0;
        for(i=0;i<n;i++){
            sumout = sumout + m[v][i];
        }
        printf("Outdegree of the %d verties is %d\n",v+1,sumout);
    }
}
int main(){
    int n,i,j,m[5][5];
    printf("How may vertieses:-");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    for(j=0;j<n;j++){
        m[i][j]=0;
        if(i!=j){
            printf("is there edge betwen the %d -:> %d",i+1,j+1);
            scanf("%d",&m[i][j]);
        }
    }
    outdegree(n,m);
    return 0;
}