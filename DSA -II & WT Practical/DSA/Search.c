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
struct Node* search(struct Node* root, int value) {
    if (root == NULL || root->data == value) {
        return root;
    }
    
    if (value < root->data) {
        return search(root->left, value);
    } else {
        return search(root->right, value);
    }
}
int main() {
    
    struct Node* root = NULL;
    int n, i, a, key;
 
   
    printf("enter the nodes to be inserted");
    scanf("%d", &n);
    for(i=0; i<n; i++)
    {
     printf("enter the element to be inserted");
     scanf("%d", &a); 
     root = insert(root,a );
     }
    printf("enter the element to be searched");
     scanf("%d", &key); 
   
    struct Node* result = search(root, key);
    
    if (result != NULL) {
        printf("Key %d, %dfound in the BST.\n", key, result);
    } else {
        printf("Key %d not found in the BST.\n", key);
    }
    
    return 0;
}
