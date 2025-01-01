// Write program to calculate the simple intersest 
#include<iostream>
using namespace std;
int main(){
    int pamo,rate,time,SI;
    cout<<"Enter the Principle Amount:-";
    cin>>pamo;
    cout<<"Enter the Rate of interest:-";
    cin>>rate;
    cout<<"Enter the Time of Period:-";
    cin>>time;
    SI = (pamo*rate*time)/100;
    cout<<"Simple Interest is "<<SI;
    return 0;


}
// output:-
// Enter the Principle Amount:-20000
// Enter the Rate of interest:-2
// Enter the Time of Period:-1
// Simple Interest is 400