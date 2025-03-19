#include<stdio.h>
#include<stdlib.h>
struct btreenode
{
int key;
struct btreenode *left, *right;
};
struct btreenode* newNodeCreate(int value)
{
struct btreenode* temp
=(struct btreenode*)malloc(sizeof(struct btreenode));
temp->key=value;
temp->left=temp->right=NULL;
return temp;
}

struct btreenode*
insertNode(struct btreenode* node,int value)
{
if(node==NULL)
{
return newNodeCreate(value);
}
if(value < node->key)
{
node->left = insertNode(node->left,value);
}
else if(value > node->key)
{
node->right = insertNode(node->right,value);
}
return node;
}
void preOrder(struct btreenode* root)
{
if(root != NULL)
{
printf("%d\t",root->key);
preOrder(root->left);
preOrder(root->right);
}
}
void inOrder(struct btreenode* root)
{
if(root != NULL)
{
inOrder(root->left);
printf("%d\t",root->key);
inOrder(root->right);
}
}
void postOrder(struct btreenode* root)
{
if(root != NULL)
{
postOrder(root->left);
postOrder(root->right);
printf("%d\t",root->key);
}
}
int main()
{
struct btreenode* root=NULL;
int n, a, i;
printf("how many nodes to insert");
scanf("%d", &n);
for(i=0; i<n;i++)
{
 printf("enter element");
scanf("%d", &a);
root = insertNode(root,a);
}
int choice;
do{
printf("choose travelsal type\n");
printf("1.preOrder\n");
printf("2.inOrder\n");
printf("3.postOrder\n");
printf("enter your choice");
scanf("%d",&choice);

{
switch(choice)
{
case 1:
printf("PreOrder");
preOrder(root);
break;
case 2:
printf("inOrder");
inOrder(root);
break;
case 3:
printf("postOrder");
postOrder(root);
break;
}
printf("\n");
}
}
while(choice !=3);
return 0;

}
