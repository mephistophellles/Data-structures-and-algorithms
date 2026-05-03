#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int OFFSET = 500000;
const int SIZE = 1000000;  // координаты после сдвига [0, 1000000]
                            // отрезки [x, x+l) с x+l <= 1000000

int N;

struct Node {
    long long sum;   // суммарная длина черного
    int cnt;         // количество максимальных черных подотрезков
    int lc, rc;      // цвет левой и правой крайней клетки
    int len;         // длина отрезка узла
};

vector<Node> tr;
vector<int> lazy;  // -1 = нет, 0 = белое, 1 = черное

inline void apply_assign(int v, int val) {
    tr[v].lc = val;
    tr[v].rc = val;
    tr[v].sum = (long long)val * tr[v].len;
    tr[v].cnt = (val == 1) ? 1 : 0;
    lazy[v] = val;
}

inline void pull(int v) {
    Node &L = tr[2 * v];
    Node &R = tr[2 * v + 1];
    Node &P = tr[v];
    P.sum = L.sum + R.sum;
    P.lc = L.lc;
    P.rc = R.rc;
    P.cnt = L.cnt + R.cnt;
    if (L.rc == 1 && R.lc == 1) P.cnt -= 1;
}

inline void push(int v) {
    if (lazy[v] != -1) {
        apply_assign(2 * v, lazy[v]);
        apply_assign(2 * v + 1, lazy[v]);
        lazy[v] = -1;
    }
}

void build(int v, int l, int r) {
    tr[v].len = r - l;
    tr[v].sum = 0;
    tr[v].cnt = 0;
    tr[v].lc = 0;
    tr[v].rc = 0;
    lazy[v] = -1;
    if (r - l == 1) return;
    int m = (l + r) >> 1;
    build(2 * v, l, m);
    build(2 * v + 1, m, r);
}

void update(int v, int vl, int vr, int l, int r, int val) {
    if (r <= vl || vr <= l) return;
    if (l <= vl && vr <= r) {
        apply_assign(v, val);
        return;
    }
    push(v);
    int m = (vl + vr) >> 1;
    update(2 * v, vl, m, l, r, val);
    update(2 * v + 1, m, vr, l, r, val);
    pull(v);
}

inline int readInt() {
    int x = 0, c, sign = 1;
    while ((c = getchar_unlocked()) != EOF && (c < '0' || c > '9') && c != '-');
    if (c == '-') { sign = -1; c = getchar_unlocked(); }
    do {
        x = x * 10 + c - '0';
    } while ((c = getchar_unlocked()) >= '0' && c <= '9');
    return x * sign;
}

inline char readChar() {
    int c;
    while ((c = getchar_unlocked()) != EOF && c != 'B' && c != 'W');
    return (char)c;
}

int main() {
    int n = readInt();
    
    N = 1;
    while (N < SIZE) N <<= 1;
    
    tr.assign(2 * N, Node());
    lazy.assign(2 * N, -1);
    
    build(1, 0, N);
    
    for (int q = 0; q < n; q++) {
        char c = readChar();
        int x = readInt();
        int l = readInt();
        
        int left = x + OFFSET;
        int right = left + l;  // полуинтервал [left, right)
        
        // Зажмём в [0, SIZE] на всякий случай
        if (left < 0) left = 0;
        if (right > SIZE) right = SIZE;
        if (right > N) right = N;
        if (left < right) {
            int val = (c == 'B') ? 1 : 0;
            update(1, 0, N, left, right, val);
        }
        
        printf("%d %lld\n", tr[1].cnt, tr[1].sum);
    }
    
    return 0;
}