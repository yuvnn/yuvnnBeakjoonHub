#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int n,m,j;
    cin >> n >> m;
    cin >> j;
    int cur = 1;
    int apple,ans=0;
    for (int i = 0; i<j; i++) {
        cin >> apple;
        if (apple < cur) {
            ans += cur-apple;
            cur = apple;
        }
        else if (cur + m-1 < apple) {
            ans += apple - (cur + m-1);
            cur = apple - m +1;
        }
    }
    cout << ans << "\n";
}