#include <iostream>
#include <string>
#include <stack>

using namespace std;

int N;
stack<int> st;

int main(){

    cin >> N;

    for(int i=0; i<N; i++){
        string command;

        cin >> command;

        if(command.compare("push") == 0){
            int val;
            cin >> val;

            st.push(val);

        }
        else if(command.compare("pop") == 0){

            if (st.size() == 0){
                cout << "-1" << '\n';
            }
            else{
                cout << st.top() << '\n';
                st.pop();
            }


        }
        else if(command.compare("size") == 0){
            cout << st.size() << '\n';
        }
        else if(command.compare("empty") == 0){
            cout << (st.empty() ? 1 : 0)  << '\n';
        }
        else if(command.compare("top") == 0){
            if (st.size() == 0){
                cout << "-1" << '\n';
            }
            else{
                cout << st.top() << '\n';
            }
        }

    }


    return 0;
}