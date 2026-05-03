#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const long long NO_ASSIGN = -1;  // признак «нет отложенного присваивания»

int N;
vector<long long> sum_tree, add_lazy, assign_lazy;
vector<int> len_node;

void apply_assign(int node, long long val) {
    sum_tree[node] = val * len_node[node];
    assign_lazy[node] = val;
    add_lazy[node] = 0;
}

void apply_add(int node, long long val) {
    sum_tree[node] += val * len_node[node];
    if (assign_lazy[node] != NO_ASSIGN) {
        assign_lazy[node] += val;
    } else {
        add_lazy[node] += val;
    }
}

void push(int node) {
    if (assign_lazy[node] != NO_ASSIGN) {
        apply_assign(2 * node, assign_lazy[node]);
        apply_assign(2 * node + 1, assign_lazy[node]);
        assign_lazy[node] = NO_ASSIGN;
    }
    if (add_lazy[node] != 0) {
        apply_add(2 * node, add_lazy[node]);
        apply_add(2 * node + 1, add_lazy[node]);
        add_lazy[node] = 0;
    }
}

void build(int node, int node_l, int node_r) {
    len_node[node] = node_r - node_l;
    if (node_r - node_l == 1) return;
    int mid = (node_l + node_r) >> 1;
    build(2 * node, node_l, mid);
    build(2 * node + 1, mid, node_r);
}

void update_assign(int node, int node_l, int node_r, int l, int r, long long val) {
    if (r <= node_l || node_r <= l) return;
    if (l <= node_l && node_r <= r) {
        apply_assign(node, val);
        return;
    }
    push(node);
    int mid = (node_l + node_r) >> 1;
    update_assign(2 * node, node_l, mid, l, r, val);
    update_assign(2 * node + 1, mid, node_r, l, r, val);
    sum_tree[node] = sum_tree[2 * node] + sum_tree[2 * node + 1];
}

void update_add(int node, int node_l, int node_r, int l, int r, long long val) {
    if (r <= node_l || node_r <= l) return;
    if (l <= node_l && node_r <= r) {
        apply_add(node, val);
        return;
    }
    push(node);
    int mid = (node_l + node_r) >> 1;
    update_add(2 * node, node_l, mid, l, r, val);
    update_add(2 * node + 1, mid, node_r, l, r, val);
    sum_tree[node] = sum_tree[2 * node] + sum_tree[2 * node + 1];
}

long long query_sum(int node, int node_l, int node_r, int l, int r) {
    if (r <= node_l || node_r <= l) return 0;
    if (l <= node_l && node_r <= r) return sum_tree[node];
    push(node);
    int mid = (node_l + node_r) >> 1;
    return query_sum(2 * node, node_l, mid, l, r)
         + query_sum(2 * node + 1, mid, node_r, l, r);
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
    
    sum_tree.assign(2 * N, 0);
    add_lazy.assign(2 * N, 0);
    assign_lazy.assign(2 * N, NO_ASSIGN);
    len_node.assign(2 * N, 0);
    
    build(1, 0, N);
    
    for (int q = 0; q < m; q++) {
        int op = readInt();
        if (op == 1) {
            int l = readInt();
            int r = readInt();
            long long v = readInt();
            update_assign(1, 0, N, l, r, v);
        } else if (op == 2) {
            int l = readInt();
            int r = readInt();
            long long v = readInt();
            update_add(1, 0, N, l, r, v);
        } else {
            int l = readInt();
            int r = readInt();
            printf("%lld\n", query_sum(1, 0, N, l, r));
        }
    }
    
    return 0;
}