#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N,K,S,X,Y;

struct Virus{
    int r,c,num,t;
};

struct compare{
    bool operator()(Virus &I, Virus &C){

        if(I.t == C.t)
            return I.num > C.num;
        return I.t > C.t;

    }
};

int board[201][201];
int dir[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
priority_queue<Virus, vector<Virus>, compare> pq;


void bfs(){

    while(pq.size()){

        Virus cur = pq.top();
        pq.pop();

        if(cur.r == X-1 && cur.c == Y-1) return;
        if(cur.t >= S) return;

        for(int i=0; i<4; i++){

            int new_r = cur.r+dir[i][0];
            int new_c = cur.c+dir[i][1];

            if(new_r >= N || new_r < 0 || new_c >= N || new_c < 0) continue;
            if(board[new_r][new_c] != 0) continue;

            board[new_r][new_c] = cur.num;
            pq.push({new_r, new_c, cur.num, cur.t+1});
        }

    }


}

int main(){


    cin >> N >> K;

    int temp;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){

            cin >> temp;
            board[i][j] = temp;
            if(board[i][j] != 0){
                pq.push({i,j,temp,0});
            }


        }
    }

    cin >> S >> X >> Y;

    bfs();

    printf("%d", board[X-1][Y-1]);




    return 0;
}