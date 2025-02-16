#include<iostream>
using namespace std;
class date{
    int dd,mm,yy;
    public:
       void accept();
       void display();
};
class student{
    int rollno;
    char name[20];
    date bdate;
    float perc;
    public:
       void accept();
       void display();
};
void date::accept(){
    cin>>dd>>mm>>yy;
}
void date::display(){
    cout<<dd<<"/"<<mm<<"/"<<yy<<endl;
}
void student::accept(){
    cout<<"Enter the rollno and Name:- "<<endl;
    cin>>rollno>>name;
    cout<<"Birth Date(dd/mm/yy) :-";bdate.accept();
    cout<<"Persentage :- ";
    cin>>perc;
}
void student::display(){
    cout<<"roll no :-"<<rollno<<endl;
    cout<<"Name :- "<<name<<endl;
    cout<<"Birth Date:-";bdate.display();
    cout<<"Percentage :- "<<perc<<endl<<endl;
}
int main(){
    student s[10];
    int i,n;
    cout<<"Enter the no of objects:-";
    cin>>n;
    for(i=0;i<n;i++){
        s[i].accept();
    }
    for(i=0;i<n;i++)
    {
        s[i].display();
    }
    return 0;
}

