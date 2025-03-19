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
// Function to count leaf total node in the BST
void mirror(struct Node* root)
{
 
 struct Node *temp = root;
 struct Node *temp1;
 if(temp!=NULL)
 {
  if(temp->left!=NULL)
      mirror(temp->left);
  if(temp->right!=NULL)
      mirror(temp->right);
    temp1= temp->left;
    temp->left = temp->right;
    temp->right=temp1;
 }

}


void inorder(struct Node* root)
{
    if (root != NULL) {
        inorder(root->left);
        printf(" %d ", root->data);
        inorder(root->right);

    }
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
    printf("inorder traversal original tree");
    inorder(root);
    mirror(root);
    printf("\nafter mirror image inorder is");
     inorder(root);
       
return 0;
}
