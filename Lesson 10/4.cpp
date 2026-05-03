#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int OFFSET = 200000;
const int Y_RANGE = 400001;  // координаты y после сдвига [0, 400000]

int N;
vector<int> mx_tree;
vector<int> pos_tree;
vector<int> lazy;

void build(int v, int l, int r) {
    pos_tree[v] = l;  // любая позиция в отрезке
    mx_tree[v] = 0;
    lazy[v] = 0;
    if (r - l == 1) return;
    int m = (l + r) >> 1;
    build(2 * v, l, m);
    build(2 * v + 1, m, r);
}

inline void apply_add(int v, int val) {
    mx_tree[v] += val;
    lazy[v] += val;
}

inline void push(int v) {
    if (lazy[v] != 0) {
        apply_add(2 * v, lazy[v]);
        apply_add(2 * v + 1, lazy[v]);
        lazy[v] = 0;
    }
}

void update(int v, int vl, int vr, int l, int r, int val) {
    if (r <= vl || vr <= l) return;
    if (l <= vl && vr <= r) {
        apply_add(v, val);
        return;
    }
    push(v);
    int m = (vl + vr) >> 1;
    update(2 * v, vl, m, l, r, val);
    update(2 * v + 1, m, vr, l, r, val);
    if (mx_tree[2 * v] >= mx_tree[2 * v + 1]) {
        mx_tree[v] = mx_tree[2 * v];
        pos_tree[v] = pos_tree[2 * v];
    } else {
        mx_tree[v] = mx_tree[2 * v + 1];
        pos_tree[v] = pos_tree[2 * v + 1];
    }
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

struct Event {
    int x;       // координата события
    int y1, y2;  // диапазон по y (включительно), уже сдвинутый
    int delta;   // +1 или -1
};

int main() {
    int n = readInt();
    
    vector<Event> events;
    events.reserve(2 * n);
    
    for (int i = 0; i < n; i++) {
        int x1 = readInt();
        int y1 = readInt();
        int x2 = readInt();
        int y2 = readInt();
        // упорядочим на всякий случай (по условию (x1,y1) - левый верхний, (x2,y2) - правый нижний)
        if (x1 > x2) swap(x1, x2);
        if (y1 > y2) swap(y1, y2);
        
        int Y1 = y1 + OFFSET;
        int Y2 = y2 + OFFSET;
        
        events.push_back({x1, Y1, Y2, +1});
        events.push_back({x2 + 1, Y1, Y2, -1});
    }
    
    // Сортируем события по x. Порядок при равных x не важен (см. рассуждение).
    sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
        return a.x < b.x;
    });
    
    N = 1;
    while (N < Y_RANGE) N <<= 1;
    
    mx_tree.assign(2 * N, 0);
    pos_tree.assign(2 * N, 0);
    lazy.assign(2 * N, 0);
    build(1, 0, N);
    
    int best_cnt = 0;
    int best_x = 0;
    int best_y = 0;
    
    int total = (int)events.size();
    int i = 0;
    while (i < total) {
        int cur_x = events[i].x;
        // Применяем все события с координатой cur_x
        while (i < total && events[i].x == cur_x) {
            update(1, 0, N, events[i].y1, events[i].y2 + 1, events[i].delta);
            i++;
        }
        // Текущее состояние действует на [cur_x, next_x - 1]
        // Проверим максимум
        int cur_mx = mx_tree[1];
        if (cur_mx > best_cnt) {
            best_cnt = cur_mx;
            best_x = cur_x;
            best_y = pos_tree[1] - OFFSET;
        }
    }
    
    printf("%d\n%d %d\n", best_cnt, best_x, best_y);
    
    return 0;
}