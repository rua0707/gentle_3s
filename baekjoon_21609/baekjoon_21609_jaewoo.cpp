#include <iostream>
#include <string.h>
#include <queue>
#include <vector>

using namespace std;

int N, M;
int board[21][21];
int check[21][21];
int dir[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

queue<pair<int, int> > q;
vector<pair<int, int> > memory;
vector<pair<int, int> > memoryTotal;

void init(){

    cin >> N >> M;

    for(int i=0; i<21; i++)
        memset(board[i], 0, sizeof(board[i]));

    //input

    int t;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
          cin >> t;

          board[i][j] = t;

        }
    }

}

int bfs(int r, int c, int norm){

    int total = 0;

    check[r][c] = 1;
    q.push(make_pair(r,c));
    memory.push_back(make_pair(r,c));
    total++;

    while(q.size()){

        pair<int, int> cur = q.front();
        q.pop();

        for(int i=0; i<4; i++){
            int new_r = cur.first + dir[i][0];
            int new_c = cur.second + dir[i][1];

            if(new_r >= N || new_r < 0 || new_c >= N || new_c < 0) continue;
            if(board[new_r][new_c] == -1 || board[new_r][new_c] == -2 || (board[new_r][new_c] != 0 && board[new_r][new_c] != norm)) continue;
            if(board[new_r][new_c] != 0 && check[new_r][new_c]) continue;

            // check zero가 다시 한번 필요
            // check zero가 안되면 계속 참조하게됨

            check[new_r][new_c] = 1;
            q.push(make_pair(new_r, new_c));
            memory.push_back(make_pair(new_r,new_c));
            total++;

        }



    }

    return total;


}

pair<int, int> findNorm(vector<pair<int, int>>& curPairVec){

    pair<int, int> norm = {-1,-1};

    for(int i=0; i<curPairVec.size(); i++){

        int r = curPairVec[i].first;
        int c = curPairVec[i].second;

        if(board[r][c] == 0) continue;

        if(r < norm.first || (r == norm.first && c < norm.second)){
            norm.first = r;
            norm.second = c;
        }

    }

    return norm;


}

int findRainbow(vector<pair<int, int>>& curPairVec){

    int rainbow = 0;

    for(int i=0; i<curPairVec.size(); i++){

        int r = curPairVec[i].first;
        int c = curPairVec[i].second;

        if(board[r][c] == 0) rainbow++;

    }

    return rainbow;

}

void findBigOne(){

    int totalSize = 1;
    for(int k=0; k<21; k++)
        memset(check[k], 0, sizeof(check[k]));

    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){

            if(check[i][j] || board[i][j] == 0 || board[i][j] == -1)
                continue;

            int curSize = bfs(i,j, board[i][j]);

            if(curSize > totalSize){

                totalSize = curSize;
                memoryTotal = memory;

//                for(int k=0; k<memory.size(); k++){
//
//                    board[memory[k].first][memory[k].second] = -2;
//
//                }

            }
            else if(curSize == totalSize){

                int prevRainbow = findRainbow(memoryTotal);
                int curRainbow = findRainbow(memory);

                if(prevRainbow < curRainbow){
                    memoryTotal = memory;
                }
                else if(prevRainbow == curRainbow){
                    pair<int, int> prevNorm = findNorm(memoryTotal);
                    pair<int, int> curNorm = findNorm(memory);

                    if(prevNorm.first < curNorm.first || (prevNorm.first == curNorm.first && prevNorm.second < curNorm.second)){
                        memoryTotal = memory;
                    }
                }

            }

            memory.clear();


        }
    }

}

int main(){


    init();
    findBigOne();
    cout << "";





    return 0;
}