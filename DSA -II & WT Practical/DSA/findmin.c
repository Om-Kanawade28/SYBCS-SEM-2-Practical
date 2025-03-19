#include <stdio.h>
#include <stdlib.h>
// Structure for a BST node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
// Function to create a new node
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
// Function to insert a node into the BST
struct Node* insert(struct Node* root, int value) {
    if (root == NULL) {
        return createNode(value);
      
    }
        if (value < root->data) {
        root->left = insert(root->left, value);
    } else {
        root->right = insert(root->right, value);
    }
    
    return root;
}
// Function to search for a value in the BST
int min(struct Node* root)
 {
   struct Node *temp=root;
   while(temp!=NULL && temp->left!=NULL)
    temp=temp->left;
   return temp->data;
}
int main() {
    
    struct Node* root = NULL;
    int n, i, a, minvalue;
 
   
    printf("enter the nodes to be inserted");
    scanf("%d", &n);
    for(i=0; i<n; i++)
    {
     printf("enter the element to be inserted");
     scanf("%d", &a); 
     root = insert(root,a );
     }
       
    minvalue = min(root);
   printf("minimum value in tree is %d", minvalue);       
    return 0;
}
