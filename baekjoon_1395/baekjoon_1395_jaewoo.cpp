#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>

#define MAXSIZE 100001

using namespace std;

int N, M;
int tree[MAXSIZE*4];
int lazy[MAXSIZE*4];

void update_lazy(int node, int start, int end){

    if(lazy[node] != 0){


        if(start != end){
            tree[node] = (end-start+1) - tree[node];
            lazy[node*2] = (lazy[node*2]+1)%2;
            lazy[node*2+1] = (lazy[node*2+1]+1)%2;
        }
        else{
            tree[node] = (tree[node]+1)%2;
        }
        lazy[node] = 0;
    }

}

void update(int node, int left, int right, int start, int end){

    update_lazy(node, start, end);

    if(left > end || right < start) return;

    if(left <= start && end <= right){

        if(start != end){
            tree[node] = (end-start+1) - tree[node];
            lazy[node*2] = (lazy[node*2]+1)%2;
            lazy[node*2+1] = (lazy[node*2+1]+1)%2;
        }
        else{
            tree[node] = (tree[node]+1)%2;
        }
        return;
    }

    int mid = (start + end)/2;
    update(node*2, left, right, start, mid);
    update(node*2+1, left, right, mid+1, end);
    tree[node] = tree[node*2] + tree[node*2+1];


}

int find(int node, int start, int end, int left, int right){

    update_lazy(node, start, end);

    if(left > end || right < start) return 0;

    if(left <=start && end <= right) return tree[node];

    int mid = (start+end)/2;
    return find(node*2, start, mid, left, right) + find(node*2+1, mid+1, end, left, right);

}

int main(){

    cin >> N >> M;

    int O, S, T;

    for(int i=0; i<M; i++){
        scanf("%d %d %d", &O, &S, &T);

        if(O == 0){
            update(1, S, T, 1, N);
        }
        else{
            int ret = find(1, 1, N,S, T);
            printf("%d\n", ret);
        }

    }

    return 0;
}