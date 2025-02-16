#include<iostream>
using namespace std;
class student
{
    int rno;
    char name[20];
    float perc;
public:
  void accept();
  void display();
};
void student::accept()
{
    cout<<"Enter the roll number,name and percentage :";
    cin>>rno>>name>>perc;


}
void student :: display()
{
    cout << "The roll number is : " <<rno<<endl;
    cout << "The name is :" << name<<endl;
    cout << "the percentage is : "<<perc<<endl;
}
//main function
int main()
{
    student s;
    s.accept();
    s.display();
    student *p;
    p=new student;
    p->accept();
    p->display();
    return 0;
}