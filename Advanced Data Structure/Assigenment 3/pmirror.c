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
struct node *insertnode(struct node *root,int key){
    if(root == NULL){
        return creatnode(key);

    }
    if(key < root -> info){
        root -> left = insertnode(root -> left,key);
    }
    if(key > root -> info){
        root -> right = insertnode(root -> right,key);
    }
    return root;
}
void inorder(struct node *root){
    if(root != NULL){
        inorder(root);
        printf("%d ",root -> info);
        inorder(root);

    }
}
struct node *mirror(struct node *root){
    struct node *temp;
    while()
}
int main(){

    return 0;
}