#include <iostream>
#include <stack>
#include <string>

using namespace std;

stack<char> st;
string answer;

void clear(){
    while(st.size()){
        answer.push_back(st.top());
        st.pop();
    }
}

int main(){

    string S;


    getline(cin, S);

    int i=0;

    while(i<S.size()){

        char c = S[i];

        if(c == ' '){
            clear();
            answer.push_back(' ');
        }
        else if(c == '<'){

            clear();

            while(c != '>'){
                answer.push_back(c);
                c = S[++i];
            }
            answer.push_back(c);

        }
        else{
            st.push(c);
        }

        i++;


    }

    clear();

    cout << answer << '\n';


    return 0;
}