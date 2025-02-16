
#include<iostream>
using namespace std;
class date{
    int dd,mm,yy;
    public:
       void accept();
       void display();
};
class student
{
    int rollno;
    char name[20];
    date bdate;
    float perc;
    public:
       void accept();
       void display();
};
void date::accept()
{
    cin>>dd>>mm>>yy;
}
void date::display()
{
    cout<<dd<<"/"<<mm<<"/"<<yy<<endl;
}
void student::accept()
{
    cout<<"Enter roll number,name:-";
    cin>>rollno>>name;
    cout<<"Enter birthdate(dd,mm,yy):-";
    bdate.accept();
    cout<<"Enter percentage:-";
    cin>>perc;
}
void student::display(){
    cout<<endl<<endl;
    cout<<"Roll Number = "<<rollno<<endl;
    cout<<"Name :-"<<name<<endl;
    cout<<"Birth Date :- ";`bdate.display();
    cout<<"Persentage :- "<<perc<<endl;

}
int main()
{
    student s[10];
    int i,n;
    cout<<"How many student objects? :- ";
    cin>>n;
    for(i=0;i<n;i++){
        s[i].accept();
    }
    cout<<"The student details are:\n";
    for(i=0;i<n;i++){
        s[i].display();
    }
    return 0;
}

