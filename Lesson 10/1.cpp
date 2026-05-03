#include <cstdio>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int N;
vector<long long> tree, lazy;

void apply_add(int node, long long val) {
    tree[node] += val;
    lazy[node] += val;
}

void push(int node) {
    if (lazy[node] != 0) {
        apply_add(2 * node, lazy[node]);
        apply_add(2 * node + 1, lazy[node]);
        lazy[node] = 0;
    }
}

void update(int node, int node_l, int node_r, int l, int r, long long val) {
    if (r <= node_l || node_r <= l) return;
    if (l <= node_l && node_r <= r) {
        apply_add(node, val);
        return;
    }
    push(node);
    int mid = (node_l + node_r) >> 1;
    update(2 * node, node_l, mid, l, r, val);
    update(2 * node + 1, mid, node_r, l, r, val);
    tree[node] = min(tree[2 * node], tree[2 * node + 1]);
}

long long query(int node, int node_l, int node_r, int l, int r) {
    if (r <= node_l || node_r <= l) return LLONG_MAX;
    if (l <= node_l && node_r <= r) return tree[node];
    push(node);
    int mid = (node_l + node_r) >> 1;
    return min(
        query(2 * node, node_l, mid, l, r),
        query(2 * node + 1, mid, node_r, l, r)
    );
}

inline int readInt() {
    int x = 0, c;
    while ((c = getchar_unlocked()) < '0');
    do {
        x = x * 10 + c - '0';
    } while ((c = getchar_unlocked()) >= '0');
    return x;
}

int main() {
    int n = readInt();
    int m = readInt();
    
    N = 1;
    while (N < n) N <<= 1;
    if (N < 2) N = 2;
    
    tree.assign(2 * N, 0);
    lazy.assign(2 * N, 0);
    
    for (int q = 0; q < m; q++) {
        int op = readInt();
        if (op == 1) {
            int l = readInt();
            int r = readInt();
            long long v = readInt();
            update(1, 0, N, l, r, v);
        } else {
            int l = readInt();
            int r = readInt();
            printf("%lld\n", query(1, 0, N, l, r));
        }
    }
    
    return 0;
}