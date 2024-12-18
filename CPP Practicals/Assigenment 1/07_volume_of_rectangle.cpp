//write program to volume of rectangle
#include<iostream>
using namespace std;
int main(){
    int l,w,h,volume;
    cout<<"Enter the length:-"<<endl;
    cin>>l;
    cout<<"Enter the width:-"<<endl;
    cin>>w;
    cout<<"Enter the height:-"<<endl;
    cin>>h;
    volume = l * w * h;
    cout<<"Volume of rectangle "<<l<<" * "<<w<<" * "<<h<<" = "<<volume;
    return 0;
}
// Enter the length:-
// 2
// Enter the width:-
// 4
// Enter the height:-
// 6
// Volume of rectangle 2 * 4 * 6 = 48