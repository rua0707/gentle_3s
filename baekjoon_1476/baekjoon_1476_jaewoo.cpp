#include <iostream>

using namespace std;


int main(){



    int e,s,m;
    cin >> e >> s >> m;

    int num = 1;

    while(1){

        if((num-e)%15 == 0 && (num-s)%28==0 && (num-m)%19 == 0){
            break;
        }
        else num++;

    }


    cout << num << "\n";

    return 0;
}