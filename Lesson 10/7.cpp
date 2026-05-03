#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    ll W,H; int N;
    cin>>W>>H>>N;

    map<ll,set<pair<ll,int>>> diag;
    for(int i=0;i<N;i++){
        double x,y; cin>>x>>y;
        ll X=(ll)round(x*2), Y=(ll)round(y*2);
        diag[Y-X].insert({X,i});
    }

    map<ll,ll> M; set<pair<ll,ll>> S;
    M[0]=0; M[W]=LLONG_MAX; S.insert({0,0});
    vector<ll> res(N);

    for(int it=0; it<N; it++){
        auto isi=S.begin(); ll Y=isi->first, X=isi->second; S.erase(isi);

        auto mit=M.find(X);
        ll next_X=next(mit)->first;

        ll d = 2*(Y - X);
        auto& ds = diag[d];
        auto pit = ds.upper_bound({2*X, INT_MAX});
        ll Xc = pit->first; int idx = pit->second;
        ll s = Xc - 2*X;
        res[idx] = s;
        ds.erase(pit);

        ll Yn = Y + s, Xr = X + s;

        M.erase(mit);
        if(Xr < next_X){ M[Xr]=Y; S.insert({Y,Xr}); }

        auto rit = M.find(Xr);
        if(rit!=M.end() && rit->first!=W && rit->second==Yn){
            S.erase({rit->second, rit->first});
            M.erase(rit);
        }

        bool lm=false;
        auto lit = M.lower_bound(X);
        if(lit!=M.begin() && prev(lit)->second==Yn) lm=true;

        if(!lm){
            M[X]=Yn;
            if(Yn<H) S.insert({Yn,X});
        }
    }

    for(int i=0;i<N;i++) cout<<res[i]<<" ";
    cout<<"\n";
}
