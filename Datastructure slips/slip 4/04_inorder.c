#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *left;
    struct node *right;
};
struct node *new_node(int key){
    struct node *newnode;
    newnode = (struct node*)malloc(sizeof(struct node));
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
}
void inorder(struct node *root){
    if(root != NULL){
        inorder(root -> left);
        printf("%d ",root -> data);
        inorder(root -> right);
    }
}
int main(){
   struct node *root =NULL;
   root = tree(root,3);
   tree(root,4);
   tree(root,6);
   tree(root,9);
   tree(root,61);
   inorder(root);

    return 0;
}