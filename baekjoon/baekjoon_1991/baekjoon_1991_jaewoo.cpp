#include <iostream>
#include <map>
#include <string>

using namespace std;

int N;
map<char, pair<char, char>> tree;
string first_order;
string second_order;
string third_order;

void find(char cur){

    if(cur == '.') return;

    first_order.push_back(cur);

    find(tree[cur].first);
    second_order.push_back(cur);
    find(tree[cur].second);
    third_order.push_back(cur);


}

int main(){

    cin >> N;

    char node, left, right;

    for(int i=0; i<N; i++){

        cin >> node >> left >> right;

        tree[node] = pair<char,char>(left, right);

    }

    find('A');

    cout << first_order << endl;
    cout << second_order << endl;
    cout << third_order << endl;

    return 0;
}