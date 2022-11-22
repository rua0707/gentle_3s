#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector<int> v;
vector<int> sum_v;

int main(){

    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;

    int temp;
    for(int i=0; i<N; i++){
        cin >> temp;
        v.push_back(temp);

    }

    sum_v.assign(v.size(), 0);

    sum_v[0] = v[0];
    for(int i=1; i<v.size(); i++){
        sum_v[i] = v[i]+sum_v[i-1];
    }

    int s, e;
    for(int i=0; i<M; i++){
        cin >> s >> e;

        printf("%d\n", sum_v[e-1] - sum_v[s-1] + v[s-1]);


    }



    return 0;
}