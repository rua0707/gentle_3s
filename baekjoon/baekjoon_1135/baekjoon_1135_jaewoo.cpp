//01:50:24
#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>

using namespace std;

int N;
vector<vector<int>> tree;

int dfs(int pos){

    vector<int> v;
    int ret = 0;
    int w = tree[pos].size()-1;

    for(int i:tree[pos]){
        v.push_back(dfs(i));
    }

    sort(v.begin(), v.end());

    for(int i=0; i<v.size(); i++){
        ret = max(ret, v[i]+w--);
    }

    return ret+1;
}

int main(){

    cin >> N;

    tree.assign(N, {});

    int temp;
    for(int i=0; i<N; i++){

        cin >> temp;

        if(i==0) continue;

        tree[temp].push_back(i);

    }

    cout << dfs(0) -1;

    return 0;
}