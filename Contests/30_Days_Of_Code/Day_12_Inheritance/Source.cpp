#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
class Student{
    protected:
        string firstName;
        string lastName;
        int phone;
    public:
        Student(string fname,string lname,int p){
            firstName=fname;
            lastName=lname;
            phone=p;
        }
        void display(){
            cout<<"First Name: "<<firstName<<"\nLast Name: "<<lastName<<"\nPhone: "<<phone; 

        }
    
};
class Grade :  public Student{
    private:
         int score;   
    public:
        char calculate()
        {
            if(score < 40)
                return 'D';
            if(40 <= score && score < 60)
                return 'B';
            if(60 <= score && score < 75)
                return 'A';
            if(75 <= score && score < 90)
                return 'E';
            if(90 <= score && score <= 100)
                return 'O';
            return 'Z';
        }
        Grade(string fname, string lname, int p, int s)
        {
            Student(fname,lname,p);
            score = s;
        }
        Grade(string fname, string lname, int p)
        {
            Student(fname,lname,p);
            score = 0;
        }
};

int main() {
    string firstName,lastName;
    int score,phone;
    cin>>firstName;
    cin>>lastName;
    cin>>phone;
    cin>>score;    
    Student *stu=new Grade(firstName,lastName,phone,score);
    stu->display();
    Grade *g=(Grade*)stu;
    cout<< "\nGrade: "<<g->calculate();
    return 0;
}
