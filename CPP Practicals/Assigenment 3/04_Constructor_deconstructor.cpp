#include<iostream>
#include<string.h> // For strcpy()
using namespace std;

class student
{
    int rno;
    char name[20];
    float perc;
public:
    student() // Constructor
    {
        rno = 0;
        strcpy(name, "Unknown");
        perc = 0.0;
        cout << "Constructor called!" << endl;
    }
    
    ~student() // Destructor
    {
        cout << "Destructor called for " << name << endl;
    }

    void accept();
    void display();
};

void student::accept()
{
    cout << "Enter Roll Number, Name, and Percentage: ";
    cin >> rno >> name >> perc;
}

void student::display()
{
    cout << "\nRoll Number: " << rno;
    cout << "\nName: " << name;
    cout << "\nPercentage: " << perc << endl;
}

int main()
{
    student s1; // Calls constructor
    s1.accept();
    s1.display();

    student *p = new student;
    p->accept();
    p->display();

    delete p; // Destructor called manually
    return 0;
}
