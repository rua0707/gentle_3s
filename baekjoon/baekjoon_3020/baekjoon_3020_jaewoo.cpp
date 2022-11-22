//02:45:55
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, H;
vector<int> up;
vector<int> down;
vector<int> sumUp;
vector<int> sumDown;

int main(){

    //위쪽 아래쪽 모두 sorting
    //두 개를 나눠서 생각하기

    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> H;

    up.assign(N/2, 0);
    down.assign(N/2, 0);
    sumUp.assign(H+1, 0);
    sumDown.assign(H+1, 0);

    int temp;
    for(int i=0; i<N/2; i++){
        cin >> temp;
        down[i] = temp;
        cin >> temp;
        up[i] = temp;
    }

    sort(down.begin(), down.end(), greater<int>());
    sort(up.begin(), up.end(), greater<int>());

    int down_val = -1;
    int up_val = -1;
    int posUp;
    int posDown;
    int _sumUp = 0;
    int _sumDown = 0;

    for(int i=0; i<down.size(); i++){

        if(down_val == -1){
            posDown = down_val = down[i];
            posUp = up_val = up[i];
            _sumDown++;
            _sumUp++;
            continue;
        }

        if(down_val != down[i]){
            while(posDown > down[i]){
                sumDown[posDown--] = _sumDown;
            }
            down_val = down[i];
        }
        if(up_val != up[i]){
            while(posUp > up[i])
                sumUp[posUp--] = _sumUp;
            up_val = up[i];
        }

        _sumDown++;
        _sumUp++;

    }

    while(posUp >0 || posDown > 0){

        if(posUp>0)
            sumUp[posUp--] = _sumUp;
        if(posDown>0)
            sumDown[posDown--] = _sumDown;

    }

    int min_cnt = 0;
    int min_val = 2000001;
    for(int i=1; i<=H; i++){

        int cur = sumDown[i] + sumUp[H-i+1];

        if(min_val > cur){
            min_cnt=1;
            min_val = cur;
        }
        else if(min_val == cur)
            min_cnt++;

    }

    cout << min_val << " " << min_cnt;

    return 0;
}