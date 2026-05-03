#include <cstdio>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

inline int readInt() {
    int x = 0, c, sign = 1;
    while ((c = getchar_unlocked()) != EOF && (c < '0' || c > '9') && c != '-');
    if (c == '-') { sign = -1; c = getchar_unlocked(); }
    do {
        x = x * 10 + c - '0';
    } while ((c = getchar_unlocked()) >= '0' && c <= '9');
    return x * sign;
}

// Дерево отрезков: точечные +/-, запрос «число позиций со значением > 0» на отрезке
int N_seg;
vector<int> val;
vector<int> cnt_pos;

void seg_init(int n) {
    N_seg = 1;
    while (N_seg < n) N_seg <<= 1;
    if (N_seg < 1) N_seg = 1;
    val.assign(N_seg, 0);
    cnt_pos.assign(2 * N_seg, 0);
}

void seg_point_update(int pos, int delta) {
    int old_v = val[pos];
    int new_v = old_v + delta;
    val[pos] = new_v;
    int old_ind = (old_v > 0) ? 1 : 0;
    int new_ind = (new_v > 0) ? 1 : 0;
    int change = new_ind - old_ind;
    if (change == 0) return;
    int v = pos + N_seg;
    cnt_pos[v] += change;
    v >>= 1;
    while (v) {
        cnt_pos[v] = cnt_pos[2 * v] + cnt_pos[2 * v + 1];
        v >>= 1;
    }
}

int seg_query(int l, int r) {
    int res = 0;
    l += N_seg;
    r += N_seg;
    while (l < r) {
        if (l & 1) res += cnt_pos[l++];
        if (r & 1) res += cnt_pos[--r];
        l >>= 1;
        r >>= 1;
    }
    return res;
}

struct Event {
    int x;
    int type;     // 0 = close, 1 = open, 2 = query
    int y1, y2;
    long long *res_ptr;
};

int main() {
    int n = readInt();
    
    vector<tuple<int,int,int> > H;  // (y, x1, x2)
    vector<tuple<int,int,int> > V;  // (x, y1, y2)
    
    for (int i = 0; i < n; i++) {
        int x1 = readInt(), y1 = readInt(), x2 = readInt(), y2 = readInt();
        if (y1 == y2) {
            int a = min(x1, x2), b = max(x1, x2);
            H.push_back(make_tuple(y1, a, b));
        } else {
            int a = min(y1, y2), b = max(y1, y2);
            V.push_back(make_tuple(x1, a, b));
        }
    }
    
    // Слияние горизонтальных с одинаковым y
    sort(H.begin(), H.end());
    vector<tuple<int,int,int> > H2;
    {
        size_t i = 0;
        while (i < H.size()) {
            int y = get<0>(H[i]);
            size_t j = i;
            vector<pair<int,int> > ints;
            while (j < H.size() && get<0>(H[j]) == y) {
                ints.push_back(make_pair(get<1>(H[j]), get<2>(H[j])));
                j++;
            }
            sort(ints.begin(), ints.end());
            int cur_l = ints[0].first, cur_r = ints[0].second;
            for (size_t k = 1; k < ints.size(); k++) {
                if (ints[k].first <= cur_r + 1) {
                    if (ints[k].second > cur_r) cur_r = ints[k].second;
                } else {
                    H2.push_back(make_tuple(y, cur_l, cur_r));
                    cur_l = ints[k].first;
                    cur_r = ints[k].second;
                }
            }
            H2.push_back(make_tuple(y, cur_l, cur_r));
            i = j;
        }
    }
    
    // Слияние вертикальных с одинаковым x
    sort(V.begin(), V.end());
    vector<tuple<int,int,int> > V2;
    {
        size_t i = 0;
        while (i < V.size()) {
            int x = get<0>(V[i]);
            size_t j = i;
            vector<pair<int,int> > ints;
            while (j < V.size() && get<0>(V[j]) == x) {
                ints.push_back(make_pair(get<1>(V[j]), get<2>(V[j])));
                j++;
            }
            sort(ints.begin(), ints.end());
            int cur_l = ints[0].first, cur_r = ints[0].second;
            for (size_t k = 1; k < ints.size(); k++) {
                if (ints[k].first <= cur_r + 1) {
                    if (ints[k].second > cur_r) cur_r = ints[k].second;
                } else {
                    V2.push_back(make_tuple(x, cur_l, cur_r));
                    cur_l = ints[k].first;
                    cur_r = ints[k].second;
                }
            }
            V2.push_back(make_tuple(x, cur_l, cur_r));
            i = j;
        }
    }
    
    // Площади H и V (сумма длин клеточных интервалов)
    long long H_area = 0;
    for (size_t k = 0; k < H2.size(); k++) {
        H_area += (long long)(get<2>(H2[k]) - get<1>(H2[k]) + 1);
    }
    long long V_area = 0;
    for (size_t k = 0; k < V2.size(); k++) {
        V_area += (long long)(get<2>(V2[k]) - get<1>(V2[k]) + 1);
    }
    
    // Sweep line по x для подсчёта |H ∩ V|
    vector<Event> events;
    events.reserve(2 * H2.size() + V2.size());
    
    for (size_t k = 0; k < H2.size(); k++) {
        int y = get<0>(H2[k]), x1 = get<1>(H2[k]), x2 = get<2>(H2[k]);
        Event e1; e1.x = x1;     e1.type = 1; e1.y1 = y; e1.y2 = 0; e1.res_ptr = NULL;
        Event e2; e2.x = x2 + 1; e2.type = 0; e2.y1 = y; e2.y2 = 0; e2.res_ptr = NULL;
        events.push_back(e1);
        events.push_back(e2);
    }
    
    vector<long long> v_results(V2.size(), 0);
    for (size_t k = 0; k < V2.size(); k++) {
        int x = get<0>(V2[k]), y1 = get<1>(V2[k]), y2 = get<2>(V2[k]);
        Event e; e.x = x; e.type = 2; e.y1 = y1; e.y2 = y2; e.res_ptr = &v_results[k];
        events.push_back(e);
    }
    
    sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
        if (a.x != b.x) return a.x < b.x;
        return a.type < b.type;  // close (0) -> open (1) -> query (2)
    });
    
    // Сжатие y
    vector<int> ys;
    ys.reserve(H2.size() + 2 * V2.size());
    for (size_t k = 0; k < H2.size(); k++) ys.push_back(get<0>(H2[k]));
    for (size_t k = 0; k < V2.size(); k++) {
        ys.push_back(get<1>(V2[k]));
        ys.push_back(get<2>(V2[k]));
    }
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());
    
    seg_init((int)ys.size());
    
    for (size_t k = 0; k < events.size(); k++) {
        Event &e = events[k];
        if (e.type == 0) {
            int idx = (int)(lower_bound(ys.begin(), ys.end(), e.y1) - ys.begin());
            seg_point_update(idx, -1);
        } else if (e.type == 1) {
            int idx = (int)(lower_bound(ys.begin(), ys.end(), e.y1) - ys.begin());
            seg_point_update(idx, +1);
        } else {
            int l = (int)(lower_bound(ys.begin(), ys.end(), e.y1) - ys.begin());
            int r = (int)(upper_bound(ys.begin(), ys.end(), e.y2) - ys.begin());
            if (l < r) {
                int active = seg_query(l, r);
                *(e.res_ptr) = active;
            }
        }
    }
    
    long long inter_area = 0;
    for (size_t k = 0; k < v_results.size(); k++) inter_area += v_results[k];
    
    long long ans = H_area + V_area - inter_area;
    printf("%lld\n", ans);
    
    return 0;
}