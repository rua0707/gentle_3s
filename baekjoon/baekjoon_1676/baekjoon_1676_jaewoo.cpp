#include <iostream>
#include <algorithm>

using namespace std;

int N;

int main(){

    cin >> N;

    int cnt2 = 0;
    int cnt5 = 0;

    for(int i=N; i>0; i--){

        int cur = i;

        while(cur > 1){
            bool flag = false;

            if(cur%2 == 0){
                cur /= 2;
                cnt2++;
                flag = true;
            }
            if(cur%5 == 0){
                cur /=5;
                cnt5++;
                flag = true;
            }

            if(!flag) break;
        }

    }

    cout << min(cnt2, cnt5);


    return 0;
}