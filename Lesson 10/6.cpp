#include <bits/stdc++.h>
using namespace std;

long long readDoubled() {
    // Читаем число, возможно с .5
    string s;
    cin >> s;
    int dot = s.find('.');
    long long sign = 1;
    int start = 0;
    if (s[0] == '-') { sign = -1; start = 1; }
    long long whole = 0;
    if (dot == (int)string::npos) {
        for (int i = start; i < (int)s.size(); i++) whole = whole * 10 + (s[i] - '0');
        return sign * 2 * whole;
    } else {
        for (int i = start; i < dot; i++) whole = whole * 10 + (s[i] - '0');
        long long doubled = 2 * whole;
        // дробная часть после точки
        if (dot + 1 < (int)s.size() && s[dot + 1] == '5') doubled += 1;
        return sign * doubled;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    long long W, H;
    int N;
    cin >> W >> H >> N;
    
    long long H2 = 2 * H;
    
    vector<long long> X(N), Y(N);
    vector<int> idx(N);
    
    for (int i = 0; i < N; i++) {
        X[i] = readDoubled();
        Y[i] = readDoubled();
        idx[i] = i;
    }
    
    sort(idx.begin(), idx.end(), [&](int a, int b) {
        if (X[a] != X[b]) return X[a] < X[b];
        return Y[a] < Y[b];
    });
    
    vector<long long> ans(N);
    
    map<long long, pair<long long, long long> > front;
    front[0] = make_pair(H2, 0LL);
    
    for (int k = 0; k < N; k++) {
        int i = idx[k];
        long long cx = X[i], cy = Y[i];
        
        auto it = front.upper_bound(cy);
        if (it == front.begin()) {
            ans[i] = -1;
            continue;
        }
        --it;
        long long y_low = it->first;
        long long y_high = it->second.first;
        long long x_left = it->second.second;
        
        long long s = cx - x_left;
        ans[i] = s;
        
        long long y_bot = cy - s;
        long long y_top = cy + s;
        
        front.erase(it);
        
        if (y_bot > y_low) front[y_low] = make_pair(y_bot, x_left);
        if (y_top > y_bot) front[y_bot] = make_pair(y_top, cx + s);
        if (y_high > y_top) front[y_top] = make_pair(y_high, x_left);
    }
    
    for (int i = 0; i < N; i++) {
        if (i > 0) cout << ' ';
        cout << ans[i];
    }
    cout << '\n';
    
    return 0;
}