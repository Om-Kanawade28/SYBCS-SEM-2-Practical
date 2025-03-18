
// C program to implement binary search tree
#include <stdio.h>
#include <stdlib.h>
 
// Define a structure for a binary tree node
struct btreenode {
    int key;
    struct btreenode *left, *right;
};
 
// Function to create a new node with a given value
struct btreenode* newNodeCreate(int value)
{
    struct btreenode* temp
        = (struct btreenode*)malloc(
            sizeof(struct btreenode));
    temp->key = value;
    temp->left = temp->right = NULL;
    return temp;
}
 

// Function to insert a node with a specific value in the
// tree
struct btreenode*
insertNode(struct btreenode* node, int value)
{
    if (node == NULL) {
        return newNodeCreate(value);
    }
    if (value < node->key) {
        node->left = insertNode(node->left, value);
    }
    else if (value > node->key) {
        node->right = insertNode(node->right, value);
    }
    return node;
}
 

 
// Function to perform pre-order traversal
void preOrder(struct btreenode* root)
{
    if (root != NULL) {
        preOrder(root->left);
        printf(" %d ", root->key);
        preOrder(root->right);
    }
}
 
int main()
{
    // Initialize the root node
    struct btreenode* root = NULL;
 
    // Insert nodes into the binary search tree
    root = insertNode(root, 50);
    insertNode(root, 30);
    insertNode(root, 20);
    insertNode(root, 40);
    insertNode(root, 70);
    insertNode(root, 60);
    insertNode(root, 80);
    
    // Perform pre-order traversal
    preOrder(root);
    printf("\n");
     
    return 0;
}

// 20  30  40  50  60  70  80 

