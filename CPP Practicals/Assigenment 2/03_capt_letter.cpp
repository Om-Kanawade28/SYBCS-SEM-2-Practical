// write cpp prgram accept letter and convert into upper case
#include<iostream>
using namespace std;
int main(){
    char ch;
    cout<<"Enter the charcter:-";
    cin>>ch;

    ch = ch - 32;
    // ch = toupper(ch);

    cout<<"Your capital letter:-"<<ch;

    return 0;
}
// output:-
// Enter the charcter:-a
// Your capital letter:-A