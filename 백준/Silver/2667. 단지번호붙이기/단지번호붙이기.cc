#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> arr;
vector<int> cnt;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void dfs(int x, int y, int idx) {
    arr[x][y] = 0;          // 방문 처리
    cnt[idx]++;             // 현재 단지 크기 증가
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0 <= nx && nx < n && 0 <= ny && ny < n && arr[nx][ny]) {
            dfs(nx, ny, idx);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    arr.assign(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            arr[i][j] = s[j] - '0';
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[i][j]) {
                cnt.push_back(0);
                dfs(i, j, ans);
                ans++;
            }
        }
    }

    cout << ans << "\n";
    sort(cnt.begin(), cnt.end());
    for (int c : cnt) cout << c << "\n";

    return 0;
}
