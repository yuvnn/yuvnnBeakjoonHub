#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;
struct d {
    int x;
    int y;
};

bool cmp(d a, d b) {
    if (a.y == b.y) {
        return a.x < b.x;
    }
    return a.y < b.y;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N;
    cin >> N;
   
    vector<d>pos(N);
    for (int i = 0; i<N; i++) {
        cin >> pos[i].x >> pos[i].y;
 
    }

    sort(pos.begin(), pos.end(), cmp);
    
    for (int i = 0; i < N; i++) {
        cout << pos[i].x << ' ' << pos[i].y << "\n";
    }
}