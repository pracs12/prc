#include<iostream>
#include<queue>
#include<vector>
#include<map>
using namespace std;

struct node{
    char ch;
    int freq;
    node*left,*right;

    node(char c,int f){
        ch=c;
        freq=f;
        left=right=nullptr;


    }
};

struct compare{
    bool operator()(node*a,node*b){
        return a->freq>b->freq;
    }
};

void generatecodes(node*root,string code){
    if(root==nullptr){
        return;
    }
    if(!root->left && !root->right){
        cout<<root->ch<<":"<<code<<endl;
        return;
    }
    generatecodes(root->left,code+"0");
    generatecodes(root->right,code+"1");
}
void encode(node* root, string text, string code, map<char,string>& codes){
    if(root == nullptr) return;

    if(!root->left && !root->right){
        codes[root->ch] = code;
        return;
    }

    encode(root->left, text, code+"0", codes);
    encode(root->right, text, code+"1", codes);
}
node* huffmanencoding(string text){
    map<char,int>freq;
    for(char ch:text){
        freq[ch]++;
    }


    priority_queue<node*,vector<node*>,compare>pq;
    for(auto i:freq){
        pq.push(new node(i.first,i.second));

    }

    while(pq.size()>1){
        node*left=pq.top();
        pq.pop();
        node*right=pq.top();
        pq.pop();

        node*merged=new node('$',left->freq+right->freq);
        merged->left=left;
        merged->right=right;
        pq.push(merged);

    }
    cout << "\nHuffman Codes:\n";
    if(!pq.empty()){
        if(pq.top()->left == nullptr &&
           pq.top()->right == nullptr){
            cout << pq.top()->ch << " : 0" << endl;
        }
        else{
            generatecodes(pq.top(), "");
        }
    }
    return pq.empty()?nullptr:pq.top();
}
void decode(node* root, string encoded){
    if(root == nullptr) return;

    node* curr = root;

    cout << "\nDecoded Text: ";

    // Special case: only one unique character
    if(root->left == nullptr && root->right == nullptr){
        for(char bit : encoded){
            if(bit == '0')
                cout << root->ch;
        }
        cout << endl;
        return;
    }

    for(char bit : encoded){

        if(bit == '0'){
            curr = curr->left;
        }
        else if(bit == '1'){
            curr = curr->right;
        }

        // Leaf node reached
        if(!curr->left && !curr->right){
            cout << curr->ch;
            curr = root;
        }
    }

    cout << endl;
}
int main(){
    string text;

    cout << "Enter text: ";
    getline(cin, text);

    node* root = huffmanencoding(text);

    // Generate Huffman codes
    map<char,string> codes;

    if(root == nullptr){
        return 0;
    }

    if(root->left == nullptr && root->right == nullptr){
        codes[root->ch] = "0";
    }
    else{
        encode(root, text, "", codes);
    }

    // Encode text
    string encoded = "";

    for(char ch : text){
        encoded += codes[ch];
    }

    cout << "\nEncoded Text: " << encoded << endl;

    // Decode text
    decode(root, encoded);

    return 0;
}
