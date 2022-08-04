//01:39:09
#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
#include <iostream>

#define max(A, B) A<B ? B : A

using namespace std;

int N;
vector<vector<int>> graph;
vector<int> building_time;
vector<int> order;
int checking[501];
int dp[501];
//int answer[501];
queue<int> sorting_queue;

void init(){
    cin >> N;

    graph.assign(N+1, vector<int>());
    building_time.assign(N+1, 0);

    memset(checking, 0, sizeof(checking));
    memset(dp, 0, sizeof(dp));
//    memset(answer, 0, sizeof(answer));

    for(int i=1; i<=N; i++){

        int temp;

        cin >> temp;

        building_time[i] = temp;

        while(1){

            cin >> temp;

            if(temp == -1) break;

            graph[i].push_back(temp);

        }


    }
}

void checking_topo(){

    for(int i=1; i<=N; i++){

        vector<int> &cur = graph[i];
        int total = 0;

        for(int j=0; j<cur.size(); j++) {

            if(checking[cur[j]] == 1) continue;
            total++;

        }

        if(!checking[i] && total == 0){
            sorting_queue.push(i);
        }

    }

}

void topo(){

    while(order.size() < N){

        checking_topo();

        while(sorting_queue.size()){

            int idx = sorting_queue.front();
            sorting_queue.pop();

            order.push_back(idx);
            checking[idx] = 1;

        }

    }

}

void calculate(){

    for(int i=0; i<order.size(); i++){

        int idx = order[i];

        if(graph[idx].size() == 0){
            dp[idx] = building_time[idx];
        }
        else{
            int min_val = -1;
            for(int j=0; j<graph[idx].size(); j++) {
                min_val = max(min_val, dp[graph[idx][j]]);
            }

            dp[idx] = building_time[idx] + min_val;

        }


    }

}

int main(){

    init();
    topo();
    calculate();


    for(int i=1; i<=N; i++){
        printf("%d\n", dp[i]);
    }

    return 0;
}

//8
//10 -1
//10 1 -1
//4 1 -1
//4 3 1 -1
//3 3 -1
//4 -1
//10 2 -1
//10 6 -1