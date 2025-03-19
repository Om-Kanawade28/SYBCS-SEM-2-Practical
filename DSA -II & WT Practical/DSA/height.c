#include <stdio.h>
#include <stdlib.h>
 
struct node
{
    int info;
    struct node* left, *right;
};
 

 
struct node* createnode(int key)
{
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    newnode->info = key;
    newnode->left = NULL;
    newnode->right = NULL;
 
    return(newnode);
}
 

int heightoftree(struct node* root)
{
    int max;
 
    if (root!=NULL)
    {
        
        int leftsubtree = heightoftree(root->left); 
       
        int rightsubtree = heightoftree(root->right);  
        if (leftsubtree > rightsubtree)
        {
            max = leftsubtree + 1;
            return max;
        }
        else
        {
            max = rightsubtree + 1;
            return max;
        }
    }
}
 

int main()
{
       struct node *newnode = createnode(25);
    newnode->left = createnode(27);
    newnode->right = createnode(19);
    newnode->left->left = createnode(17);
    newnode->left->right = createnode(91);
    //newnode->left->left->left = createnode(16);
    newnode->right->right = createnode(55);
     printf("Height of the first Tree is\t%d\n",heightoftree(newnode));
}
