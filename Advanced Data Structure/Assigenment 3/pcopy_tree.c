#include<stdio.h>
#include<stdlib.h>
struct node{
    int info;
    struct node *left,*right;
};
struct node *creatnode(int key){
    struct node *newnode = (struct node*)malloc(sizeof(struct node));
    newnode -> info = key;
    newnode -> left = newnode -> right = NULL;
    return newnode;

}
struct node *inserted(struct node *root,int key){
    if(root == NULL){
        return creatnode(key);
    }
    if(key < root -> info){
        root -> left = 
    }
}
int main(){


    return 0;
}