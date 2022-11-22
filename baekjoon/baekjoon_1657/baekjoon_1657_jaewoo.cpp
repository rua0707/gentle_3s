#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int N, M;
int table[5][5] = {
        {10,8,7,5,1},
        {8,6,4,3,1},
        {7,4,3,2,1},
        {5,3,2,2,1},
        {1,1,1,1,0}
};
int board[15][15];
int dp[15*15][1<<14];

int dpf(int k, int s){

    int &ret = dp[k][s];

    if(ret != -1) return ret;

    ret = 0;

    if((s & 1) && (s & (1<<M))){
        return ret;
    }
    else if(s & 1) {// 이미 k+1이 있을 경우

        if(k+M >= N*M) return ret;

        ret = max(ret, max(table[board[(int)(k/M)][k%M]][board[(int)((k+M)/M)][(k+M)%M]] + dpf(k, s | (1<<M)),dpf(k+M, s >> M)));
    }
    else if(s & (1<<M)){

        if(k+1 >= N*M) return ret;

        ret = max(ret, max(table[board[(int)(k/M)][k%M]][board[(int)((k+1)/M)][(k+1)%M]] + dpf(k, s | 1),dpf(k+1, s >> 1)));
    }
    else{

        if(k+M >= N*M) return ret;

        ret = max(ret, max(table[board[(int)(k/M)][k%M]][board[(int)((k+M)/M)][(k+M)%M]] + dpf(k, s | (1<<M)),dpf(k+M, s >> M)));

        if(k+1 >= N*M) return ret;

        ret = max(ret, max(table[board[(int)(k/M)][k%M]][board[(int)((k+1)/M)][(k+1)%M]] + dpf(k, s | 1),dpf(k+1, s >> 1)));


    }

    return ret;

}

int main(){

    cin >> N >> M;

    char c;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
           cin >> c;
           if(c == 'F') board[i][j] = 4;
           else board[i][j] = c - 'A';
        }
    }

    memset(dp, -1, sizeof(dp));

    cout << dpf(0,0);

    return 0;
}