#include<iostream>
using namespace std;

int fib(int n){
    if(n==0) return 0;
    if(n==1) return 1;
    return fib(n-1)+fib(n-2);
}

void itfib(int n){
    int a=0,b=1;
    for(int i=0;i<n;i++){
        cout<<a<<" ";
        int c=a+b;
        a=b;
        b=c;
    }
}

int main(){
    int n;
    cout<<"Enter the number of terms for fib"<<endl;
    cin>>n;
    for(int i=0;i<n;i++){
        cout<<fib(i)<<" ";

    }
    cout<<endl;
    itfib(n);
    return 0;
}