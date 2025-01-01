#include<iostream>
using namespace std;
int main(){
    char ch;
    cout<<"Enter the letter(in capital letter):-";
    cin>>ch;
    ch = ch + 32;
    cout<<"your small letter:-"<<ch;

    return 0;
}
// output:-
// Enter the letter(in capital letter):-A
// your small letter:-a