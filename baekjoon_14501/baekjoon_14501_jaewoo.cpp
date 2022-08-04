#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int N;
int T[16];
int P[16];
int dp[1<<15];

int dfs(int idx, int day){

    int& ret = dp[day];

    if(ret != -1) return ret;

    ret = 0;

    int first = 0;
    int second = 0;

    if(idx+1 <= N)
        first = dfs(idx+1, day);

    if(idx+T[idx] <= N)
        second = P[idx] + dfs(idx+T[idx],day | (1<<(idx+T[idx])));

    return ret = max(first, second);

}

int main(){

    cin >> N;

    memset(dp, -1, sizeof(dp));

    for(int i=0; i<N; i++){

        cin >> T[i] >> P[i];

    }

    cout << dfs(0, 0);


    return 0;
}