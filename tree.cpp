#include <bits/stdc++.h> 
using namespace std; 

struct TreeNode  
{  
    public: 
int data;  
struct TreeNode *left;  
struct TreeNode *right;  
};  

int Solve(TreeNode *Node)  
{  

    if(Node == NULL)  
    return 0;  

    int boomer = Node->data;  

    Node->data = Solve(Node->left) + Solve(Node->right);  

    return Node->data + boomer;  
}  

void SumTree(struct TreeNode* Node)  
{  
    if (Node == NULL)  
        return;  
    SumTree(Node->left);  
    cout<<" "<<Node->data;  
    SumTree(Node->right);  
}  

TreeNode* newNode(int data)  
{  
    TreeNode *tmpo = new TreeNode;  
    tmpo->data = data;  
    tmpo->left = NULL;  
    tmpo->right = NULL;  
      
    return tmpo;  
}  

int main()  
{  
    TreeNode *root = NULL;  
    int x;  

    root = newNode(10);  
    root->left = newNode(-2);  
    root->right = newNode(6);  
    root->left->left = newNode(8);  
    root->left->right = newNode(-4);  
    root->right->left = newNode(7);  
    root->right->right = newNode(5);  
      
    Solve(root);  

 
    SumTree(root);  
    return 0;  
}  