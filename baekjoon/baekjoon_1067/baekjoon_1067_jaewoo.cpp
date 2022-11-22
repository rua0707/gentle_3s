#include <vector>
#include <complex>
#include <iostream>

using namespace std;

typedef complex<double> cpx;
typedef vector<cpx> vec;

const double pi = acos(-1); // cos(pi) = -1이기 때문에

void FFT(vec &f, cpx w){

    int n = f.size();
    if(n == 1) return;



}

int main(){

    int n = 5 >> 1;
    cout << n << endl;


    return 0;
}