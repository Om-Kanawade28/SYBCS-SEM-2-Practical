#include<stdio.h>
#include<stdlib.h>
struct node{
    int info;
    struct node *left,*right;
};


struct node *createnode(int key){
     struct node *newnode = (struct node*)malloc(sizeof(struct node));
     newnode -> info = key;
     newnode -> left = NULL;
     newnode -> right = NULL;

     return(newnode);
}
int heightoftree(struct node *root)
{
    int max;
    if(root != NULL)
    {
        int leftsubtree = heightoftree(root->left);
        int rightsubtree = heightoftree(root->right);
        if(leftsubtree > rightsubtree)
        {
            max = leftsubtree + 1;
            return max;
        }else{
            max = rightsubtree + 1;
            return max;
        }
    }
}
int main()
{
    struct node *newnode = createnode(25);
    newnode-> left = createnode(27);
    newnode -> right = createnode(16);
    newnode -> left -> left = createnode(24);
    printf("Height of the first tree is %d",heightoftree(newnode));
}