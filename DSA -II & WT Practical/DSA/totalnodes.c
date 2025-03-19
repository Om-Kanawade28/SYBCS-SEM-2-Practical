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
// Function to count total node in the BST
int countnodes(struct Node* root)
{
 static int count=0;
 struct Node *temp = root;
 if(temp!=NULL)
 {
  count++;
  countnodes(temp->left);
  countnodes(temp->right);
 }
 return count;
}
int main() {
    // Input BST: [8,3,10,1,6,null,14,null,null,4,7,13,null]
    
    struct Node* root = NULL;
    root = insert(root, 8);
    root = insert(root, 3);
    root = insert(root, 10);
    root = insert(root, 1);
    root = insert(root, 6);
    root = insert(root, 4);
    root = insert(root, 7);
    root = insert(root, 14);
    root = insert(root, 13);
    
    int key;
    key= countnodes(root);
    printf("total nodes in tree = %d\n", key);
       
return 0;
}
