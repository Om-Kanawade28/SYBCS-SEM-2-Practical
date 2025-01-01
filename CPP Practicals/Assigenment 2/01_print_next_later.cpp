// write cpp program that accept character and give output next charcter 
#include<iostream>
using namespace std;
int main(){
    char ch;
    cout<<"Enter the character:-";
     
    cin>>ch;
    ch = ch + 1;
    cout<<"Next character is "<<ch;

    return 0;

}
// output:-
// Enter the character:-a
// Next character is b