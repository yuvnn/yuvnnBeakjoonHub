#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N, k;
    cin >> N >> k;
    vector<int>a;
    a = vector<int>(N, 0);
    vector <int>::iterator itor = a.begin();
    for (int i = 0; i<N; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    cout << a[k-1] <<endl;
}