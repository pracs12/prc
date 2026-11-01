#include<bits/stdc++.h>
using namespace std;

struct item{
    int profit,weight;
    double ratio;

};

bool compare(item a,item b){
    return a.ratio>b.ratio;
}

struct node{
    int lvl,profit,weight;
    double bound;
};

//calculate upper bound via fractional kp

double calbound(node u,int n,int capacity,vector<item>&items){
    if(u.weight>=capacity) return 0;
    double profitbound=u.profit;
    int totalweight=u.weight;
    int j=u.lvl+1;

    while(j<n && totalweight+items[j].weight<=capacity){
        totalweight+=items[j].weight;
        profitbound+=items[j].profit;
        j++;
    }

    if(j<n){
        profitbound+=(capacity-totalweight)*items[j].ratio;
    }
    return profitbound;
}

int knapsack(int capacity,vector<item>&items,int n){
    sort(items.begin(),items.end(),compare);
    queue<node>q;
    node u,v;
    u.lvl=-1;
    u.profit=0;
    u.weight=0;
    u.bound=calbound(u,n,capacity,items);
    q.push(u);
    int maxprofit=0;

    while(!q.empty()){
        u=q.front();
        q.pop();
        if (u.bound <= maxprofit)
            continue;
        v.lvl=u.lvl+1;
        if(v.lvl>=n) continue;
        v.weight = u.weight + items[v.lvl].weight;
        v.profit = u.profit + items[v.lvl].profit;

        if (v.weight <= capacity && v.profit > maxprofit) {
            maxprofit = v.profit;
        }

        v.bound = calbound(v, n, capacity, items);

        if (v.bound > maxprofit) {
            q.push(v);
        }
         v.weight = u.weight;
        v.profit = u.profit;

        v.bound = calbound(v, n, capacity, items);

        if (v.bound > maxprofit) {
            q.push(v);
        }
    }
    return maxprofit;
}
int main() {

    int n, capacity;

    cout << "Enter number of items: ";
    cin >> n;

    vector<item> items(n);

    cout << "Enter profit and weight of each item:\n";

    for (int i = 0; i < n; i++) {
        cin >> items[i].profit >> items[i].weight;

        items[i].ratio =
            (double)items[i].profit / items[i].weight;
    }

    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    cout << "Maximum Profit = "
         << knapsack(capacity, items, n);

    return 0;
}