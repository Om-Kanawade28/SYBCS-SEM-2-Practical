//write program to calculate the volume of circle 
#include<iostream>
using namespace std;
int main(){
    int volume;
    int r,h;
    cout<<"Enter the radius of circle :- "<<endl;
    cin>>r;
    cout<<"Enter the height of circle :- "<<endl;
    cin>>h;
    volume = 3.14 * r * r * h;
    cout<<"Volume of circle = "<<volume;

    return 0;
}
// Enter the radius of circle :- 
// 3
// Enter the height of circle :- 
// 4
// Volume of circle = 113 