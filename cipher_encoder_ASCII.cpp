#include<bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
int main()
{fastio;
    string s;int k;
    cin>>s;cin>>k;
    for(int i=0;i<s.length();i++)
    {int x,y;

        if(int(s[i])>=97 && int(s[i])<=122)
        {
            y=k%26;
            x=(int(s[i])-96);
            if(x+y>26)
            {
                cout<<char(y-(26-x)+96);
            }
            else
            {
                    cout<<char(x+y+96);
            }

        }
        if(int(s[i])>=65 && int(s[i])<=90)
        {
            y=k%26;x=(int(s[i])-64);
            if(x+y>26)
            {
                cout<<char(y-(26-x)+64);
            }
            else{cout<<char(x+y+64);}
        }
        


    }

}
