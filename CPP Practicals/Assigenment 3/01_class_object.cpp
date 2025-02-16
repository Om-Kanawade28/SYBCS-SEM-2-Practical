#include<iostream>
using namespace std;
int main(){
    //class on stdent and object
class student{
    public:
        string name;
        int roll;
        int age;
};
 student s1;
    s1.name = "ram";
    s1.roll = 1;
    s1.age = 20;
    cout<<s1.name<<endl;
    cout<<s1.roll<<endl;
    cout<<s1.age<<endl;
    student s2;
    s2.name = "shyam";
    s2.roll = 2;
    s2.age = 22;
    cout<<s2.name<<endl;
    cout<<s2.roll<<endl;
    cout<<s2.age<<endl;
    return 0;
}