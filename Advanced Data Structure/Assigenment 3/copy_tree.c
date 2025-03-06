#include<stdio.h>
#include<stdlib.h>
struct btreenode{
    int key;
    struct btreenode *left,*right;
};
struct btreenode* newNodeCreate(int value){
    struct btreenode * temp = (struct btreenode*)malloc(sizeof(struct btreenode));
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
        node -> left = insertNode(node->left,value);
    }
    else if(value > node -> key){
        node -> right = insertNode(node -> right,value);
    }
    return node;
}
void inOrder(struct btreenode *root){
    if(root != NULL){
        inOrder(root->left);
        printf(" %d",root -> key);
        inOrder(root -> right);
    }
}
struct btreenode *treecopy(struct btreenode* root){
    struct btreenode *temp;
    if(root != NULL)
    {
      temp = (struct btreenode*)malloc(sizeof(struct btreenode));
      temp -> key = root ->key;
      temp -> left = treecopy(root -> left);
      temp -> right = treecopy(root -> right);
      return temp;

    }
}
int main(){
    struct btreenode *root = NULL;
    root = insertNode(root,50);
    insertNode(root,10);
    insertNode(root,20);
    insertNode(root,30);
    insertNode(root,40);
    insertNode(root,50);
    printf("\ninorder traversal original tree:-");
    inOrder(root);
    struct btreenode* root1 = treecopy(root);
    printf("\ninorder trversal of comp tree:-");
    inOrder(root1);
    printf("\n");
    return 0;
}