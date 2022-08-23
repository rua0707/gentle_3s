#include <iostream>
#include <string.h>

using namespace std;

int N;
int row[21];
int col[21];
int checking[1<<21];
int checking2[1<<21];
int total = 0;

void count(int check){

    if(checking2[check] == 0){

        int val = 0;

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if((col[i] & (1<<j)) == 1){
                    val++;
                }
            }
        }

        total = total < val ? val : total;

        checking2[check] = 1;
    }

}

void dfs2(int c, int check){

    if(c > N) return;

    count(check);

    dfs2(c+1, check);

    int prev = col[c];

    col[c] = (1<<N)-1 - col[c];//row 뒤집기

    dfs2(c+1, check | (1<<c));

    col[c] = prev;

}

void greedy(int check){

    if(checking[check] == 0){

        memset(col, 0, sizeof(col));

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(row[i] & (1<<j) == 1){
                    col[j] = col[j] | (1<<i);
                }
            }
        }

        dfs2(0,0);


        checking[check] = 1;
    }

}

void dfs(int r, int check){

    if(r > N) return;

    greedy(check);

    dfs(r+1, check);

    int prev = row[r];

    row[r] = (1<<N)-1 - row[r];//row 뒤집기

    dfs(r+1, check | (1<<r));

    row[r] = prev;

}

int main(){

    cin >> N;

    memset(row, 0, sizeof(row));
    memset(checking, 0, sizeof(checking));
    memset(checking2, 0, sizeof(checking2));

    char c;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin >> c;
            if(c == 'H'){
                row[i] = row[i] | (1<<j);
            }
        }
    }

    dfs(0,0);

    printf("%d", N*N - total);

    return 0;
}

//5
//HHTHH
//THHTT
//THTHH
//HHTHH
//THTHT