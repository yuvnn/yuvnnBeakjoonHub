#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;
bool cmp(int a, int b) {
    return a > b;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N;
    cin >> N;
   
    vector<int>a(N);

    for (int i = 0; i<N; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end(), cmp);
    
    for (int i = 0; i < N; i++) {
        cout << a[i]<< "\n";
    }
}