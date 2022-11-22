#include <iostream>
#include <string>

using namespace std;

string N;
int number[10] = {0, };
int max_val = -1;

int main(){

    cin >> N;

    for(int i=0; i<N.size(); i++){
        int cur_num = N[i] - '0';
        if(cur_num == 6 || cur_num == 9){
            if(number[6] > number[9]) {
                number[9]++;
                max_val = number[9] > max_val ? number[9] : max_val;
            }
            else {
                number[6]++;
                max_val = number[6] > max_val ? number[6] : max_val;
            }
        }
        else{
            number[cur_num]++;
            max_val = number[cur_num] > max_val ? number[cur_num] : max_val;
        }


    }

    cout << max_val;

    return 0;
}