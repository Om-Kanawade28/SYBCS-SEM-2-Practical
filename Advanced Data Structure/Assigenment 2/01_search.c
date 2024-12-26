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
    if(root==NULL){
        return createNode(value);
    }
    if(value < root -> data){
        root -> left = insert(root->left,value);
    } else {
        root -> right = insert(root->right,value);
    }
    return root;
}
struct Node* search(struct Node* root,int value){
    if(root == NULL || root -> data == value){
        return root;
    }
    if(value < root -> data){
        return search(root -> left,value);
    } else{
        return search(root -> right,value);
    }
}
int main() {
    struct Node* root = NULL;
    int n,i,a,key;
    printf("Enter the nodes to be inserted:-");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("Enter the element to be inserted:-");
        scanf("%d",&a);
        root = insert(root,a);

    }
    printf("Enter the element to be searched:-");
    scanf("%d",&key);
     
    struct Node* temp = search(root,key);
    if(temp!=NULL){
        printf("Element found");
    } else {
        printf("Element not found");
    }
    return 0;

}