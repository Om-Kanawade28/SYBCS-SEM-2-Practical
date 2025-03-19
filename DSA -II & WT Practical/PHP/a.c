#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *left;
    struct node *right;
};
struct node *new_node(int key){
    struct node *newnode = (struct node*)malloc(sizeof(struct node));
    newnode -> data = key;
    newnode -> left = newnode -> right = NULL;
    return newnode;
}
struct node *tree(struct node *root,int key){
    if(root == NULL){
        return new_node(key);
    }
    if(key < root -> data){
        root -> left = tree(root -> left,key);
    }else{
        root -> right = tree(root -> right,key);
    }
    return root;
}
int total_node(struct node *root){
    struct node *temp = root;
    int total = 0;
    while(temp != NULL){
        total++;
        total_node(temp -> left);
        total_node(temp->right);
    }
    return total;
}
int main(){
    struct node *root = NULL;
    root = tree(root,3);
    tree(root,4);
    tree(root,6);
    tree(root,9);
    tree(root,61);
    printf(" toatal number of the node:-%d",total_node(root));

    return 0;
}