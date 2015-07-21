#include <bits/stdc++.h>

using namespace std;

int main(){
    
    int m, s;
    cin>>m>>s;
    
    string a(m,'0'), b(m,'0');
    int sa=0, sb=0;
    for(int i=0; i<m; i++){
        int d = min(9, s-sa);
        a[i] = '0' + d;
        sa += d;
        
        if(i+1<m && b[0]!='-'){
            d = min(9, s-sb-1);
            if(d<0){
                b="-1";
                continue;
            }
            b[m-i-1] = '0' + d;
            sb += d;
        }
    }
    
    int d = min(9, s-sb);
    b[0] = '0' + d;
    sb += d;
    
    if((b[0]>'0' && sb==s) || (s<=9 && m==1))
        cout<<b<<' ';
    else
        cout<<-1<<' ';
    if((a[0]>'0' && sa==s) || (s<=9 && m==1))
        cout<<a<<endl;
    else
        cout<<-1<<endl;

    return 0;
}
