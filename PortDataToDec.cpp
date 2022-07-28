#include <bits/stdc++.h>
using namespace std;

#define DATASIZE 100

string s[DATASIZE];


int main()
{
    cout<<"This program is inteded to transform the data from the port into the decimal representation."<<endl;
    cout<<"Please input the port data."<<endl;
    for(int i=0; i<DATASIZE;i++)
    {
        //cin>>s[i];
        getline(cin,s[i]);
    }
    for(int i=0;i<DATASIZE;i++)
    {
        string temp;
        temp=s[i].substr(6,8);
        int tempnum;
        tempnum=std::stoi(temp);
        //cout<<temp<<endl;
        //cout<<tempnum<<endl;
        int x = stoi(temp, nullptr, 16);
        cout << x <<endl;
    }
    cout<<"Done."<<endl;
    return 0;
}