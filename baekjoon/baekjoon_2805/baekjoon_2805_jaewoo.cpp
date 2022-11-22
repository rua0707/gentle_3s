#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector<int> tree;

// output : -1(low), 0(correct), 1(high)
int cutTree(int standard){

    int total = 0;
    for(int i=0; i<N; i++){

        int val = tree[i] - standard;

        if(val <= 0) continue;

        total += val;

        if(total > M) return 1;
    }

    return total == M ? 0 : -1;

}

int main(){

    cin >> N >> M;

    tree.assign(N, 0);

    int temp;
    for(int i=0; i<N; i++){
        cin >> temp;
        tree[i] = temp;
    }

    int low=0, high=1000000001;

    while(low < high){

        int mid = (low+high)/2;

        int out = cutTree(mid);

        if(out == 0) {
            cout << mid;
            return 0;
        }
        else if(out == -1){
            high = mid;
        }
        else{
            low = mid+1;
        }

    }

    cout << high-1;




    return 0;
}