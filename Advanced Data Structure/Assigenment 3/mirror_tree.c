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
    else if(value > node -> key){
        node -> right = insertNode(node -> right,value);
    }
    return node;
}
void inOrder(struct btreenode *root){
    if(root != NULL){
        inOrder(root -> left);
        printf(" %d",root -> key);
        inOrder(root -> right);
    }
}
// mirror function for tree
struct btreenode* mirror(struct btreenode* node)
{
    struct btreenode* temp;
    if (node != NULL) {
        temp = node->left;
        node->left = mirror(node->right);
        node->right = mirror(temp);
    }
    return node;
}
void mirrorTree(struct btreenode* node)
{
    node = mirror(node);
    inOrder(node);
}

int main(){
    struct btreenode *root = NULL;
    root = insertNode(root,50);
    insertNode(root,10);
    insertNode(root,20);
    insertNode(root,30);
    insertNode(root,40);
    insertNode(root,50);
    insertNode(root,60);
    inOrder(root);
    printf("\n");
    mirrorTree(root);
    return 0;
}