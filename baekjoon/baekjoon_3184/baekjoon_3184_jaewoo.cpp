#include <iostream>
#include <queue>
#include <string.h>

using namespace std;

int R, C;
int dir[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
char board[251][251];
bool check[251][251];
queue<pair<int, int>> q;
pair<int, int> count_creatures;
pair<int, int> total_count_creatures;

void counting(int r, int c){

    if(board[r][c] == 'o')
        count_creatures.first +=1;
    else if(board[r][c] == 'v')
        count_creatures.second +=1;

}

void bfs(int r, int c){

    count_creatures.first = 0;
    count_creatures.second = 0;

    check[r][c] = true;
    counting(r,c);
    q.push({r,c});

    while(q.size()){

        pair<int, int> cur = q.front();
        q.pop();

        for(int i=0; i<4; i++){
            int new_r = cur.first + dir[i][0];
            int new_c = cur.second + dir[i][1];

            if(new_r >= R || new_r < 0 || new_c >= C || new_c < 0)
                continue;
            if(check[new_r][new_c])
                continue;
            if(board[new_r][new_c] == '#')
                continue;

            counting(new_r, new_c);
            check[new_r][new_c] = true;
            q.push({new_r, new_c});

        }


    }


}

int main(){

    cin >> R >> C;

    char c;
    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++){
            cin >> c;
            board[i][j] = c;
        }
    }

    for(int i=0; i<251; i++)
        memset(check[i], 0, sizeof(check[i]));

    total_count_creatures.first = 0;
    total_count_creatures.second = 0;

    for(int i=0; i<R; i++){
        for(int j=0; j<C; j++){

            if(board[i][j] == '#')
                continue;

            if(check[i][j])
                continue;

            bfs(i,j);
            if(count_creatures.first > count_creatures.second)
                total_count_creatures.first += count_creatures.first;
            else
                total_count_creatures.second += count_creatures.second;

        }
    }

    cout << total_count_creatures.first << " " << total_count_creatures.second;


    return 0;
}