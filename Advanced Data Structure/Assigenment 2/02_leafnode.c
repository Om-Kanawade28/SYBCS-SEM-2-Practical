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
    if(root == NULL) {
        return createNode(value);

    }
    if(value < root -> data){
        root -> left = insert(root -> left,value);
    } else {
        root -> right = insert(root->right,value);
    }

    return root;
}
int leafNodes(struct Node* root){
    if(root == NULL){
        return 0;
    }
    if(root -> left == NULL && root -> right == NULL){
        return 1;
    }
    return leafNodes(root -> left) + leafNodes(root -> right);
}
int main() {
    struct Node* root = NULL;
    int n,i,a;
    printf("Enter the number of nodes to be inserted:-");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("Enter the element to be inserted:-");
        scanf("%d",&a);
        root = insert(root,a);

    }
    int count = leafNodes(root);
    printf("The number of leaf nodes are %d",count);
    return 0;
}
