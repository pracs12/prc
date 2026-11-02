#include<iostream>
using namespace std;

// Recursive Fibonacci
int fib(int n){
    if(n==0) return 0;
    if(n==1) return 1;

    return fib(n-1)+fib(n-2);
}

// Iterative Fibonacci
void itfib(int n){
    int a=0,b=1;

    for(int i=0;i<n;i++){
        cout<<a<<" ";

        int c=a+b;
        a=b;
        b=c;
    }
}

// Recursive Tower of Hanoi
void TOH(int n, char source, char auxiliary, char destination){

    if(n==1){
        cout<<"Move disk 1 from "<<source
            <<" to "<<destination<<endl;
        return;
    }

    TOH(n-1,source,destination,auxiliary);

    cout<<"Move disk "<<n<<" from "
        <<source<<" to "<<destination<<endl;

    TOH(n-1,auxiliary,source,destination);
}

int main(){

    int n;

    // Fibonacci
    cout<<"Enter the number of terms for Fibonacci: ";
    cin>>n;

    cout<<"Recursive Fibonacci: ";
    for(int i=0;i<n;i++){
        cout<<fib(i)<<" ";
    }

    cout<<endl;

    cout<<"Iterative Fibonacci: ";
    itfib(n);

    cout<<endl<<endl;

    // Tower of Hanoi
    int disks;

    cout<<"Enter number of disks for Tower of Hanoi: ";
    cin>>disks;

    cout<<"Tower of Hanoi moves:"<<endl;

    if(disks>0){
        TOH(disks,'A','B','C');
    }

    return 0;
}
