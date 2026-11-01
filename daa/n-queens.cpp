#include<bits/stdc++.h>

using namespace std;
int board[20][20];

bool issafe(int row,int col,int n){
    //upperside
    for(int i=0;i<row;i++){
        if(board[i][col]==1) return false;

    }
    //upperleftdiagonal
    for(int i=row-1,j=col-1;i>=0 && j>=0;i--,j--){
         if (board[i][j] == 1)
            return false;
    }
    //upperrightdiagonal
    for(int i=row-1,j=col+1;i>=0,j<n;i--,j++){
        if (board[i][j] == 1)
            return false;
    }
    return true;

}

bool nqueen(int row,int n){
    if(row==n) return true;
    for(int col=0;col<n;col++){
        if(issafe(row,col,n)){
            board[row][col]=1;
            if(nqueen(row+1,n)) return true;
            board[row][col]=0;
        }
    }
    return false;
}

int main(){
    int n;
    cout<<"Enter  number of queens"<<endl;
    cin>>n;
    if(n<=0||n>20){
        cout<<"Inavlid boARD SIZE"<<endl;
        return 0;


    }
     for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            board[i][j] = 0;
        }
    }
    if (nqueen(0, n)) {

        cout << "\nSolution:\n";

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }

    } else {
        cout << "No solution exists";
    }

    return 0;
}
