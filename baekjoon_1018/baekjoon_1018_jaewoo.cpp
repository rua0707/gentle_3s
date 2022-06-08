#include <iostream>
#include <string.h>

using namespace std;

int N, M;
char board[51][51];
int min_val = 80;

int solution(){

    for(int start_row=0; start_row<=N-8; start_row++){
        for(int start_col=0; start_col<=M-8; start_col++){

            int cntB = 0;
            int cntW = 0;

            for(int i=start_row; i<start_row+8; i++){
                for(int j=start_col; j<start_col+8; j++){

                    if((i+j)%2 == 0){
                        if(board[i][j] == 'B'){
                            cntW++;
                        }
                        else{
                            cntB++;
                        }
                    }
                    else{
                        if(board[i][j] == 'B'){
                            cntB++;
                        }
                        else{
                            cntW++;
                        }
                    }



                }
            }

            min_val = min_val > cntB ? cntB : min_val;
            min_val = min_val > cntW ? cntW : min_val;


        }
    }

    return min_val;

}

int main(){

    // input
    cin >> N >> M;

    char val;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){

            cin >> val;
            board[i][j] = val;

        }
    }

    cout << solution();






    return 0;
}