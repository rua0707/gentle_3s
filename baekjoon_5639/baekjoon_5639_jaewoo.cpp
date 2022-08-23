#include <iostream>

using namespace std;

struct Node{
    int value;
    Node* left;
    Node* right;
};

Node* insert(Node* root, int value){

    if(root == NULL){

        root = new Node;
        root->left = root->right = NULL;
        root->value = value;
        return root;
    }
    else{
        if(root-> value > value){
            root->left = insert(root->left, value);
        }
        else{
            root->right = insert(root->right, value);
        }
    }

    return root;

}

void postOrder(Node* root){

    if(root == NULL)
        return;

    postOrder(root->left);
    postOrder(root->right);
    printf("%d\n", root->value);

}

int main(){

    int n;
    Node* root = new Node;
    scanf("%d", &n);
    root->left = root->right = NULL;
    root->value = n;


    while(scanf("%d", &n) != EOF){
        insert(root, n);
    }

    postOrder(root);



    return 0;
}