//02:08:25
#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#define max(a,b) (((a) > (b)) ? (a) : (b))

using namespace std;

int N, M;
int dp[21][301];
int path[21][301];
vector<vector<int>> investment;

int dfs(int company, int total_invest){

    int &ret = dp[company][total_invest];

    if(ret != 0)
        return ret;

    if(company == 0){
        for(int i=0; i<=total_invest; i++){

            int value = investment[i][company-1];
            if(value > ret){
                path[company][total_invest] = i;
                ret = value;
            }
        }

//        cout << company << " " << total_invest << " " << ret << " " << path[company][total_invest] << '\n';

        return ret;
    }

    ret = total_invest;

    for(int i=0; i<=total_invest; i++){

        int value = dfs(company-1, total_invest-i) + investment[i][company-1];
        if(value > ret){
            path[company][total_invest] = i;
            ret = value;

        }
    }

//    cout << company << " " << total_invest << " " << ret << " " << path[company][total_invest] << '\n';

    return ret;

}

int main(){

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    for(int i=0; i<21; i++){
        memset(dp[i], 0, sizeof(dp[i]));
        memset(path[i], 0, sizeof(path[i]));
    }


    cin >> N >> M;

    investment.assign(N+1, vector<int>(M, 0));

    int investNum;
    for(int i=0; i<N; i++){
        cin >> investNum;

        int temp;
        for(int j=0; j<M; j++){
            cin >> temp;
            investment[investNum][j] = temp;
        }

    }

    cout << max(N, dfs(M, N)) << '\n';

    vector<int> ans;
    int curr = M;
    int cost = N;
    while (curr > 0) {
        // dp[curr][cost] 를 최대로 만드는 현재 기업에서 투자하는 금액
        int now_invest = path[curr][cost];
        ans.push_back(now_invest);

        // 현재 기업에서 투자한 만큼 빼줌
        cost -= now_invest;
        // 이전 기업
        curr--;
    }

    reverse(ans.begin(), ans.end());
    for(int i=0; i<ans.size(); i++)
        printf("%d ", ans[i]);

//    int max_val = N;    //최대값
//    for(int i=0; i<N; i++){
//        max_val = max(max_val, dfs(M, i));
//    }






    return 0;
}