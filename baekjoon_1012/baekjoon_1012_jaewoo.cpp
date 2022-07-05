#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

int T, M, N, K;
int board[51][51] = {0,};
bool check[51][51] = {0,};
int dir[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

void dfs(int r, int c){

    for(int i=0; i<4; i++){
        int new_r = r+dir[i][0];
        int new_c = c+dir[i][1];

        if(new_r >= N ||new_r <0 ||new_c >=M || new_c <0) continue;

        if(check[new_r][new_c]) continue;
        if(!board[new_r][new_c]) continue;

        check[new_r][new_c] = true;
        dfs(new_r, new_c);
    }


}

void clear(){

    for(int i=0; i<51; i++){
        memset(board[i], 0, sizeof(board[i]));
        memset(check[i], 0, sizeof(check[i]));
    }

}

int main(){

    cin >> T;

    for(int i=0; i<T; i++){

        cin >> M >> N >> K;
        int x,y;

        clear();

        for(int j=0; j<K; j++){

            cin >> x >> y;

            board[y][x] = 1;

        }

        int ret = 0;

        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){

                if(check[i][j] || !board[i][j]) continue;

                ret++;
                check[i][j] = true;
                dfs(i,j);
            }
        }

        cout << ret << '\n';

    }



    return 0;
}