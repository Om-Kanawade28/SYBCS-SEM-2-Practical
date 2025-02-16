#include<iostream>
using namespace std;
class student{
    int rno;
    char name[10];
    float perc;
public:
    void accept();
    void display();
};
void student :: accept(){
    cout << "Enter the roll number,name and persentage :";
    cin >>rno>>name>>perc;
}
void student :: display(){
    cout<<"roll no : "<<rno<<endl;
    cout<<"name : "<<name<<endl;
    cout<<"percentage : "<<perc<<endl;
}
int main(){
    int n;
    int i;
    cout<<"Entetr the no of student :-";
    cin >> n;
    student *s = new student[n];
    cout<<"Enter the student details:-"<<endl;
    for(i = 0;i<n;i++){
        s[i].accept();
    }
    cout<<"Displying the details of students:-"<<endl;
    for(i=0;i<n;i++){
        s[i].display();
    }

}