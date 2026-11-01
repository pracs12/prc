#include<bits/stdc++.h>

using namespace std;

struct item{
    int profit,weight;
    double ratio;

};

bool compare(item a, item b){
    return a.ratio > b.ratio;
}

int main(){
    int n,capacity;
    cout<<"Enter nummber of items"<<endl;
    cin>>n;
    vector<item>st(n);
    cout<<"Enter profit and weights"<<endl;
    for(int i=0;i<n;i++){
        cin>>st[i].profit>>st[i].weight;
        st[i].ratio=(double)st[i].profit/st[i].weight;

    }
    cout<<"Enter knapsack capacity"<<endl;
    cin>>capacity;

    sort(st.begin(),st.end(),compare);
    double  totalprofits=0;
    for(int i=0;i<n;i++){
        if(capacity==0) break;
        if(st[i].weight<=capacity){
            totalprofits+=st[i].profit;
            capacity-=st[i].weight;

        }
        else{
            totalprofits+=st[i].ratio*capacity;
            capacity=0;
        }
    }
    cout << "Maximum Profit = " << totalprofits << endl;

    return 0;
}