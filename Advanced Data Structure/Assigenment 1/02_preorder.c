#include<stdio.h>
#include<stdlib.h>
struct btreenode{
    int key;
    struct btreenode *left,*right;
};
struct btreenode* newNodeCreate(int value){
    struct btreenode *temp = (struct btreenode*)malloc(sizeof(struct btreenode));
    temp -> key = value;
    temp -> left = temp -> right = NULL;
    return temp;
}
struct btreenode* insertNode(struct btreenode *node,int value){
    if(node == NULL){
        return newNodeCreate(value);
    }
    if(value < node -> key)
    {
        node -> left = insertNode(node -> left,value);
    }
    else if
    (value > node -> key){
        node -> right = insertNode(node -> right,value);
    }
    return node;
}
void preOrder(struct btreenode *root){
    if(root != NULL){
        printf(" %d",root -> key);
        preOrder(root -> left);
        preOrder(root -> right);
    }
}
int main(){
    struct btreenode *root = NULL;
    root = insertNode(root, 50);
    insertNode(root, 10);
    insertNode(root, 30);
    insertNode(root, 60);
    insertNode(root, 80);
    preOrder(root);
    printf("\n");
    return 0;
}
