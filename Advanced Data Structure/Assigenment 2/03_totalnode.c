#include<stdio.h>
#include<stdlib.h>
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
struct Node* createNode(int value){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> data = value;
    newNode -> left = NULL;
    newNode -> right = NULL;
    return newNode;
}
struct Node* insert(struct Node* root,int value) {
    if(root == NULL){
        return createNode(value);
    }
    if(value < root -> data){
        root -> left = insert(root -> left,value);
    } else{
        root -> right = insert(root -> right,value);
    }
    return root;
}
int countnodes(struct Node* root)
{
    static int count = 0;
    struct Node *temp = root;
    if(temp!=NULL)
    {
        count++;
        countnodes(temp->left);
        countnodes(temp->right);
        
    }
    return count;
}
int main(){
    struct Node* root = NULL;
    root = insert(root,5);    
    insert(root,3);
    insert(root,8);
    insert(root,1);
    insert(root,4);
    insert(root,7);
    insert(root,9);

    int count = countnodes(root);
    printf("The total number of nodes are %d",count);

    
    return 0;
}