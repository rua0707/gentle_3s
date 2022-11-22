#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<long long> solution(vector<long long> numbers) {
    vector<long long> answer;

    for(int i=0; i<numbers.size(); i++){
        long long int bit=1;
        //짝수의 경우
        if(numbers[i]%2==0){
            answer.push_back(numbers[i]+1);
        }
            //홀수의 경우
        else{
            //연속된 1의 마지막 자리를 찾음
            while((numbers[i]&bit)!=0){
                bit*=2;
            }
            bit/=2;
            answer.push_back(numbers[i]+bit);
        }
    }

    return answer;
}

int main(){

    vector<long long> ret =  solution({2,7});

    for(int i=0; i<ret.size(); i++)
        cout << ret[i] << " ";
    cout << endl;

    return 0;
}