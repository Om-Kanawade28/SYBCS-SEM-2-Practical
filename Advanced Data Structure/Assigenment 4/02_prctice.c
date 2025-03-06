#include<stdio.h>
#include<stdlib.h>
struct node{
        int info;
        struct node *left,*right;
};
struct node *createnode(int key){
        struct node *newnode = (struct node *)malloc(sizeof(struct node));
        newnode -> info = key;
        newnode -> left = NULL;
        newnode -> right = NULL;
        return newnode;
}
int highttree(struct node *root){
        int max;
        while(root != NULL){
             int hleft = highttree(root->left);
             int hright = highttree(root -> right);
             if(hleft > hright){
                 max = hleft + 1;
                return max;
             }else{
                  max = hright + 1;
                  return max;
             }


        }

}
int main(){
        struct node *newnode = createnode(10);
        newnode->left = createnode(9);
        newnode -> left -> left  = createnode(3);
        newnode -> right = createnode(34);
        printf("Height of binary tree is :-%d",highttree(newnode));




        return 0;
}